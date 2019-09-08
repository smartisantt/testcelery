from django.http import HttpResponse
from django.core.cache import cache

# Create your views here.
from django.views.decorators.cache import cache_page

from app.tasks import add


def test(request):
    for i in range(10000):
        add.delay(0, i)
    return HttpResponse("计算完毕")
