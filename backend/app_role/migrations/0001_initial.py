# Generated by Django 4.2.1 on 2024-01-13 15:08

from django.db import migrations, models
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', utils.models.SnowflakeIDField(primary_key=True, serialize=False)),
                ('modifier', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('update_datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('role_name', models.CharField(help_text='角色名称', max_length=64, verbose_name='角色名称')),
                ('role_key', models.CharField(help_text='角色代码', max_length=64, unique=True, verbose_name='角色代码')),
                ('status', models.CharField(choices=[('0', '正常'), ('1', '停用')], default='0', help_text='角色状态（0正常 1停用）', max_length=1, verbose_name='角色状态（0正常 1停用）')),
                ('sort', models.IntegerField(default=1, help_text='角色顺序', verbose_name='角色顺序')),
                ('admin', models.BooleanField(default=False, help_text='是否为admin', verbose_name='是否为admin')),
                ('data_scope', models.CharField(choices=[('1', '全部数据权限'), ('2', '自定数据权限'), ('3', '本部门数据权限'), ('4', '本部门及以下数据权限'), ('5', '仅本人数据权限')], default='5', help_text='数据权限范围', max_length=1, verbose_name='数据权限范围')),
                ('remark', models.CharField(blank=True, help_text='备注', max_length=128, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '系统-角色表',
                'verbose_name_plural': '系统-角色表',
                'db_table': 'sys_role',
                'ordering': ('sort',),
            },
        ),
    ]
