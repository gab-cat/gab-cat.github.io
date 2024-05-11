from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    myMembers = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': myMembers,
    }
    return HttpResponse(template.render(context, request))
