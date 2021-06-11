import cv2
from django.shortcuts import render
from .models import feedback,ppeviwer
from .forms import PPEviewerForm
from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading

# Create your views here.
def index(request):
    return render(request,'index.html')

def records(request):
    return render(request,'records.html')

def livesteaming(request):
    ppedata=ppeviwer.objects.all()
    data = feedback.objects.all()
    context =  {
        'PPEdata': data,
        "ppeviwer":ppedata
        
        }
    return render(request,'livesteaming.html',context)

def gallery(request):
    return render(request,'gallery.html')
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