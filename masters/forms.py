""""
from django import forms
from masters.models import Categories
from django.forms import ModelChoiceField


from django.forms import ModelForm
from models import User


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class LocationsForm(forms.Form):
    location_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'location','class': 'special'}),label='Location', max_length=100)
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LocationsForm, self).__init__(*args, **kwargs)


class CategoriesForm(forms.Form):
    category_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'category','class': 'special'}),label='Categories', max_length=100)
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CategoriesForm, self).__init__(*args, **kwargs)


class ServicesForm(forms.Form):
    STATUS_CHOICES = (
           (1, ("Active")),
           (2, ("In Active")),
    )
    service_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'services','class': 'special'}),label='Services', max_length=100)
    response_time = forms.CharField(widget=forms.TextInput(attrs={'id': 'response_time','class': 'special'}),label='Response Time', max_length=4)
    threshold_time = forms.CharField(widget=forms.TextInput(attrs={'id': 'threshold_time','class': 'special'}),label='Threshold Time', max_length=4)
    # category_name = forms.ModelChoiceField(queryset = Categories.objects.filter(is_active=1), to_field_name="id", label="Category",empty_label="(Choose your options)")
    category_name = MyModelChoiceField(queryset = Categories.objects.filter(is_active=1), to_field_name="id", label="Category",empty_label="(Choose your options)")
    status = forms.ChoiceField(choices = STATUS_CHOICES, label="Status", initial='', widget=forms.Select(), required=True)

    class Meta:
        model = User
        fields = ['service_name', 'response_time', 'threshold_time', 'category_name']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ServicesForm, self).__init__(*args, **kwargs)


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='confirm_password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']
        exclude = ('password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email address already exists')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2


class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
"""