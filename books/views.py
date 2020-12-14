from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from books.models import Book 

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .tesseract import image_to_text
import pytesseract
from PIL import Image
from pytesseract import image_to_string
from django.conf import settings
import time
from .tasks import quote_text


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different

def index(request):
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits+1
	return render(request, 'books/base.html', context={'num_visits':num_visits})


class BookListView(LoginRequiredMixin, ListView):
	model = Book
	queryset = Book.objects.all()
	template_name = 'books/book_list.html'
	paginate_by = 10
	
	def get_queryset(self):
		return Book.objects.filter(borrower=self.request.user)


class BookDetailView(LoginRequiredMixin, DetailView):
	model = Book
	template_name = 'books/book_detail.html'

	

	"""def quotes_image_text(request, pk):
					quote_img = Book.objects.get(pk=pk)
					quote = image_to_string(Image(settings.MEDIA_URL + '/' + quote_img.quote_image))
					return render(request, 'books/book_detail.html', context={'quote':quote})"""

def book_detail_view(request, pk):

	try:
		start_time = time.time()
		book_id = Book.objects.get(pk=pk)

								#quote = settings.MEDIA_URL + str(quote_img.quote_image)
		url = 'D:/DJANGOPROJECTS/Books/booksite/media/'
		quote = quote_text.delay(url + str(book_id.quote_image))
		actual_time = time.time() - start_time
	except:
		Http404("Book doesn't exist")
		
	return render(request, 'books/book_detail.html', context={'lol':book_id, 'quote_txt':quote, 'time':actual_time})

class BookCreateView(CreateView):
	model = Book
	fields = ('name', 'author', 'genre', 'country', 'started_date', 'finished_date', 'review', 'image')



class BookUpdateView(UpdateView):
	model = Book
	fields = ('name', 'author', 'genre', 'country', 'started_date', 'finished_date', 'review', 'image')

class BookDeleteView(DeleteView):
	model = Book

class AllBooksListView(ListView):
	model = Book
	template_name = 'books/all_books_list.html'
	context_object_name = 'all_books_list'


class Search(ListView):
	model = Book

	def get_queryset(self):
		return Book.objects.filter(name__icontains=self.request.GET.get("q"))

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context["q"] = self.request.GET.get("q")
		return context

