from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from keras.models import load_model
from keras.preprocessing.image import img_to_array, save_img
import numpy as np 
import cv2 as cv

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get_images')
    else:
        form = imageForm()
    return render(request, 'index.php', {'form': form})


def reupload_images(request):
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get_images')
    else:
        form = imageForm()
    return render(request, 'index.php', {'form': form})


def get_images(request):
    if request.method == 'GET':
        images = Image_Upload.objects.all()
        print(images)
        return render(request, 'show_image.php', {'images': images})


def del_images(request):
    Image_Upload.objects.all().delete()
    return reupload_images(request)


def predict_image(request):
    predictmodels = load_model('C:/Dev/Coba Django/SED_net/LenetModel1.model')
    label_info = {1:'Tidak Memperhatikan', 0:'Memperhatikan'}
    # if request.method == 'GET':
    images = Image_Upload.objects.all()
    url = images[len(images)-1].name_Img.url
    original_image = cv.imread("C:/Dev/Coba Django/SED_net"+url)
    grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    detected_faces = face_cascade.detectMultiScale(grayscale_image)
    for (column, row, width, height) in detected_faces:
        face_res = grayscale_image[row:row + width, column:column + width]

        resized_img = cv.resize(face_res, (100, 100))
        reshaped = np.reshape(resized_img, (1, 100, 100, 1))
        res = predictmodels.predict(reshaped)
        info = np.argmax(res, axis=1)[0]
        if info == 1:
            img_rec = cv.rectangle(original_image, (column, row), (column + width, row + height), (0,0,255),2)
            cv.rectangle(original_image, ((column-40), row + height + 20), (column + width + 60, row + height), (0,0,255), cv.FILLED)
            cv.putText(img_rec, label_info[info], ((column-25), row + height + 15), cv.FONT_HERSHEY_PLAIN, 0.8, (255,0,0),1)
        else:
            img_rec = cv.rectangle(original_image, (column, row), (column + width, row + height), (0,255,0),2)
            cv.rectangle(original_image, ((column-40), row + height + 20), (column + width + 60, row + height), (0,255,0), cv.FILLED)
            cv.putText(img_rec, label_info[info], ((column-25), row + height + 15), cv.FONT_HERSHEY_PLAIN, 0.8, (255,0,0),1)
    filename = "C:/Dev/Coba Django/SED_net/static/img/predictimg.jpg"
    cv.imwrite(filename, original_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    # return HttpResponse(filename)
    return render(request, 'predict_image.php', {'imagesUrl': filename})
