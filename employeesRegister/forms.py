from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):


    class Meta :
        model = Employee
        fields = ('firstName', 'lastName', 'department','position','emp_code','mobile', )
        labels = {
            'firstName' : 'FirstName',
            'lastName' : 'LastName',
            'emp_code' : 'Emp.Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "   -----------------Select------------------"
        self.fields['emp_code'].required = False

