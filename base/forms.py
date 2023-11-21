from django import forms
from django.forms import CheckboxSelectMultiple
from.models import Skills, Certification, Projects


class SkillsCreateForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'


class SkillsUpdateForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('level',)


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'

    skill = forms.ModelMultipleChoiceField(
        queryset=Skills.objects.all(),
        widget=CheckboxSelectMultiple,
    )
