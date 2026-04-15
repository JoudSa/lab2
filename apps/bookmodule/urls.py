from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),

    path('html5/links/', views.links_view, name="books.links"),
    path('html5/text/formatting/', views.formatting_view, name="books.formatting"),
    path('html5/listing/', views.listing_view, name="books.listing"),
    path('html5/tables/', views.tables_view, name="books.tables"),

    path('search/', views.searchView, name='searchView'),

    path('simple/query/', views.simple_query, name='books.simple_query'),
    path('complex/query/', views.complex_query, name='books.complex_query'),

    path('lab8/task1/', views.l8Task1, name='books.l8Task1'),
    path('lab8/task2/', views.l8Task2, name='books.l8Task2'),
    path('lab8/task3/', views.l8Task3, name='books.l8Task3'),
    path('lab8/task4/', views.l8Task4, name='books.l8Task4'),
    path('lab8/task5/', views.l8Task5, name='books.l8Task5'),
    path('lab8/task7/', views.l8Task7, name='books.l8Task7'),
]
