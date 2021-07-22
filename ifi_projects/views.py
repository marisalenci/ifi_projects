import csv
import io

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, View
from django.urls import reverse_lazy, reverse

from .models import Project, Country, Region

class ProjectList(ListView):
    model = Project
    
class ProjectDetail(DetailView):
    model = Project

class ProjectCreate(CreateView):
    model = Project
    fields = ['bank', 'project_number', 'country', 'name', 'local_cost', 'currency', 'usd_cost',
        'approval_date', 'url']
    success_url = reverse_lazy('projects')

class ImportProjects(View):

    def get(self, request):
        return render(request, 'project_upload.html')

    def post(self, request):
        csv_file = request.FILES['csv_file']
        reader = csv.DictReader(io.StringIO(csv_file.read().decode('utf-8')))
        for index, project in enumerate(reader, start=1):
            country, created = Country.objects.get_or_create(
                name=project['Country'])
            new_project = Project.objects.create(
                name=project['Project Name'],
                country=country,
                bank='IFC',
                )
        return redirect(reverse('projects'))