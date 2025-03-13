from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description']
        labels = {'title':'عنوان','description':'متن شکایت'}
        widgets = {'title': forms.TextInput(attrs={'class':'form-control'}),
                   'description':forms.Textarea(attrs={'class':'form-control'})}