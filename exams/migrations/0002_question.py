# Generated by Django 3.1 on 2021-01-10 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=50)),
                ('correct_ans', models.CharField(max_length=50)),
                ('a_ans', models.CharField(max_length=500)),
                ('b_ans', models.CharField(max_length=500)),
                ('c_ans', models.CharField(max_length=500)),
                ('d_ans', models.CharField(max_length=500)),
                ('mark', models.FloatField()),
                ('cate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.category')),
            ],
        ),
    ]