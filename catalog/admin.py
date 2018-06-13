from django.contrib import admin
from . models import Book, Author, BookInstance, Genre, Language
# Register your models here.

#admin.site.register(Book)
#admin.site.register(BookInstance)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(Language)


class BookInstanceInline(admin.TabularInline):
	model = BookInstance


@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
	list_filter = ('status', 'due_back')
	fieldsets = (
		(None, {
			'fields': ('book', 'imprint', 'id' )
			}),
		('availability',{
			'fields':('status','due_back')
			}),
		
		)


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('surname',  'first_name', 'DOB')
	fields = ['first_name', 'surname', ('DOB', 'DOD')]

admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BookInstanceInline]

#admin.site.register(Book, BookAdmin)



@admin.register(Language)
class Language(admin.ModelAdmin):
	pass