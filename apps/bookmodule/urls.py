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

    path('lab9/task1/', views.l9Task1, name='books.l9Task1'),
    path('lab9/task2/', views.l9Task2, name='books.l9Task2'),
    path('lab9/task3/', views.l9Task3, name='books.l9Task3'),
    path('lab9/task4/', views.l9Task4, name='books.l9Task4'),
    path('lab9/task5/', views.l9Task5, name='books.l9Task5'),
    path('lab9/task6/', views.l9Task6, name='books.l9Task6'),

    path('lab10_part1/listbooks/', views.l10Part1ListBooks, name='books.l10Part1ListBooks'),
    path('lab10_part1/addbook/', views.l10Part1AddBook, name='books.l10P1AddBook'),
    path('lab10_part1/eiditbook/<int:bookId>/', views.l10Part1EditBook, name='books.l10P1EditBook'),
    path('lab10_part1/deletebook/<int:bookId>/', views.l10P1DeleteBook, name='books.l10P1DeleteBook'),

    path('lab10_part2/listbooks/', views.l10Part2ListBooks, name='books.l10Part2ListBooks'),
    path('lab10_part2/addbook/', views.l10Part2AddBook, name='books.l10P2AddBook'),
    path('lab10_part2/eiditbook/<int:bookId>/', views.l10Part2EditBook, name='books.l10P2EditBook'),
    path('lab10_part2/deletebook/<int:bookId>/', views.l10P2DeleteBook, name='books.l10P2DeleteBook'),

    path('lab11/add_student', views.lab11_addStudent, name='lab11_addStudent'),
    path('lab11/list_students', views.lab11_list_students, name='lab11_list_students'),
    path('lab11/update_student/<int:id>', views.lab11_update_student, name='lab11_update_student'),
    path('lab11/delete_student/<int:id>', views.lab11_delete_student, name='lab11_delete_student'),

    path('lab11/task2_list', views.lab11_task2_list, name='lab11_task2_list'),
    path('lab11/task2_add', views.lab11_task2_add_student, name='lab11_task2_add'),

    path('lab11/upload_photo', views.lab11_upload_photo, name='lab11_upload_photo'),
]
