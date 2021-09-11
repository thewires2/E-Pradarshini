from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# class ProjectForm(forms.Form):
#     project_Year = forms.IntegerField(label='Year')
#     project_Class = forms.CharField(max_length=2,label='BE')
#     project_Mentor = forms.CharField(max_length=100)

class ProjectForm(forms.Form):

    project_Year = forms.IntegerField(
        label = "Select the Year",
        min_value =2015,
        max_value =2025,
        required = True,
    )

    project_Class = forms.CharField(
        label = "Select the Class",
        # choices = (('BE', 'BE'),('TE', 'TE'),('SE', 'SE')),
        max_length = 2,
        required = True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))