# Generated by Django 3.0.5 on 2020-04-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0002_auto_20200412_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=64, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=64, verbose_name='书籍'),
        ),
        migrations.AlterField(
            model_name='book',
            name='no',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='书籍编号'),
        ),
    ]
