from django import forms

# choice para escolher uma quantidade entre 1 e 20
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range (1, 21)]


class CartAddProductForm(forms.Form):
    # coerce, converte a entrada em inteiro
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
