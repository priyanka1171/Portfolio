from django.shortcuts import render,redirect
from .forms import FbForm
from .models import FbModel


def welcome(request):
	return render(request,"welcome.html")

def home(request):
	if request.method=="POST":
		na=request.POST.get("name")
		fb=request.POST.get("feedback")
		d=FbModel(name=na,feedback=fb)
		d.save()
		fm=FbForm()
		return render(request,"home.html",{"fm":fm,"msg":"Thanks For Feedback!!"})
	else:
		fm=FbForm()
		return render(request,"home.html",{"fm":fm})
def course(request):
	return render(request,"course.html")
def intern(request):
	return render(request,"intern.html")