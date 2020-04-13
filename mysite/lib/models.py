from django.db import models

# Create your models here.


class Book(models.Model):
    no = models.IntegerField(primary_key=True, verbose_name='书籍编号')
    name = models.CharField(max_length=64, verbose_name='书籍')
    author = models.CharField(max_length=64, verbose_name='作者')
    pub_house = models.CharField(max_length=100, verbose_name='出版社')
    pub_date = models.DateField(null=True, verbose_name='出版日期')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_book'
        verbose_name = '图书'
        verbose_name_plural = '图书'
