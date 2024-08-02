from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True}) )
                                      
    password = forms.CharField(
       widget=forms.PasswordInput(attrs={"autocomplete": "current-password" }))
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
    

                                         
class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()  

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2'] 


    def clean_password2(self):
        sd = self.cleaned_data
        if sd['password1'] != sd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return sd['password2']                                    
   
    