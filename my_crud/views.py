from django.shortcuts import render
from . models import Player
from django.contrib import messages

# Create your views here.
def home(request):
	display=Player.objects.all()
	return render(request,'first.html',{"Player":display})
	
def create(request):
	if request.method=="POST":
		if request.POST.get('ID') and request.POST.get('Player_Name') and request.POST.get('Player_Email') and request.POST.get('Country') and request.POST.get('No_of_Games') and request.POST.get('Total_Score'):
			add= Player()
			add.ID=request.POST.get('ID')
			add.Player_Name=request.POST.get('Player_Name')
			add.Player_Email=request.POST.get('Player_Email')
			add.Country=request.POST.get('Country')
			add.No_of_Games=request.POST.get('No_of_Games')
			add.Total_Score=request.POST.get('Total_Score')
			add.save()
			messages.success(request,"The data of"+add.Player_Name+"is saves successfully")
			return render(request,"second.html")
	else:
		return render(request,"second.html")