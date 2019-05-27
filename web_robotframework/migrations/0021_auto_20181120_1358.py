# Generated by Django 2.1.1 on 2018-11-20 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_robotframework', '0020_auto_20181120_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit_case_step',
            name='webcase',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web_robotframework.add_web_steps'),
        ),
        migrations.AlterField(
            model_name='edit_case_step',
            name='webcasename',
            field=models.CharField(default=1, max_length=200, verbose_name='测试标题'),
        ),
    ]