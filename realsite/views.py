from django.shortcuts import render, redirect
from realsite.models import Book
from django.http import HttpResponse
from datetime import datetime
from .forms import PostSearchForm
from django.db.models import Q
from .forms import BookForm
from django.shortcuts import render, get_object_or_404
from .models import Writer
from .models import Chapter

def rent_book(request, book_id):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, id=book_id)
        book.rented_by = request.user
        book.save()
        
        return HttpResponse("Book has been marked as rented.")
    else:
        return HttpResponse("You must be logged in to mark a book as rented.")

def rent_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    button_value = request.POST.get('action')

    if button_value == 'rented':
        book.status = 'Rented'
    elif button_value == 'not_rented':
        book.status = 'Not Rented'

    book.save()

    return HttpResponse("Book status updated.")

def chapter_detail(request, book_id, chapter_id):
    chapter = get_object_or_404(Chapter, book_id=book_id, chapter_number=chapter_id)
    return render(request, 'chapter_detail.html', {'chapter': chapter})

def book_list(request, book_id):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    chapters = Chapter.objects.filter(book=book)
    return render(request, 'book_detail.html', {'book': book, 'chapters': chapters})

def writer_post(request, writer_id):
    writer = get_object_or_404(Writer, pk=writer_id)
    return render(request, 'writer_post.html', {'writer': writer})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

def search_posts(request):
    form = PostSearchForm(request.GET)
    posts = Book.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        posts = posts.filter(Q(booktitle__icontains=search_query) | Q(info__icontains=search_query))

    return render(request, 'search_results.html', {'posts': posts, 'form': form})

def homepage(request):
    posts = Book.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showbook(request, book_name=None):
    if book_name:
        try:
            book = Book.objects.get(booktitle=book_name)
            return render(request, 'post.html', {'book': book})
        except Book.DoesNotExist:
            return redirect("/")
    else:
        return render(request, 'general_book.html')