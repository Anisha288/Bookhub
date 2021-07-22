from django.shortcuts import render,redirect,HttpResponse
from ebook.forms import BookForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ebook.models import Category,Book
   


   
def genre(request):
    object_list = Category.objects.all()
    context = {
        
        "object_list" : object_list
    }
    
    return render(request,'ebook/genre.html',context)


def category_book(request,id):
    if not request.user.is_authenticated:

        form = AuthenticationForm()

        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    object_search = Book.objects.filter(category=id)
                    return render(request, 'ebook/category_book.html', context={'object_search':object_search})

        return render(request,'app_authenticate/login.html', context={'form':form})
    else:   
            object_search = Book.objects.filter(category=id)
    return render(request, 'ebook/category_book.html', context={'object_search':object_search})


def search(request):
    if not request.user.is_authenticated:

        form = AuthenticationForm()

        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)
                    #object_search = Book.objects.filter(category=id)
                    query=request.GET['query']
                    object_searchBookname = Book.objects.filter(bookname__icontains=query)
                    object_searchAuthor = Book.objects.filter(author__icontains=query)
                    object_search = object_searchBookname.union(object_searchAuthor)
                    params={'object_search':object_search, 'query':query}
                    #return render(request, 'ebook/category_book.html', context={'object_search':object_search})
                    return render(request,'ebook/search.html',params)

        return render(request,'app_authenticate/login.html', context={'form':form})
    else:    
        query=request.GET['query']
        if len(query)>100:
            object_search = []
        object_searchBookname = Book.objects.filter(bookname__icontains=query)
        object_searchAuthor = Book.objects.filter(author__icontains=query)
        object_search = object_searchBookname.union(object_searchAuthor)
        params={'object_search':object_search,'query':query}
        return render(request,'ebook/search.html',params)



