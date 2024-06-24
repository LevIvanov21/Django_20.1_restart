
from django.forms import ModelForm, forms, BooleanField

from Catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ("viewed", "slug",)

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if name.lower() in self.forbidden_words:
            raise forms.ValidationError(f'Вы ввели запрещенное слово: {name.upper()}')

        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")

        if description.lower() in self.forbidden_words:
            raise forms.ValidationError(f'Вы ввели запрещенное слово: {description.upper()}')

        return description
