from django.contrib import admin
from django.urls import path
from realsite import views as mv
from django.conf import settings
from django.conf.urls.static import static
from realsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mv.homepage, name="homepage"),
    path('book/<str:book_name>/', mv.showbook, name='book_detail'),
    path('search/', mv.search_posts, name='search_posts'), 
    path('writer/<int:writer_id>/', views.writer_post, name='writer_post'),
    path('book/<int:book_id>/chapter/<int:chapter_id>/', mv.chapter_detail, name='chapter_detail'),
    path('book/<int:book_id>/rent/', mv.rent_book, name='rent_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)