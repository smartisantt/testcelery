from django.db import models

# Create your models here.

class Result(models.Model):
    uuid = models.CharField(max_length=64, unique=True, null=True)
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", null=True)
    updateTime = models.DateTimeField(auto_now=True, verbose_name="更新时间", null=True)
    result = models.IntegerField( null=True)

    class Meta:
        db_table = "tb_result"
