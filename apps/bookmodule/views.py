from urllib import request

from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book,Student, Address,Book1, Publisher, Author

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
