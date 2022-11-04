from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    return render(request,'projects/projects.html',{"projects": projectsList})

def project(request,pk):
    projectObject = None
    for p in projectsList:
        if p['id']==pk:
            projectObject=p
    return render(request,'projects/single-project.html',{'project':projectObject})