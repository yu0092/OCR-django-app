import base64
import numpy as np
import pytesseract
from django.contrib import messages
from django.shortcuts import render
from PIL import Image

# 设置 Tesseract 路径
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def homepage(request):
    if request.method == "POST":
        try:
            image = request.FILES["imagefile"]
            # 将图片编码为 base64 字符串
            image_base64 = base64.b64encode(image.read()).decode("utf-8")
        except:
            messages.add_message(
                request, messages.ERROR, "No image selected or uploaded"
            )
            return render(request, "home.html")

        # 固定为中文和英文
        lang = "chi_tra+eng"
        
        img = np.array(Image.open(image))
        text = pytesseract.image_to_string(img, lang=lang)

        # 返回文字到 HTML
        return render(request, "home.html", {"ocr": text, "image": image_base64})

    return render(request, "home.html")


