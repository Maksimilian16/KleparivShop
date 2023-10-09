from django import forms


class Products(forms.Form):
    phone_number = forms.CharField()
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    photo = forms.ImageField()
