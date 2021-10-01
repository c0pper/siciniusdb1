from django import forms

class DateInput(forms.DateInput):
    input_type = "date"

class CreateNewPerson(forms.Form):
    fname = forms.CharField(label="Nome", max_length=30)
    lname = forms.CharField(label="Cognome", max_length=30, required=True)
    birth_date = forms.DateField(label="Data di nascita", widget=DateInput, required=False)
    phone = forms.CharField(label="Telefono", max_length=13, required=False)
    city = forms.CharField(label="Città", max_length=30, required=True)
    province = forms.CharField(label="Provincia", max_length=2, required=True)
    job = forms.CharField(label="Lavoro", max_length=30, required=False)