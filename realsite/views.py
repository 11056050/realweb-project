from django.shortcuts import render, redirect, get_object_or_404
from realsite.models import Book,Comment
from django.contrib.auth.decorators import login_required
from .forms import BookForm, RegistrationForm, PostSearchForm, UserProfileForm,BookReleaseForm,CommentForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from .models import Writer, Chapter, UserProfile
from datetime import datetime
from django.contrib.auth import logout
from .forms import BookEditForm  

@login_required
def edit_user_added_books(request):
    user = request.user
    user_added_books = Book.objects.filter(added_by=user)

    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        try:
            book = Book.objects.get(id=book_id, added_by=user)
        except Book.DoesNotExist:
            print(f"Book with ID {book_id} does not exist or doesn't belong to the current user.")
            pass

        if book:
            book_form = BookEditForm(request.POST, instance=book)
            if book_form.is_valid():
              
                book_form.save()
                return redirect('edit_user_added_books')
    else:
       
        book_form = BookEditForm()

    context = {
        'user_added_books': user_added_books,
        'book_form': book_form,
    }

    return render(request, 'edit_user_added_books.html', context)




def edit_comment(request, book_id, comment_id):
    book = get_object_or_404(Book, id=book_id)
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'form': form, 'book': book, 'comment': comment})


def renting_history(request):
 
    rented_books = Book.objects.filter(rented_by=request.user)

   
    return render(request, 'renting_history.html', {'rented_books': rented_books})

def user_logout(request):
    logout(request)
    return redirect('homepage')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



@login_required
def rent_or_return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'rent' and book.available_copies > 0:
            book.available_copies -= 1
            book.rented_by.add(request.user)
            book.save()

        elif action == 'return' and request.user in book.rented_by.all():
            book.available_copies += 1
            book.rented_by.remove(request.user)
            book.save()

       
        return redirect('homepage')

    else:
        
        return render(request, 'rent_return_book.html', {'book': book})


@login_required
def rent_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'rent' and book.available_copies > 0:
            book.available_copies -= 1  
            book.rented_by.add(request.user)  
            book.save()

    return redirect('homepage')

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    renters = book.rented_by.all()  
    return render(request, 'book_detail.html', {'book': book, 'renters': renters})

def chapter_detail(request, book_id, chapter_id):
    chapter = get_object_or_404(Chapter, book_id=book_id, chapter_number=chapter_id)
    return render(request, 'chapter_detail.html', {'chapter': chapter})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    chapters = Chapter.objects.filter(book=book)
    return render(request, 'book_detail.html', {'book': book, 'chapters': chapters})

def writer_post(request, writer_id):
    writer = get_object_or_404(Writer, pk=writer_id)
    return render(request, 'writer_post.html', {'writer': writer})


def search_posts(request):
    form = PostSearchForm(request.GET)
    posts = Book.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        posts = posts.filter(Q(booktitle__icontains=search_query) | Q(info__icontains=search_query))

    return render(request, 'search_results.html', {'posts': posts, 'form': form})

@login_required
def edit_profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})

@login_required
def profile_view(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'user': request.user,
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)


@login_required
def profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})

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

@login_required
def release_book(request):
    if request.method == 'POST':
        form = BookReleaseForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.released_by = request.user
            book.save()
            return redirect('homepage')  
    else:
        form = BookReleaseForm()

    return render(request, 'createbook.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})