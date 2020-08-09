from django import forms

from authapp.models import StrapUser
from authapp.forms import StrapUserChangeForm
from mainapp.models import Product


class StrapUserAdminChangeForm(StrapUserChangeForm):
    class Meta:
        fields = '__all__'
        model = StrapUser


class ProductAdminChangeForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Product

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field_name, field in self.fields.items():
        #     field.help_text = ''

    def clean_short_desc(self):
        product_short_desc = self.cleaned_data['short_description']
        min_limit = 0
        max_limit = 500
        # Change limit value
        if not min_limit < len(product_short_desc) < max_limit:
            raise forms.ValidationError(f'text size should be in ({min_limit}, {max_limit})')
        return product_short_desc

    def clean_desc(self):
        product_desc = self.cleaned_data['description']
        min_limit = 0
        max_limit = 500
        # Change limit value
        if not min_limit < len(product_desc) < max_limit:
            raise forms.ValidationError(f'text size should be in ({min_limit}, {max_limit})')
        return product_desc
