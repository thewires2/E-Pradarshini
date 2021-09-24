from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class ProjectForm(forms.Form):
    CLASS_CHOICES = [
    ('BE', 'BE'),
    ('TE', 'TE'),
    ('SE', 'SE'),
    ]
    
    YEAR_CHOICES=[(r,r) for r in range(2015,2026)]

    project_Year = forms.IntegerField(
        label = "Select the Year",
        # min_value =2015,
        # max_value =2030,
        widget=forms.Select(choices=YEAR_CHOICES),
        required = True,
    )

    project_Class = forms.CharField(
        label = "Select the Class",
        widget=forms.Select(choices=CLASS_CHOICES),
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