from django.shortcuts import redirect, render
from .models import feedback,ppeviwer
from .forms import PPEviewerForm,ppForm
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from django.core.files import File
import sys
import os
from PPE.settings import BASE_DIR

print(sys.path.append('H:\Edata\PPE-UI-Django\PPE\yolov5'))
from yolov5 import detect
# sys.path.append(os.path.abspath(os.path.join('..', 'yolov5')))
# from yolov5.detect import detect


print(sys.path)

# Create your views here.
def index(request):
    return render(request,'index.html')

def records(request):
    alldata=ppeviwer.objects.all()
    context={   
        'alldata1':alldata
                }
    return render(request,'records.html',context)

def livesteaming(request):



    if request.method == 'POST':
        form = ppForm(request.POST, request.FILES)
  
        if form.is_valid():
                     
            form.save()
            form=ppForm()
            

    else:
        form = ppForm()
    # onedata=ppeviwer.objects.latest('id')
    alldata=ppeviwer.objects.all()
    context={
        'form' : form,
        # 'snapdata':onedata,
        'alldata1':alldata
                }

    detect.logic('H:\Edata\PPE-UI-Django\PPE\media\images')
    

    return render(request, 'livesteaming.html', context)
def deletesnap(request,pk):
    try:
        obj=ppeviwer.objects.get(pk=pk)
        obj.delete()
        path='H:\Edata\PPE-UI-Django\PPE/'+str(obj.pm.url)
        os.remove(path)
      
    except:
        return render(request,'livesteaming.html')


    return render(request,'livesteaming.html')

def gallery(request):
    snapdata=ppeviwer.objects.all()
    context={
        'snap':snapdata

    }
    return render(request,'gallery.html',context)

def Fb(request):
  
    if request.method=='POST':    
        form = PPEviewerForm(request.POST)
        if form.is_valid():
            form.save()
            form = PPEviewerForm()
    else:
        form = PPEviewerForm()
        # return render(request,'form.html',context)

    data = feedback.objects.all()
    context =  {
        'form': form,
        'PPEdata': data
    }
    return render(request,'form.html',context)


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def livefe(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass