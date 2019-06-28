from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import models

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

def show_circle_graph(request):
    account_book_data = AccountBook.objects.all()

    total = sum([ item.money for item in account_book_data]) if account_book_data.count() != 0 else 0
    
    category_total_dict = dict()
    for category in Category.objects.all():
        category_total = AccountBook.objects.filter(category__category_name=category.category_name).aggregate(sum=models.Sum('money'))['sum']
        category_total = 0 if category_total is None else category_total
        category_total_dict[category.category_name] = int(100 * category_total/total) if total != 0 else 0
    
    return render(request, 'account_book/accountbook_circle.html',{
        'category_dict': category_total_dict,
    })