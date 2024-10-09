from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "price", "description"]
    