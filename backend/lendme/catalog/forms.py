from django import forms

from catalog.models import Item, ItemImage


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'category',
            'name',
            'description',
            'price',
            'time_period',
        )
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'time_period': forms.Select(attrs={'class': 'form-control', 'required': True}),
        }


class ItemImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.FileInput(attrs={"multiple": True, "id": "upload-image"}),
        required=True
    )

    class Meta:
        model = ItemImage
        fields = ('image',)
