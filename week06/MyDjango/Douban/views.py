from django.shortcuts import render

# Create your views here.
from .models import T1
from django.db.models import Avg


def books_short(request):
    ###  从models取数据传给template  ###
    # shorts = T1.objects.all()
    shorts = T1.objects.filter(n_star__gt=3)
    # 评论数量
    # counter = T1.objects.all().count()
    counter = shorts.count()
    # 平均星级
    # star_value = T1.objects.values('n_star')
    # star_avg = f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    star_avg = f" {shorts.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    sent_avg = f" {shorts.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = shorts.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = shorts.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())
