from django import forms
from masters.models import Categories, TaskStatus, Services
from django.forms import ModelChoiceField
from django.forms import ModelForm
from django.contrib.auth import get_user_model

from masters import models

User = get_user_model()

STATUS_CHOICES = (
       (1, ("Active")),
       (2, ("In Active")),
)

EMPLOYEE_CHOICES = (
    ("1", ("SalesMan")),
    ("2", ("Admin")),
)

TICKET_CHOICES = (
       (1, ("Request")),
       (2, ("Query")),
       (3, ("Sales Inquiry")),
)

CUSTOMER_TYPE = ((1, "internal"),
                 (2, "customer"),)

class MyModelChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.name


class InternalUserChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.username


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
    response_time = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'response_time','class': 'form-control', 'step': "1"}),label='Response Time')
    threshold_time = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'threshold_time','class': 'form-control', 'step': "1"}),label='Threshold Time')
    price = forms.FloatField(min_value=0.01, widget=forms.NumberInput(attrs={'id': 'price','class': 'form-control', 'step': "0.01"}))
    service_from = forms.CharField(widget=forms.DateInput(attrs={'class':'form-control timepicker input-12-hour-icon-button'}))
    service_to = forms.CharField(widget=forms.DateInput(attrs={'class':'form-control timepicker input-12-hour-icon-button'}))
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
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username','class': 'form-control'}),label='User Name')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'first_name','class': 'form-control'}),label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'last_name','class': 'form-control'}),label='Last Name')
    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'email','class': 'form-control'}),label='Email Address')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirm Password')
    department = forms.ChoiceField(choices=EMPLOYEE_CHOICES, widget=forms.Select(attrs={'id': 'department','class': 'form-control'}), label="Department", initial='')
    designation = forms.ChoiceField(choices=EMPLOYEE_CHOICES, widget=forms.Select(attrs={'id': 'designation','class': 'form-control'}), label="Designation", initial='')
    mobile = forms.CharField(widget=forms.TextInput(attrs={'id': 'mobile','class': 'form-control'}),label='Mobile', max_length=10)
    address1 = forms.CharField(widget=forms.TextInput(attrs={'id': 'address1','class': 'form-control'}),label='Address1', max_length=255)
    address2 = forms.CharField(widget=forms.TextInput(attrs={'id': 'address1','class': 'form-control'}),label='Address2', max_length=255)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'department', 'designation', 'password1', 'password2','mobile', 'address1','address2']

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
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username','class': 'form-control'}),label='User Name')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'first_name','class': 'form-control'}),label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'last_name','class': 'form-control'}),label='Last Name')
    department = forms.ChoiceField(choices=EMPLOYEE_CHOICES, widget=forms.Select(attrs={'id': 'user_type','class': 'form-control'}), label="Department", initial='')
    designation = forms.ChoiceField(choices=EMPLOYEE_CHOICES, widget=forms.Select(attrs={'id': 'designation','class': 'form-control'}), label="Designation", initial='')
    mobile = forms.CharField(widget=forms.TextInput(attrs={'id': 'mobile','class': 'form-control'}),label='Mobile', max_length=10)
    address1 = forms.CharField(widget=forms.TextInput(attrs={'id': 'address1','class': 'form-control'}),label='Address1', max_length=255)
    address2 = forms.CharField(widget=forms.TextInput(attrs={'id': 'address1','class': 'form-control'}),label='Address2', max_length=255)
    status = forms.ChoiceField(choices = STATUS_CHOICES, label="Status", initial='', widget=forms.Select(attrs={'id': 'status','class': 'form-control'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'department', 'designation','status','mobile', 'address1','address2']

class CreateTicketForm(forms.Form):
    customer_type = forms.ChoiceField(choices=CUSTOMER_TYPE, label="Customer type", initial='', widget=forms.Select(attrs={'id': 'customer_type','class': 'form-control'}))
    internal_customer = InternalUserChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'id': 'users', 'class': 'form-control'}), to_field_name="id", label="Internal customers",empty_label="Choose your options")
    ticket_type = forms.ChoiceField(choices=TICKET_CHOICES, label="Ticket Types", initial='', widget=forms.Select(attrs={'id': 'ticket_type','class': 'form-control'}))
    category_name = MyModelChoiceField(queryset=Categories.objects.filter(is_active=1), widget=forms.Select(attrs={'id': 'category','class': 'form-control', 'onchange':'get_services(this.value);'}), to_field_name="id", label="Category" ,empty_label="Choose your options")
    service_name = MyModelChoiceField(queryset=Services.objects.filter(is_active=1), widget=forms.Select(attrs={'id': 'services','class': 'form-control services'}), to_field_name="id", label="Services",empty_label="Choose your options")
    comment = forms.CharField(widget=forms.Textarea(attrs={'id': 'comment','class': 'form-control','cols':100, 'rows':50}))
    activity_name = forms.CharField(widget=forms.Textarea(attrs={'id': 'activity','class': 'form-control activity','cols':100, 'rows':50}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CreateTicketForm, self).__init__(*args, **kwargs)


class CustomerCreateForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'first_name','class': 'form-control'}),label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'last_name','class': 'form-control'}),label='Last Name')
    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'email','class': 'form-control'}),label='Email Address')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirm Password')

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


class UpdateCreateForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    status = forms.ChoiceField(choices=STATUS_CHOICES, label="Status", initial='',
                           widget=forms.Select(attrs={'id': 'status', 'class': 'form-control'}), required=True)
