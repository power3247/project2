# Generated by Django 3.2.6 on 2021-08-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('제목', models.TextField()),
                ('점수', models.IntegerField()),
                ('질문', models.TextField()),
                ('답변', models.TextField()),
            ],
        ),
    ]
