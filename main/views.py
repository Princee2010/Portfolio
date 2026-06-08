from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, ContactMessage
from .forms import ContactForm



def home(request):
    context = {
    'languages': Skill.objects.filter(category='language'),
    'frontend': Skill.objects.filter(category='frontend'),
    'backend': Skill.objects.filter(category='backend'),
    'database': Skill.objects.filter(category='database'),
    'datascience': Skill.objects.filter(category='datascience'),
    'tools': Skill.objects.filter(category='tools'),
}
    return render(request, 'home.html', context)


def about(request):
    skills = Skill.objects.all()
    projects_count = Project.objects.count()
    context = {
        'skills': skills,
        'projects_count': projects_count,
    }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Message sent successfully! I'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def projects(request):
    all_projects = Project.objects.all()
    category = request.GET.get('category', '')
    if category:
        all_projects = all_projects.filter(category=category)
    return render(request, 'projects.html', {'projects': all_projects, 'active_category': category})

