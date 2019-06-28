from django.urls import path

from . import views

app_name = 'account_book'

urlpatterns = [
    path('account_book_list/', views.AccountBookListView.as_view(), name='account_book_list'),
    path('account_book_create/', views.AccountBookCreateView.as_view(), name='account_book_create'),
    path('create_done/', views.create_done, name='create_done'),
    path('update/<int:pk>/', views.AccountBookUpdateView.as_view(), name='account_book_update'),
    path('update_done/', views.update_done, name='update_done'),
    path('delete/<int:pk>/', views.AccountBookDeleteView.as_view(), name='account_book_delete'),
    path('delete_done/', views.delete_done, name='delete_done'),
    path('circle/', views.show_circle_graph, name='account_book_circle'),
]