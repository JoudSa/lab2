from urllib import request

from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book,Student, Address,Book1, Publisher, Author, Student2,Address2, NaturePhoto
from .forms import BookForm, StudentForm, Student2Form, NaturePhotoForm


def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)

#def index(request):
   #return HttpResponse("Hello, world!")
   #return HttpResponse("Hello, "+name)
   #name = request.GET.get("name") or "world!"
   #return render(request, "bookmodule/index.html",{"name": name})    

def index2(request, val1 = 0):   #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))
 
def index(request):
    mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)
    mybook.save() 
    return render(request, "bookmodule/index.html", {"book": mybook})
 
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')


def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
 

def links_view(request):
    return render(request, 'bookmodule/links.html')

def formatting_view(request):
    return render(request, 'bookmodule/text_formatting.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')

def searchView(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def l8Task1(request):
    myBook = Book.objects.filter(Q(price__lte = 80))
    return render(request, 'bookmodule/l8Task1.html', {'books': myBook})

def l8Task2(request):
    query = Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    myBooks = Book.objects.filter(query)
    return render(request, 'bookmodule/l8Task2.html', {'books': myBooks})

def l8Task3(request):
    query = ~Q(edition__gt=3) & (~Q(title__icontains='qu') | ~Q(author__icontains='qu'))
    myBooks = Book.objects.filter(query)
    return render(request, 'bookmodule/l8Task3.html', {'books': myBooks})

def l8Task4(request):
    myBooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/l8Task4.html', {'books': myBooks})

def l8Task5(request):
    stats = Book.objects.aggregate(
        totalBooks=Count('id'),
        totalPrice=Sum('price'),
        avgPrice=Avg('price'),
        maxPrice=Max('price'),
        minPrice=Min('price')
    )
    return render(request, 'bookmodule/l8Task5.html', {'stats': stats})

def l8Task7(request):
    city = Address.objects.annotate(stdNum=Count('student'))
    return render(request, 'bookmodule/l8Task7.html', {'cities': city})

def l9Task1(request):
    total_stock = Book1.objects.aggregate(Sum('quantity'))['quantity__sum']
    
    books = Book1.objects.all()
    
    for b in books:
        if total_stock > 0:
            b.availability = (b.quantity / total_stock) * 100
        else:
            b.availability = 0

    return render(request, 'bookmodule/lab9Task1.html', {'books': books})

def l9Task2(request):
    publishers = Publisher.objects.annotate(book_count=Count('book1'))
    return render(request, 'bookmodule/lab9Task2.html', {'publishers': publishers})

def l9Task3(request): 
    publishers = Publisher.objects.annotate(firstBook=Min('book1__pubdate')).filter(book1__pubdate__isnull=False)
    return render(request, 'bookmodule/lab9Task3.html', {'publishers': publishers})

def l9Task4(request):
    stats = Publisher.objects.annotate( 
        avgPrice=Avg('book1__price'),
        maxPrice=Max('book1__price'),
        minPrice=Min('book1__price')).filter(book1__price__isnull=False)
    
    return render(request, 'bookmodule/lab9Task4.html', {'stats': stats})

def l9Task5(request):
    publishers = Publisher.objects.filter(book1__rating__gte=4).annotate(book_count=Count('book1'),total_quantity=Sum('book1__quantity'))
    return render(request, 'bookmodule/lab9Task5.html', {'publishers': publishers})

def l9Task6(request):
    publishers = Publisher.objects.filter(Q(book1__price__gt=50)&Q(book1__quantity__lt=5)&Q(book1__quantity__gte=1)).annotate(book_count=Count('book1'))
    return render(request, 'bookmodule/lab9Task6.html', {'publishers': publishers})


def l10Part1ListBooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/l10P1ListBooks.html', {'books': books})

def l10Part1AddBook(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = float(request.POST.get('price'))
        author = int(request.POST.get('author')) 
        edition = int(request.POST.get('edition'))       
        new_book = Book(title=title, price=price, author=author, edition=edition)
        new_book.save()
        
        return render(request, 'bookmodule/l10P1AddBook.html', {'message': 'Book added successfully!'})
    
    return render(request, 'bookmodule/l10P1AddBook.html')

def l10Part1EditBook(request, bookId):
    book = Book.objects.get(id=bookId)
    
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.price = float(request.POST.get('price'))
        book.author = int(request.POST.get('author')) 
        book.edition = int(request.POST.get('edition'))       
        book.save()
        
        return render(request, 'bookmodule/l10P1EditBook.html', {'book': book, 'message': 'Book updated successfully!'})
    
    return render(request, 'bookmodule/l10P1EditBook.html', {'book': book})

def l10P1DeleteBook(request, bookId):
    book = Book.objects.get(id=bookId)
    
    if request.method == "POST":
        book.delete()
        return render(request, 'bookmodule/l10P1DeleteBook.html', {'message': 'Book deleted successfully!'})
    
    return render(request, 'bookmodule/l10P1DeleteBook.html', {'book': book})

def l10Part2ListBooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/l10P2ListBooks.html', {'books': books})

def l10Part2AddBook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('books.l10Part2ListBooks')
    else:
        form = BookForm()
    
    return render(request, 'bookmodule/l10Part2AddBook.html', {'form': form}) 

def l10Part2EditBook(request, bookId):
    book = Book.objects.get(id=bookId)
    
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.l10Part2ListBooks')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'bookmodule/l10Part2EditBook.html', {'form': form, 'book': book})

def l10P2DeleteBook(request, bookId):
    book = Book.objects.get(id=bookId)
    
    if request.method == "POST":
        book.delete()
        return redirect('books.l10Part2ListBooks')
    
    return render(request, 'bookmodule/l10Part2DeleteBook.html', {'book': book})   

def lab11_addStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab11_addStudent')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/lab11StudentForm.html', {'form': form})
def lab11_list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/lab11_list_students.html', {'students': students})

def lab11_update_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('lab11_list_students')
    else:
        form = StudentForm(instance=student)
        
    return render(request, 'bookmodule/lab11StudentForm.html', {'form': form})

def lab11_delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('lab11_list_students')


def lab11_task2_add_student(request):
    if request.method == 'POST':
        form = Student2Form(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('lab11_task2_list')
    else:
        form = Student2Form() 
    return render(request, 'bookmodule/lab11_student2_form.html', {'form': form})

def lab11_task2_list(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/lab11_task2_list.html', {'students': students})

from .forms import NaturePhotoForm

def lab11_upload_photo(request):
    if request.method == 'POST':
        form = NaturePhotoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('lab11_gallery')
    else:
        form = NaturePhotoForm()
    return render(request, 'bookmodule/lab11_upload_form.html', {'form': form})


def lab11_upload_photo(request):
    if request.method == 'POST':
        form = NaturePhotoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('lab11_gallery')
    else:
        form = NaturePhotoForm()
    return render(request, 'bookmodule/lab11_upload_form.html', {'form': form})

def lab11_gallery(request):
    photos = NaturePhoto.objects.all()
    return render(request, 'bookmodule/lab11_gallery.html', {'photos': photos})