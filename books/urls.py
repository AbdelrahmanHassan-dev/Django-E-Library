from django.urls import path
from . import views
urlpatterns = [
    path('author_details/<int:author_id>/',views.author_details, name ='author_details'),
    path('authors_list/',views.authors_list, name ='authors_list'),
    path('book_details/<int:book_id>/',views.book_details, name ='book_details'),
    path('favorite/', views.favorite_books, name='favorite_books'),
    path('books_list/',views.books_list, name ='books_list'),
    path('category_list/',views.categories_list,name='category_list'),
    path('feature/',views.mark_featured,name='mark_featured')
]
