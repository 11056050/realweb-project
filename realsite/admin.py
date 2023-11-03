from django.contrib import admin
from realsite.models import Book,Chapter
from realsite.models import Writer

class BookAdmin(admin.ModelAdmin):
    list_display = ('booktitle', 'picture', 'info', 'creator', 'pub_date', 'release')


class WriterAdmin(admin.ModelAdmin):
    list_display = ('image', 'age', 'gender', 'born_date', 'creatorname')

admin.site.register(Writer, WriterAdmin)

admin.site.register(Book, BookAdmin)
admin.site.register(Chapter)