from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from lib.models import Book
# Create your views here.


def detail(request):
    book_list = Book.objects.order_by('no')[:10]
    context = {'book_list': book_list}
    return render(request, 'detail.html', context)


def addBook(request):
    if request.method == 'POST':
        temp_no = request.POST['no']
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']

    from django.utils import timezone
    temp_book = Book(no=temp_no, name=temp_name, author=temp_author,
                     pub_house=temp_pub_house, pub_date=timezone.now())
    temp_book.save()

    # 重定向
    return HttpResponseRedirect(reverse('lib:detail'))


def deleteBook(request, book_no):
    bookID = book_no
    Book.objects.filter(no=bookID).delete()
    return HttpResponseRedirect(reverse('lib:detail'))
