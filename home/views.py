from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from yolov5 import detect
import os
import urllib
from yolov5.utils.plots import output_to_target


def home(request):
    context={'a':1}

    return render(request,'headerPage.html',context)

def index(request):
    context={'a':1}
 
    return render(request,'index.html',context)

async def predictImage(request):
    print(request)
    print(request.POST.dict())
    fileObj = request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName = fs.save(fileObj.name,fileObj)
    filePathName = fs.url(filePathName) 
    filename = os.path.basename(filePathName.replace('%20',' '))
    detect.run( weights ='yolov5/runs/train/weights/best.pt',
                source='media/'+filename, 
                iou_thres=0.45, 
                line_thickness=1,
                imgsz=[640,640],
                project='media/detect',
                view_img=False )
    output = 'media/detect/'+os.path.basename(filePathName)
    context={'filePathName':filePathName,'output':output} 
    return render(request,'index.html',context)
