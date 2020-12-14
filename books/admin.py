from django.contrib import admin

# Register your models here.
from .models import Genre, Book, Author



class AuthorInline(admin.TabularInline):
	model = Author
	extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('name', 'author', 'started_date', 'finished_date')
	list_display_links = ('name', 'author')
	list_filter = ('author', 'genre')
	save_on_top = True
	search_fields = ('name', 'author__name')
	save_as = True
	fieldsets = (
		(None, {
			"fields": (('name', 'author'), )
			}),
		(None, {
			"fields": (("country", "genre"), )
			}),
		(None, {
			"fields": (("started_date", "finished_date"), )
			}),
		(None, {
			"fields": (("quote_image", ), )
			}))

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ('name', )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'was_born')

	save_on_top = True






