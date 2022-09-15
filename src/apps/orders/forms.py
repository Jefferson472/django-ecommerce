from django import forms

# from localflavor.us.forms import USZipCodeField

from .models import Order


class OrderCreateForm(forms.ModelForm):
    # postal_code = USZipCodeField() # localflavor não será usado no código, somente demonstração de exemplo
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email',
            'address', 'postal_code', 'city',
        ]
