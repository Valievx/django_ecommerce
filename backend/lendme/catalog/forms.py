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


class ItemImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.FileInput(attrs={"multiple": True, "id": "upload-image"}))

    class Meta:
        model = ItemImage
        fields = ('image',)
