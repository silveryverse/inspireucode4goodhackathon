
from django.http import HttpResponse
from django.shortcuts import render, redirect
from service.models import UploadedImage
from service.forms import ImageUploadForm
import subprocess


# def flask_integration(request):

#     subprocess.Popen(['python', 'app.py'])


#     return HttpResponse("Flask app is running.")


def homePage(request):
   
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'aboutus.html')
def plant(request):
    return redirect('http://127.0.0.1:5000')



def upload_image(request):

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
    return render(request, 'uploadimage.html', {'form': form})
 
 


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