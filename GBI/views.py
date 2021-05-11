from tkinter import EXCEPTION

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import requests

from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm



# Create your views here.
def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    url = 'https://www.googleapis.com/books/v1/volumes?q={}&key=AIzaSyC-2WYcaCeJ0N54v3yQTtw0ITo1koCllcM'
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

    form = BookForm()
    books = Book.objects.all()

    book_data = []
    try:
        for book in books:
            r = requests.get(url.format(book)).json()
            book_Api = {
                'id': book.id,
                'title': r['items'][0]['volumeInfo']['title'],
                'publishdate': r['items'][0]['volumeInfo']['publishedDate'],
                'description': r['items'][0]['volumeInfo']['description'],
                'icon': r['items'][0]['volumeInfo']['imageLinks']['thumbnail'],
                'infoLink': r['items'][0]['volumeInfo']['infoLink'],
             }

            book_data.append(book_Api)

    except KeyError:
        Book.objects.filter(name=book.name).delete()
        pass

    except EXCEPTION as e:
        pass
    context = {'book_data': book_data, 'form': form}

    return render(request, 'dashboard.html', context)



def delete(request, id):
    if request.method == 'POST':
        Book.objects.filter(id=id).delete()

    return redirect('/dashboard/')


def registerView(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
            form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})

