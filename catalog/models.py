from django.db import models
import uuid
from django.urls import reverse
# Create your models here.
class Genre(models.Model):
	"A model representing the Genre Object"
	name = models.CharField(max_length = 500, help_text = "kindly enter the genre the book belongs to e.g(scientific, Fiction or Drama) ")

	def __str__(self):
		"String for representing the Object in Admin View page "
		return self.name

class Book(models.Model):
	"Model representing the book Object"
	title = models.CharField(max_length = 200)
	author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)
	summary = models.CharField(max_length = 500, help_text = 'enter a brief summary of the book')
	isbn = models.CharField(max_length = 14, help_text = '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(Genre, help_text = 'enter the book genre here ')

	def display_genre(self):
	
		return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
	display_genre.short_description = 'Genre'

	def __str__(self):
		"String representing the Book model"
		return self.title

	def get_absolute_url(self):
		"returns the url to access a particular book"
		return reverse('book-detail', args = [str(self.id)])

class Author(models.Model):
	"Model representing the Author model "
	first_name = models.CharField(max_length = 100 )
	surname = models.CharField(max_length = 100)
	DOB = models.DateField(null = True, blank = True)
	DOD = models.DateField('Died', null = True, blank = True)

	class Meta:
		ordering = ['first_name', 'surname']	

	def __str__(self):
		"String representing the Author details"

		return '{0}, {1}'.format(self.first_name, self.surname)

	def get_absolute_url(self):
		"returns the urls contianing the profile of the Author"

		return reverse('author-detail', args = [String(self.id)])


class BookInstance(models.Model):
	imprint = models.CharField(max_length = 300)
	id = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'unique Id to indetify the book')
	book = models.ForeignKey('Book', on_delete = models.SET_NULL, null = True)	
	due_back = models.DateField(null = True, blank = True)

	Loan_Status = ((
		'R', 'Reversed'),
		('A', 'Available'),
		('M', 'Maintanance'),
		('N', 'Not Available')
		)
	status = models.CharField(max_length = 2, choices = Loan_Status, default = 'A', help_text = 'Book Availability', blank = True)

#	class Meta:
#		ordering = ['due_back']

	def __str__(self):
		return '{0} ({1})'.format(self.id, self.book.title)


class Language(models.Model):
	Language_used = (
		('E', 'English'),
		('F', 'French'),
		('C', 'Chinese'),
		('F2', 'Farsi'),
		)
	book_dialect = models.ForeignKey('Book', on_delete = models.SET_NULL, null = True)
	Language_dialect = models.CharField(max_length = 2, default = 'E', choices = Language_used )

	def __str__(self):
		return self.book_dialect