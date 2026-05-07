from django import forms
from .models import Book, NaturePhoto, Student, Address, Student2, Address2

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'addresses']
        widgets = {'addresses': forms.CheckboxSelectMultiple(), }

class NaturePhotoForm(forms.ModelForm):
    class Meta:
        model = NaturePhoto
        fields = ['title', 'image']