from django import forms
from django.core.exceptions import ValidationError

from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields= ("tc_no", "name", "surname", "phone", "city", "state")

    def clean(self):
        cleaned_data = super().clean()
        tc_no = cleaned_data.get("tc_no")
        phone = cleaned_data.get("phone")
        
        if tc_no and phone:
            if (len(tc_no) != 11 
                or len(phone) != 11 ):
                raise forms.ValidationError("Check Your Information!")
        else:
            return None
