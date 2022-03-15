from django import forms

from adminportal.models import Course

class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ('is_deleted',)

