from django import forms
from .models import Contact,BlogComment,Booking


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

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'room':forms.TextInput(attrs={'class':'form-control'}),
            'check_in':forms.TextInput(attrs={'class':'form-control'}),
            'check_out':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'adults':forms.Textarea(attrs={'class':'form-control'}),
            'children':forms.Textarea(attrs={'class':'form-control'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = '__all__'
        exclude = ['Blogusercomment','post']