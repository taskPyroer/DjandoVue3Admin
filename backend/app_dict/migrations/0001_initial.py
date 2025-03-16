# Generated by Django 4.2.1 on 2024-01-13 15:08

from django.db import migrations, models
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DictData',
            fields=[
                ('id', utils.models.SnowflakeIDField(primary_key=True, serialize=False)),
                ('modifier', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('update_datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('sort', models.IntegerField(default=1, help_text='字典顺序', verbose_name='字典顺序')),
                ('dict_label', models.CharField(help_text='字典标签', max_length=64, verbose_name='字典标签')),
                ('dict_value', models.CharField(help_text='字典数值', max_length=64, verbose_name='字典数值')),
                ('dict_type', models.CharField(help_text='类型', max_length=64, verbose_name='类型')),
                ('status', models.CharField(choices=[('0', '正常'), ('1', '停用')], default='0', help_text='字典状态（0正常 1停用）', max_length=1, verbose_name='字典状态（0正常 1停用）')),
                ('remark', models.CharField(blank=True, help_text='备注', max_length=150, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '系统-字典数值',
                'verbose_name_plural': '系统-字典数值',
                'db_table': 'sys_dict_data',
                'ordering': ('sort', '-create_datetime'),
            },
        ),
        migrations.CreateModel(
            name='DictType',
            fields=[
                ('id', utils.models.SnowflakeIDField(primary_key=True, serialize=False)),
                ('modifier', models.CharField(blank=True, help_text='修改人', max_length=255, null=True, verbose_name='修改人')),
                ('update_datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('dict_name', models.CharField(help_text='字典名称', max_length=64, unique=True, verbose_name='字典名称')),
                ('dict_type', models.CharField(help_text='类型', max_length=64, unique=True, verbose_name='类型')),
                ('status', models.CharField(choices=[('0', '正常'), ('1', '停用')], default='0', help_text='字典状态（0正常 1停用）', max_length=1, verbose_name='字典状态（0正常 1停用）')),
                ('remark', models.CharField(blank=True, help_text='备注', max_length=150, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '系统-字典类型',
                'verbose_name_plural': '系统-字典类型',
                'db_table': 'sys_dict_type',
                'ordering': ('-create_datetime',),
            },
        ),
    ]
