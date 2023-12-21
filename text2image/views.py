
from django.shortcuts import render
from .text2image import query
from PIL import Image
import io
import base64
from django.views.decorators.csrf import csrf_exempt
from django import forms


class ImageUploadForm(forms.Form):
    image = forms.ImageField()

@csrf_exempt
def text2image(request):
    if request.method == 'POST':
        text_input = request.POST.get('text_input', '')
        image_bytes = query({
            "inputs": text_input,
        })
        image = Image.open(io.BytesIO(image_bytes))
        img_io = io.BytesIO()
        image.save(img_io, format='JPEG')
        img_url = base64.b64encode(img_io.getvalue()).decode()
        return render(request, 'image.html', {'img_url': img_url})
    return render(request, 'text2image.html')