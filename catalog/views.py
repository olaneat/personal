from django.shortcuts import render
from .models import Book, BookInstance, Author, Language, Genre
# Create your views here.


def index(request):
	"view function for the home page"

	num_book = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	#num_instances_available = BookInstance.objects.filter(status_exact = 'A').count()
	num_author = Author.objects.count()

	return render(
		request,
		'index.html',
		context = {'num_book': num_book, 'num_instances':num_instances, 'num_author': num_author,} # 'num_instance_available':num_instance_available, },
		)