from django import forms
from .models import FormData, Branch, District, AccountType, Material


class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'district', 'branch', 'actype',
                  'materials']
        widgets = {
            'dob': forms.TextInput(attrs={'type': 'date'}),
            'materials': forms.CheckboxSelectMultiple(),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['branch'].queryset = Branch.objects.none()

            if 'district' in self.data:
                try:
                    district_id = int(self.data.get('district'))
                    self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['name']

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['district','name']



class AccountTypeForm(forms.ModelForm):
    class Meta:
        model = AccountType
        fields = ['name']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name']
