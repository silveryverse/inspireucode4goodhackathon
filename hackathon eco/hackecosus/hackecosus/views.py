
from django.http import HttpResponse
from django.shortcuts import render, redirect
from service.models import UploadCattleImage, UploadedImage
from service.forms import ImageUploadForm, CattleImageUploadForm
import subprocess


# def flask_integration(request):

#     subprocess.Popen(['python', 'app.py'])


#     return HttpResponse("Flask app is running.")


def homePage(request):
    data = {
        'title': 'Ecosystem And Sustainability'
    }
    return render(request, 'index.html', data)

def aboutUs(request):
    data = {
        'title': 'About Us'
    }
    return render(request, 'aboutus.html', data)
def plant(request):
    data = {
        'title': 'Plant'
    }
    return redirect('http://127.0.0.1:5000', data)



def upload_image(request):
    data = {
        'title': 'Your Locality'
    }

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
 
        if form.is_valid():
            image= request.FILES.get('image')
            description=request.POST.get('description')
            location=request.POST.get('location')
            pincode=request.POST.get('pincode')
            uploaded_at=request.POST.get('uploaded_at')
            en=UploadedImage(image=image,description=description,location=location,pincode=pincode,uploaded_at=uploaded_at)
            en.save()
            return redirect('/check-your-locality')

    else:
        form = ImageUploadForm()
    return render(request, 'uploadimage.html', {'form': form}, data)
 
def uploadcattleimage(request):
    data = {
        'title': 'Upload Cattle Issues'
    }

    if request.method == 'POST':
        form = CattleImageUploadForm(request.POST, request.FILES)
 
        if form.is_valid():
            image= request.FILES.get('image')
            description=request.POST.get('description')
            location=request.POST.get('location')
            pincode=request.POST.get('pincode')
            uploaded_at=request.POST.get('uploaded_at')
            en=UploadCattleImage(image=image,description=description,location=location,pincode=pincode,uploaded_at=uploaded_at)
            en.save()
            return redirect('/cattle-management-info-panel')

    else:
        form = CattleImageUploadForm()
    return render(request, 'cattlemanagement.html')
 
 
def uploadedcattleImages(request):
    data = {
        'title': 'Cattle Panel'
    }
    serviceData=UploadCattleImage.objects.all()

    context={
        'serviceData':serviceData
    }
    return render(request, 'cattlemanagepanel.html', context)


    # if request.method=="POST":
    #     form = ImageUploadForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         image= request.POST.get('image')
    #         description=request.POST.get('description')
    #         location=request.POST.get('location')
    #         uploaded_at=request.POST.get('uploaded_at')
    #         en=UploadedImage(image=image,description=description,location=location,uploaded_at=uploaded_at)
    #         en.save()
    #         return HttpResponse("success")

    # return render(request, 'uploadimage.html')



def locality(request):
    serviceData=UploadedImage.objects.all()

    context={
        'serviceData':serviceData
    }
    return render(request, 'locality.html', context)

def leaderboard(request):
    return render(request, 'leaderboard.html')

def weather(request):
    return render(request, 'weather.html')



import requests
import datetime
from django.shortcuts import render

def weather(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6ec404fe5625938fb0da68e398c67b93'
    PARAMS = {'units': 'metric'}

    API_KEY = 'YOUR_GOOGLE_API_KEY'
    SEARCH_ENGINE_ID = 'YOUR_SEARCH_ENGINE_ID'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    
    # Check if search_items is None before accessing it
    search_items = data.get("items")
    if search_items:
        image_url = search_items[1]['link']
    else:
        image_url = ''  # Provide a default value if there are no search items
    
    data = requests.get(url, params=PARAMS).json()
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    day = datetime.date.today()

    return render(request, 'weather.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city, 'exception_occurred': False, 'image_url': image_url})


def nursery(request):
    return render(request, 'nursery.html')


