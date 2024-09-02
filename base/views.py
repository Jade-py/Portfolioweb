from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Skills, Certification, Projects, Resume
from .forms import SkillsCreateForm, SkillsUpdateForm, CertificationForm, ProjectForm, ResumeForm
from django.conf import settings
from django.http import HttpResponse
import os


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper


def home(request):
    skills = Skills.objects.all()
    certificates = Certification.objects.all()
    projects = Projects.objects.all()

    context = {
        'skills': skills,
        'certificates': certificates,
        'projects': projects,
    }

    return render(request, 'index.html', context)


def resume(request):
    pdf = os.path.join(settings.BASE_DIR, Resume.objects.get(id=1).file.path)
    filename = pdf.split('/')[-1]
    with open(pdf, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{filename}"'

    return response


@login_required
def workspace(request):
    skills = Skills.objects.all()
    certificates = Certification.objects.all()
    projects = Projects.objects.all()
    form1 = SkillsCreateForm()
    form2 = SkillsUpdateForm()
    form3 = CertificationForm()
    form4 = ProjectForm()
    form5 = ResumeForm()

    if request.method == 'POST':
        print(request.POST)

        if 'SkillsCreate' in request.POST:
            form1 = SkillsCreateForm(request.POST, request.FILES)
            if form1.is_valid():
                form1.save()
                return redirect('workspace')
            else:
                print(form1.errors)

        elif "SkillsUpdate" in request.POST:
            form2 = SkillsUpdateForm(request.POST)
            name = request.POST.get('SkillsUpdate')
            skill = Skills.objects.get(name=name)
            if form2.is_valid():
                skill.level = form2.cleaned_data['level']
                skill.save()
            else:
                print(form2.errors)

        elif 'Certification' in request.POST:
            form3 = CertificationForm(request.POST)
            if form3.is_valid():
                certificate = Certification(
                    name=form3.cleaned_data['name'],
                    platform=form3.cleaned_data['platform'],
                    start=form3.cleaned_data['start'],
                    end=form3.cleaned_data['end'],
                    verification_link=form3.cleaned_data['verification_link']
                )
                certificate.save()
                return redirect('workspace')
            else:
                print(form3.errors)

        elif 'Projects' in request.POST:
            form4 = ProjectForm(request.POST, request.FILES)
            if form4.is_valid():
                form4.save()
                return redirect('workspace')
            else:
                print(form4.errors)

        elif 'resume' in request.POST:
            obj = Resume.objects.get(id=1)
            file_path = obj.file.path
            print(file_path)
            if os.path.isfile(file_path):
                os.remove(file_path)
            form5 = ResumeForm(request.POST, request.FILES, instance=obj)
            print('1')
            if form5.is_valid():
                print('2')
                form5.save()
                print('3')
                return redirect('workspace')
            else:
                print(form5.errors)
    else:
        form1 = SkillsCreateForm()
        form2 = SkillsUpdateForm()
        form3 = CertificationForm()
        form4 = ProjectForm()
        form5 = ResumeForm()

    context = {
        'skills': skills,
        'certificates': certificates,
        'projects': projects,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
    }
    return render(request, 'workspace.html', context)


class DeleteSkills(DeleteView):
    model = Skills
    success_url = reverse_lazy('workspace')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


class DeleteProjects(DeleteView):
    model = Projects
    success_url = reverse_lazy('workspace')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


class DeleteCertification(DeleteView):
    model = Certification
    success_url = reverse_lazy('workspace')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


def checkup(pk):
    try:
        b = Certification.objects.get(pk=pk - 1)
        return b
    except:
        if pk>0:
            pk = pk - 1
            b = checkup(pk=pk)
            return b
        else:
            b = None
            return b


def checkdown(pk):
    try:
        b = Certification.objects.get(pk=pk + 1) or Projects.objects.get(pk=pk + 1)
        return b
    except:
        if pk <= Certification.objects.last().pk:
            pk = pk + 1
            b = checkdown(pk=pk)
            return b
        else:
            b = None
            return b


def moveup(request, model, pk):

    if model == 'Certification':
        a = Certification.objects.get(pk=pk)
        try:
            b = Certification.objects.get(pk=pk - 1)
        except:
            pk = pk-1
            b = checkup(pk=pk)
        print(b)
        if b:
            a.pk, b.pk = b.pk, a.pk
            a.save()
            b.save()

    if model == 'Projects':
        a = Projects.objects.get(pk=pk)
        try:
            b = Projects.objects.get(pk=pk - 1)
        except:
            pk = pk - 1
            b = checkup(pk=pk)
        print(b)
        if b:
            a.pk, b.pk = b.pk, a.pk
            a.save()
            b.save()
    return redirect(reverse_lazy('workspace'))


def movedown(request, model, pk):
    if model == 'Certification':
        a = Certification.objects.get(pk=pk)
        try:
            b = Certification.objects.get(pk=pk + 1)
        except:
            pk = pk + 1
            b = checkdown(pk=pk)
        print(b)
        if b:
            a.pk, b.pk = b.pk, a.pk
            a.save()
            b.save()

    if model == 'Projects':
        a = Projects.objects.get(pk=pk)
        try:
            b = Projects.objects.get(pk=pk + 1)
        except:
            pk = pk + 1
            b = checkdown(pk=pk)
        print(b)
        if b:
            a.pk, b.pk = b.pk, a.pk
            a.save()
            b.save()
    return redirect(reverse_lazy('workspace'))
