from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('product_name', 'product_description', 'avatar', 'category')
        # exclude = ('date_create', 'date_last_change', 'slug', 'views_count')

    def clean_product_name(self):
        cleaned_product_name = self.cleaned_data.get('product_name')
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in words:
            if word in cleaned_product_name:
                raise forms.ValidationError('Ошибка, связанная с названием продукта')

        return cleaned_product_name

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
