from django import forms
from django.forms import CheckboxSelectMultiple
from .models import Skills, Certification, Projects, Resume


class SkillsCreateForm(forms.ModelForm):
    icon = forms.FileField(label='Icon')

    class Meta:
        model = Skills
        fields = ('name', 'level')


class SkillsUpdateForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('level',)


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    img = forms.FileField(label='Choose Image')

    class Meta:
        model = Projects
        exclude = ('img_url',)

    skill = forms.ModelMultipleChoiceField(
        queryset=Skills.objects.all(),
        widget=CheckboxSelectMultiple,
    )


class ResumeForm(forms.ModelForm):
    file = forms.FileField(label='Upload Resume')

    class Meta:
        model = Resume
        fields = '__all__'
