from django.contrib import admin
from realsite.models import Book
from realsite.models import Writer

class BookAdmin(admin.ModelAdmin):
    list_display = ('booktitle', 'picture', 'info', 'creator', 'pub_date', 'release')


class WriterAdmin(admin.ModelAdmin):
    list_display = ('image', 'age', 'gender', 'born_date')

admin.site.register(Writer, WriterAdmin)

admin.site.register(Book, BookAdmin)