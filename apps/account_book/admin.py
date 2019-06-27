from django.contrib import admin


from .models import Category, AccountBook

class AccontBookAdmin(admin.ModelAdmin):
    list_display= ['date', 'category', 'money', 'memo']

admin.site.register(Category)
admin.site.register(AccountBook, AccontBookAdmin)