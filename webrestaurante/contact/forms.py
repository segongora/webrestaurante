from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre'}), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={
                             'class': 'form-control', 'placeholder': 'Correo electrónico'}), min_length=3, max_length=100)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Mensaje', 'rows': 3}), min_length=3, max_length=1000)
