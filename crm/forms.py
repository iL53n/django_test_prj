from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        min_length=6,
        # required=False,
        widget=forms.TextInput(attrs={'class': 'form_control'}),
    )
    phone = forms.CharField(
        max_length=200,
        min_length=10,
        widget=forms.TextInput(attrs={'class': 'form_control'}),
    )
