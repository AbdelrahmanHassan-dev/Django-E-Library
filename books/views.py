from django.shortcuts import render,redirect, get_object_or_404
from .models import Author, Book, Category
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
from .models import Favoritebooks,Book




def author_details(request,author_id):

    return render(request,'books/author_details.html',{'author_details':Author.objects.get(id=author_id)})

def authors_list(request):
    return render(request,'books/authors_list.html',{'authors':Author.objects.all()})


def book_details(request, book_id):
    return render(request,'books/book_details.html',{'book':Book.objects.get(id = book_id)})


# def books_list(request):
#    # return render(request,'books/books_list.html',{'books':Book.objects.all()})
    # if request.method=="GET":
    #     sort = request.GET.get('sort')
    # the_sort='-spread_date'
    # if sort == 'lastest':
    #     the_sort = 'spread_date'
    # return render(request,'books/books_list.html',{'books':Book.objects.order_by(the_sort)})
def books_list(request):
    sort = request.GET.get('sort', 'oldest')
    
    if sort == 'latest':
        the_sort = '-spread_date'
    else:
        the_sort = 'spread_date'
    
    return render(request, 'books/books_list.html', {
        'books': Book.objects.order_by(the_sort),
        'current_sort': sort
    })


def categories_list(request):
    return render(request,'books/category_list.html',{'categorys':Category.objects.all()})



# user = get_user_model
@login_required
def favorite_books(request):
    user = request.user
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        book = Book.objects.get(id=book_id)
        add = Favoritebooks(user=user , favorite_books=book)
        add.save()
        return redirect('book_details', book_id=book.id)

    return redirect('books_list')



@login_required
@permission_required('books.can_mark_featured',raise_exception=True)
def mark_featured(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        book = Book.objects.get(id=book_id)
        book.is_featured = True 
        book.save()
        return redirect('book_details',book_id=book.id)
    return redirect('books_list')


    