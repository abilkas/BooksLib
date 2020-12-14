from django.urls import path, include
from books.views import BookListView, Search, AllBooksListView, BookUpdateView, BookDetailView, index, BookCreateView, book_detail_view

urlpatterns = [
	path('', index, name='base'),
	path('search/', Search.as_view(), name='search'),
	path('books/', BookListView.as_view(), name='booklist'),
	path('books/<pk>', book_detail_view, name='bookdetail'),
	path('create', BookCreateView.as_view(), name='bookcreate'),
	path('update/<int:pk>', BookUpdateView.as_view(), name='bookupdate'),
	path('allbooks/', AllBooksListView.as_view(), name='allbookslist'),
]

