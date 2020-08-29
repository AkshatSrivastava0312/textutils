# My creation

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name' : 'Akshat', 'work' : 'Computer Science Engineer', 'page_name' : 'Home'}
    return render(request, 'index.html', params)

def about(request):
    params = {'name' : 'Akshat', 'page_name' : 'About'}
    return render(request, 'about.html', params)

def analyze(request):
    params = {'name' : 'Akshat'}
    return render(request, 'analyze.html', params)

def action(request):
    text = request.GET.get('text', 'no value given')         # for post request, use  request.POST.get()
    rad_action = request.GET.get('rad_action', 'no action')    

    if text == 'no value given':
        return HttpResponse('No Text Given')

    if rad_action == 'no action':
        return HttpResponse('No Action Given')
    elif rad_action == 'countchars':    
        total = 0       
        for i in text:  
            if i is not None:              
                total = total + 1
        return HttpResponse(f'Total Characters : {total}')
    elif rad_action == 'removepunc':
        punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        new_text = ''
        removed = 0
        for char in text:
            if char not in punctuations:
                new_text = new_text + char
            else:
                removed = removed + 1
        return HttpResponse(f'Your Text After Removing {removed} punctuations : {new_text}')
    elif rad_action == 'removespaces':
        new_text = ''
        spaces = 0
        for char in text:
            if char != ' ':
                new_text = new_text + char
            else:
                spaces = spaces + 1
        return HttpResponse(f'Your Text After Removing {spaces} whitespaces : {new_text}')