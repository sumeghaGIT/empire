from django import forms

class MyForm(forms.Form):
    location_name = forms.CharField()
    # message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass