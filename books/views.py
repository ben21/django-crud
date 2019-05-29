# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from books.forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from books.models import Book
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class BookList(LoginRequiredMixin, ListView):
    model = Book

class BookView(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')



