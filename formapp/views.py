from django.shortcuts import render, redirect
from .models import Query

# Create your views here.
def home(request):
	if request.method == "POST" :
		name = request.POST.get("name")
		email = request.POST.get("email")
		subject = request.POST.get("subject")
		message = request.POST.get("message")

		query = Query(name = name, email = email, message = message, subject = subject)
		query.save()
		return redirect("/")
	else:
		return render(request, "index.html")
