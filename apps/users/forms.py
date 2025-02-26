from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpUserForm(UserCreationForm):
    email = forms.EmailField(required=True,
                            widget=forms.EmailInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    first_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}))
    last_name = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({"placeholder":"Username", "class":"form-control"})
        self.fields['password1'].widget.attrs.update({"placeholder":"Password", "class":"form-control"})
        self.fields['password2'].widget.attrs.update({"placeholder":"Confirm Password", "class":"form-control"})