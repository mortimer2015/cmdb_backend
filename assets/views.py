from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from . import models
# Create your views here.


def generate_success_ret(data=None):
    ret = {
        'data': data,
        'status': 200,
        'message': 'success',
    }
    return ret


def generate_not_found_ret():
    return {'status': '404', 'message': 'not found'}


class Assets(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        asset_list = models.Assets.objects.all()
        data = [
            {
                'id': asset.id,
                'name': asset.name,
                'status': asset.status,
                'type': asset.type.name
             } for asset in asset_list
        ]
        ret = generate_success_ret(data)
        return Response(ret)


class AssetView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, asset_id):
        try:
            asset = models.Assets.objects.filter(pk=asset_id).first()
            data = {
                'name': asset.name,
                'groups': [group.name for group in asset.groups.all()],
                'describe': asset.describe,
                'raw': asset.raw,
            }
            return Response(generate_success_ret(data))
        except:
            return Response(generate_not_found_ret())
