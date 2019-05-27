# Generated by Django 2.1.1 on 2018-12-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcasestep',
            name='webassertdata',
            field=models.CharField(blank=True, max_length=200, verbose_name='验证数据'),
        ),
        migrations.AlterField(
            model_name='webcasestep',
            name='webcomments',
            field=models.CharField(blank=True, max_length=200, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='webcasestep',
            name='webfindmethod',
            field=models.CharField(blank=True, max_length=200, verbose_name='方法|操作'),
        ),
        migrations.AlterField(
            model_name='webcasestep',
            name='webkwargesone',
            field=models.CharField(blank=True, max_length=200, verbose_name='参数1'),
        ),
        migrations.AlterField(
            model_name='webcasestep',
            name='webkwargesthree',
            field=models.CharField(blank=True, max_length=200, verbose_name='参数3'),
        ),
        migrations.AlterField(
            model_name='webcasestep',
            name='webkwargestwo',
            field=models.CharField(blank=True, max_length=200, verbose_name='参数2'),
        ),
        migrations.AlterField(
            model_name='webcasestep',
            name='webtestresult',
            field=models.CharField(blank=True, max_length=50, verbose_name='测试结果'),
        ),
    ]