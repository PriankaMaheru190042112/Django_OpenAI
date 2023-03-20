from django.shortcuts import render
import openai,os,requests
from dotenv import load_dotenv
from django.core.files.base import ContentFile
from .models import AI_Images
# Create your views here.


load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def home(request):
    obj = None
    if openai.api_key is not None and request.method =='POST':
        desc= request.POST.get('desc')
        response= openai.Image.create(
            prompt= desc,
            size='256x256'
        )
        img= response["data"][0]["url"]
        response = requests.get(img)
        img_file= ContentFile(response.content)

        count=AI_Images.objects.count()+1
        fname= f"image-{count}.jpg"

        obj= AI_Images(desc=desc)
        obj.ai_image.save(fname, img_file)
        obj.save()

        print(obj)

    return render(request,'home.html',{"obj":obj})
