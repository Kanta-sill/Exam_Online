# Generated by Django 3.1 on 2021-01-10 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_auto_20210110_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='c_ans',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='d_ans',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
