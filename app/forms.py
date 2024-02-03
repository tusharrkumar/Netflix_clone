from django import forms
from app.models import *
import re

class Signup_Form(forms.ModelForm):
    # password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password',
    #                                                          'placeholder': 'Enter your password'}))
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {'username':forms.TextInput(attrs={'placeholder': 'Enter Username'}),
                    'email':forms.TextInput(attrs={'placeholder':'Enter mail'}),
                   'password':forms.PasswordInput(attrs={'placeholder':'Enter Password'})}
        help_texts = {'username':''}
    
    def clean(self):
        un = self.cleaned_data.get('username')
        em = self.cleaned_data.get('email')
        pw = self.cleaned_data.get('password')
        
        if len(un)>10:
            raise forms.ValidationError('username length should be less than 10')
        
        if not un.isalpha():
            raise forms.ValidationError('username should be only alphabets')
        
        vem = re.match('[a-zA-Z1-9]\w*[.]?\w+@gmail[.]com',em)
        if vem == None:
            raise forms.ValidationError('Email is not valid')
        # if vem:
        #     pass
        # else:
        #     raise forms.ValidationError('Email is not valid')
        
        if len(pw)>7:
            raise forms.ValidationError('Password length must be less than or equal to 7')
        
        
