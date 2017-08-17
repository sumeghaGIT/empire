from django import forms
from masters.models import Categories, TaskStatus
from django.forms import ModelChoiceField
from django.forms import ModelForm
from models import User

from masters import models


STATUS_CHOICES = (
       (1, ("Active")),
       (2, ("In Active")),
)


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class LocationsForm(forms.Form):
    location_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'location','class': 'form-control'}),label='Location', max_length=100)
    status = forms.ChoiceField(choices = STATUS_CHOICES, label="Status", initial='', widget=forms.Select(attrs={'id': 'status','class': 'form-control'}), required=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LocationsForm, self).__init__(*args, **kwargs)

    def clean_location_name(self):
        location_name = self.cleaned_data.get('location_name')
        if models.Location.objects.filter(name=location_name):
            raise forms.ValidationError(u'Locations already exists')
        return location_name


class CategoriesForm(forms.Form):
    category_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'category','class': 'form-control col-lg-6'}),label='Categories', max_length=100)
    status = forms.ChoiceField(choices = STATUS_CHOICES, label="Status", initial='', widget=forms.Select(attrs={'id': 'status','class': 'form-control'}), required=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CategoriesForm, self).__init__(*args, **kwargs)

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        if models.Categories.objects.filter(name=category_name):
            raise forms.ValidationError(u'Category already exists')
        return category_name


class ServicesForm(forms.Form):
    service_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'services','class': 'form-control'}),label='Services', max_length=100)
    # response_time = forms.CharField(widget=forms.TextInput(attrs={'id': 'response_time','class': 'form-control'}),label='Response Time', max_length=4)
    # threshold_time = forms.CharField(widget=forms.TextInput(attrs={'id': 'threshold_time','class': 'form-control'}),label='Threshold Time', max_length=4)
    # price = forms.CharField(widget=forms.TextInput(attrs={'id': 'price','class': 'form-control'}),label='Price', max_length=9)
    response_time = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'response_time','class': 'form-control', 'step': "1"}),label='Response Time')
    threshold_time = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'threshold_time','class': 'form-control', 'step': "1"}),label='Threshold Time')
    price = forms.FloatField(min_value=0.01, widget=forms.NumberInput(attrs={'id': 'price','class': 'form-control', 'step': "0.01"}))
    service_from = forms.CharField(widget=forms.DateInput(attrs={'id': 'service_from','class': 'form-control'}),label='Service From')
    service_to = forms.CharField(widget=forms.DateInput(attrs={'id': 'service_to','class': 'form-control'}),label='Service To')
    category_name = MyModelChoiceField(queryset = Categories.objects.filter(is_active=1), widget=forms.Select(attrs={'id': 'category','class': 'form-control'}), to_field_name="id", label="Category",empty_label="Choose your options")
    status = forms.ChoiceField(choices = STATUS_CHOICES, label="Status", initial='', widget=forms.Select(attrs={'id': 'threshold_time','class': 'form-control'}), required=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ServicesForm, self).__init__(*args, **kwargs)

    def clean_service_name(self):
        service_name = self.cleaned_data.get('service_name')
        if models.Services.objects.filter(name=service_name):
            raise forms.ValidationError(u'Service already exists')
        return service_name


class TaskStatusForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'task_status','class': 'form-control col-lg-6'}),label='Name', max_length=100)
    status = forms.ChoiceField(choices = STATUS_CHOICES, label="Status", initial='', widget=forms.Select(attrs={'id': 'status','class': 'form-control'}), required=True)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if models.TaskStatus.objects.filter(status=name) :
            raise forms.ValidationError(u'This task status already exists')
        elif models.InquiryStatus.objects.filter(status=name) :
            raise forms.ValidationError(u'This Inquiry status already exists')
        elif models.InquirySources.objects.filter(sources=name) :
            raise forms.ValidationError(u'This Inquiry source already exists')
        else:
            if models.Department.objects.filter(name=name) :
                raise forms.ValidationError(u'This Department name already exists')
        return name


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='confirm_password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']

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
    status = forms.ChoiceField(choices = STATUS_CHOICES, label="Status", initial='', widget=forms.Select(attrs={'id': 'status','class': 'form-control'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'status', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email address already exists')
        return email