from django.contrib import admin
from lib.models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'author', 'pub_house', 'pub_date')
    #ordering = ('no')
    #search_fields('name', 'author')


admin.site.register(Book, BookAdmin)
