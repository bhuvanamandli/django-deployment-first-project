from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def note(req):
 ss=input("Enter your note")
 k='''<head>Google-Notes</head>
 <center><h1 style='color:Blue'>YOUR ENTERED NOTE</h1><hr/>
 <h2 style='color:orange'>''',ss,'''</h2><hr/></center>'''
 return HttpResponse(k)
 
def show(req):
 ss="<head>Google-Notes</head><h1 style='color:plum'>Hi User!!!</h1>"
 return HttpResponse(ss)
 
def homepage(req):
 ss="<h1 style='color:plum'>Hi Google User</h1>"
 return HttpResponse(ss)
