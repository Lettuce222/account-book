from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Category, AccountBook
from .forms import AccountBookForm

class AccountBookListView(ListView):
    model = AccountBook

class AccountBookCreateView(CreateView):
    model = AccountBook
    form_class = AccountBookForm
    success_url = reverse_lazy('account_book:create_done')

def create_done(request):
    return render(request, 'account_book/create_done.html')

class AccountBookUpdateView(UpdateView):
    model = AccountBook
    form_class = AccountBookForm
    success_url = reverse_lazy('account_book:update_done')

def update_done(request):
    return render(request, 'account_book/update_done.html')

class AccountBookDeleteView(DeleteView):
    model = AccountBook
    success_url = reverse_lazy('account_book:delete_done')

def delete_done(request):
    return render(request, 'account_book/delete_done.html')
