from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .form import profile_form
def profile(request):
    data=profile_form()
    if request.method=='POST':
        # name = request.POST.get('name')
        # mobile_no = request.POST.get('mobile_no')
        # desc = request.POST.get('desc')
        # bio =request.POST.get('bio')
        # birth_date =request.POST.get('birth_date')
        # address =request.POST.get('address')
        # city =request.POST.get('city')
        # username =request.POST.get('username')
        # district =request.POST.get('district')
        # state =request.POST.get('state')
        # country =request.POST.get('country')
        # postal_code =request.POST.get('postal_code')
        data = profile_form(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse("Save")
        else:
            print(data.errors)
            return HttpResponse("Error")
    return render(request,"index.html")