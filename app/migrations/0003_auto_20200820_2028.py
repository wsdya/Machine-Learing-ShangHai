# Generated by Django 2.2.14 on 2020-08-20 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200820_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='typs_list',
            name='like_numb',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='typs_list',
            name='read_numb',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Obj_List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oname', models.CharField(max_length=12, verbose_name='子栏目分类名')),
                ('like_numb', models.IntegerField(default=0)),
                ('read_numb', models.IntegerField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Typs_List')),
            ],
            options={
                'db_table': 'Obj_List',
            },
        ),
    ]
