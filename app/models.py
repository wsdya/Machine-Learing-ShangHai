from django.db import models


# Create your models here.
class Typs_List(models.Model):
    #  初始化大的栏目，下一层是子目录
    tname = models.CharField(max_length=12, null=False, verbose_name='栏目分类名')
    like_numb = models.IntegerField(default=0)
    read_numb = models.IntegerField(default=0)

    class Meta:
        db_table = "Typs_List"


class Obj_List(models.Model):
    # 获取每个栏目的子栏目，下一层是文章的信息
    tname = models.CharField(max_length=12, null=False, verbose_name='子栏目分类名')
    type = models.ForeignKey(to=Typs_List, on_delete=models.CASCADE)
    is_top = models.BooleanField(default=False)
    is_delect = models.BooleanField(default=False)
    like_numb = models.IntegerField(default=0)
    read_numb = models.IntegerField(default=0)

    class Meta:
        db_table = "Obj_List"


class Article_List(models.Model):
    title = models.CharField(max_length=64, null=False, verbose_name='文章标题')
    url = models.CharField(max_length=512)
    obj = models.ForeignKey(to=Obj_List, on_delete=models.CASCADE)
    is_top = models.BooleanField(default=False)
    is_delect = models.BooleanField(default=False)
    add_time = models.DateTimeField(auto_now=True)
    like_numb = models.IntegerField(default=0)
    read_numb = models.IntegerField(default=0)

    class Meta:
        db_table = "Article_List"
