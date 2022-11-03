from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def photo(req):
 ss=input("Enter your photo-name")
 k='''<head>Google-Photos</head>
 <center><h1 style='color:Blue'>YOUR ENTERED Photo-name</h1><hr/>
 <h2 style='color:orange'>''',ss,'''</h2><hr/></center>'''
 return HttpResponse(k)
 
def show(req):
 ss="<head>Google-Photos</head><h1 style='color:plum'>Hi User!!!</h1>"
 return HttpResponse(ss)
 
