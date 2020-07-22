from django.shortcuts import render

# Create your views here.
def ListView(request):
	return render(request,'frontend/index.html')