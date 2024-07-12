from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UploadFilesForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV File', required=True)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class TeacherSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        teacher_profile = UserProfile.objects.create(user=user, is_teacher=True)
        return user


class StudentSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        student_profile = UserProfile.objects.create(user=user, is_student=True)
        return user

from django import forms
from .models import StudyMaterial

class StudyMaterialForm(forms.ModelForm):
    performance_level = forms.ChoiceField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    links = forms.URLField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter links (optional)'}))
    sms_recommendations = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Enter SMS recommendations (optional)'}))

    class Meta:
        model = StudyMaterial
        fields = ['performance_level', 'title', 'links', 'sms_recommendations']

# forms.py

from django import forms
from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name', 'roll_number', 'mobile_number', 'address']
