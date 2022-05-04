from django import forms

from adminportal.models import Course, User

class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ('is_deleted',)

class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        

