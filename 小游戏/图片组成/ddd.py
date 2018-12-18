from img2html.converter import Img2HTMLConverter

converter = Img2HTMLConverter(char='人生苦短，我学Python')
html = converter.convert("微信图片_20181130144421.jpg")

with open("mnls.html", mode='w', encoding="utf-8") as f:
    f.write(html)