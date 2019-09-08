from __future__ import absolute_import, unicode_literals
# from celery import app
from uuid import uuid4

from app.models import Result
from testcelery.celery import app


@app.task
def add(x, y):
    # 处理完毕存数据库
    Result.objects.create(
        uuid=uuid4().hex,
        result=x+y
    )
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)