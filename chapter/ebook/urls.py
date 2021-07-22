from django.urls import path
from ebook import views
urlpatterns = [
    
    path('',views.genre,name='genre'),
    path('ebook/<int:id>',views.category_book,name='detail'),
    path('search',views.search,name='search'),
]

