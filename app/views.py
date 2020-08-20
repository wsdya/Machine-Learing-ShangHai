import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets

from app.models import Typs_List, Obj_List, Article_List
from app.serilazer import Typs_List_Serilazer


def Typs_List_View(request):
    if request.method == 'GET':
        title = '首页'
        types = Typs_List.objects.all()
        type_list = []
        for i in types:
            all_munb = Obj_List.objects.filter(type=i.id).count()
            like_numb = i.like_numb
            read_numb = i.read_numb
            #  [颜色随机id，type_id，标题，子类别数量，有用数量，阅读数量]
            type_list.append(
                {
                    'color': i.id if i.id < 9 else i.id - ((i.id // 8) * 8),
                    'type_id': i.id,
                    'title': i.tname,
                    "all_munb": all_munb,
                    "like_numb": like_numb,
                    "read_numb": read_numb,
                }
            )

        return render(request, 'index.html', context=locals())


def get_type(request, id):
    if request.method == 'GET':
        type_list = Typs_List.objects.get(pk=id)
        type_list.read_numb += 1
        type_list.save()
        title = type_list.tname
        type_list = []
        # 取置顶子栏目
        types = Obj_List.objects.filter(type=id, is_top=True, is_delect=False)
        for i in types:
            all_munb = Article_List.objects.filter(obj=i.id).count()
            like_numb = i.like_numb
            read_numb = i.read_numb
            #  [颜色随机id，type_id，标题，子类别数量，有用数量，阅读数量]
            type_list.append(
                {
                    'color': i.id if i.id < 9 else i.id - ((i.id // 8) * 8),
                    'type_id': 'list/' + str(i.id),
                    'title': '[·置顶·]' + i.tname,
                    "all_munb": all_munb,
                    "like_numb": like_numb,
                    "read_numb": read_numb,
                }
            )

        types = Obj_List.objects.filter(type=id, is_top=False, is_delect=False).order_by('-id')

        for i in types:
            all_munb = Article_List.objects.filter(obj=i.id).count()
            like_numb = i.like_numb
            read_numb = i.read_numb
            #  [颜色随机id，type_id，标题，子类别数量，有用数量，阅读数量]
            type_list.append(
                {
                    'color': i.id if i.id < 9 else i.id - ((i.id // 8) * 8),
                    'type_id': 'list/' + str(i.id),
                    'title': i.tname,
                    "all_munb": all_munb,
                    "like_numb": like_numb,
                    "read_numb": read_numb,
                }
            )

        return render(request, 'index.html', context=locals())


def get_info(request, id):
    if request.method == 'GET':
        type_list = Obj_List.objects.get(pk=id)
        type_list.read_numb += 1
        type_list.save()
        type_list = []
        types = Article_List.objects.filter(obj=id)
        for i in types:
            like_numb = i.like_numb
            read_numb = i.read_numb
            print(i.add_time)
            #  [颜色随机id，type_id，标题，子类别数量，有用数量，阅读数量]
            type_list.append(
                {
                    'color': i.id if i.id < 9 else i.id - ((i.id // 8) * 8),
                    'title': i.title,
                    'url': i.url,
                    "like_numb": like_numb,
                    "read_numb": read_numb,
                    'time': i.add_time,
                }
            )

        return render(request, 'info.html', context=locals())
