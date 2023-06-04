from django import forms
from . models import *



class CustomerRegister(forms.ModelForm):
    password1 = forms.CharField(label=('Password'),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label=('Confirm Password'),widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Customer
        fields = ['full_name','email','username','password1','password2','address']
        widgets={
            'full_name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
        }



class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        exclude = ['booking_status','subtotal','discount','amount','cart','payment_completed','ref']
        widgets={
            'check_in':forms.TextInput(attrs={'class':'form-control'}),
            'check_out':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'adults':forms.Textarea(attrs={'class':'form-control'}),
            'children':forms.Textarea(attrs={'class':'form-control'}),
            'booked_by':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = '__all__'
        exclude = ['Blogusercomment','post']