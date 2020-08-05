from django import forms
from .models import StockMarket


class StockForm(forms.ModelForm):
    class Meta:
        model = StockMarket
        fields = ["ticker"]
