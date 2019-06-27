from django import forms
from .models import AccountBook

class AccountBookForm(forms.ModelForm):
    """
    新規データ登録用のフォーム定義
    """
    class Meta:
        model = AccountBook
        fields = ['date', 'category', 'money', 'memo']