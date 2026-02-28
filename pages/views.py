from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .forms import Contact_us
from books.models import Book,Category,Author,Favoritebooks
from django.db.models import Q
from .forms import Signup
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
def about(request):
    return render(request,'pages/about.html')

def contact(request):

    if request.method=="POST":
        form = Contact_us(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إرسال رسالتك بنجاح، شكراً!')
            return redirect('contact')
    return render(request,'pages/contact.html', {'contact':Contact_us})


def base(request):
    return render(request,'base.html')

def home(request):
    books = Book.objects.all()[:6]
    category = Category.objects.all()
    author = Author.objects.all()



    return render(request,'pages/home.html',{'books':books, 'category': category, 'author':author})


def search(request):
    if request.method == "GET":
        search_query = request.GET.get('book',None)
        if search_query == None:
            return render(request, 'pages/search.html',{'query':search_query,'books':None})

        book = Book.objects.filter(Q(title__icontains=search_query)|Q(autor__name__icontains=search_query)|Q(category__title__icontains=search_query)).distinct()
        if book:
            return render(request, 'pages/search.html',{'query':search_query,'books':book})
        return render(request, 'pages/search.html',{'query':search_query,'books':None})

    else:
        return render(request, 'pages/search.html',{'query':search_query,'books':None})

# def search(request):
#     if request.method == "GET":
#         search_query = request.GET.get('book')
#         if search_query:
#             book = Book.objects.filter(title__icontains=search_query)
#             if book :
#                 return render(request, 'pages/search.html',{'query':search_query,'book':book})
#             else:
#                 return render(request, 'pages/search.html',{'book':'None'})
#         else:
#             return render(request, 'pages/search.html',{'book':'None'})

#     else:
#         return render(request, 'pages/search.html',{'book':'None'})




def signup(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form= Signup()
    return render(request, 'pages/signup.html',{'form':form})

#that is the first tried I don't know what is the reason that make me made that
# @login_required
# def profile(request,id):
#     user = user.objects.get(id=id)
    
#     if request.user == user:
#         return HttpResponseForbidden("you can't get here")
#     return render(request,'pages/profile.html',{'user':user})




# @login_required
# def profile(request):
#     # book = Book.objects.get(is_featured=True)
#     books = Book.objects.all()
#     books_featured = []
#     for book in books:
#         if book.is_featured:
#             books_featured.append(book)

#     user = request.user
#     favoritebooks = Favoritebooks.objects.all


#     return render(request,'pages/profile.html',{'user':request.user,'book_featured':books_featured,'favoritebooks':favoritebooks})




@login_required
def profile(request):
    # book = Book.objects.get(is_featured=True)
    books = Book.objects.all()
    books_featured = []
    for book in books:
        if book.is_featured:
            books_featured.append(book)

    user = request.user
    # favoritebooks = Favoritebooks.objects.all()
    # favorite_books =[]
    # if user == favoritebooks.user:
    #     favorite_books.append(favoritebooks)

    user_favorites= Favoritebooks.objects.filter(user=request.user)
    # if not favorite_books :
    #     favorite_books.append("Unfortunatly you don't have favorite books")
    return render(request,'pages/profile.html',{'user':request.user,'book_featured':books_featured,'favorite_books':user_favorites})




