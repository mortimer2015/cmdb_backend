from django.db import models
from jsonfield import JSONField

# Create your models here.

assets_status = (
    ('1', '在线'),
    ('2', '维修'),
    ('3', '故障'),
    ('4', '未知'),
)

groups_status = (
    ('1', '启用'),
    ('2', '禁止'),
    ('3', '未知'),
)


class AssetType(models.Model):
    name = models.CharField(max_length=256, unique=True)
    describe = models.TextField(null=True, blank=True)
    raw = JSONField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class Groups(models.Model):
    name = models.CharField(max_length=256, unique=True, null=False)
    status = models.CharField(max_length=256, choices=groups_status, default=groups_status[0])
    describe = models.TextField(null=True, blank=True)
    raw = JSONField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class Assets(models.Model):
    name = models.CharField(max_length=256, null=True)
    status = models.CharField(max_length=256, choices=assets_status, default=assets_status[0])
    groups = models.ManyToManyField(Groups)
    type = models.ForeignKey(AssetType, on_delete=True)
    describe = models.TextField(null=True, blank=True)
    raw = JSONField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)



