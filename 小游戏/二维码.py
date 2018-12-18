import qrcode 
# 复杂的生成二维码
def make_code(text):
	#  version是二维码的尺寸，数字大小决定二维码的密度       error_correction：是指误差    
	# box_size:参数用来控制二维码的每个单元(box)格有多少像素点    
	# border: 参数用控制每条边有多少个单元格(默认值是4，这是规格的最小值    
	qr = qrcode.QRCode(version=5,
	                   error_correction=qrcode.constants.ERROR_CORRECT_L,
	                   box_size=8,
	                   border=4,
	                   )    
	# 添加数据    
	qr.add_data(text)    
	# 生成二维码    
	qr.make(fit=True)    
	img = qr.make_image()    
	img.show() # 简单的生成二维码
def make_code_easy(text):    
	image = qrcode.make(text)    
	image.save(r"C:\python_work")    
	image.show()    
	print("image already save: C:\python_work") 
if __name__ == '__main__':    
	text = input("请输入你想说的话:")    
	make_code(text)









#https://www.jb51.net/article/127033.htm
#https://blog.csdn.net/henni_719/article/details/54580732?locationNum=3&fps=1
# ~ qr = qrcode.QRCode(
  # ~ version=2,
  # ~ error_correction=qrcode.constants.ERROR_CORRECT_H,
  # ~ box_size=10,
  # ~ border=1
# ~ )
# ~ qr.add_data("http://jb51.net/")
# ~ qr.make(fit=True)
 
# ~ img = qr.make_image()
# ~ img = img.convert("RGBA")
 
# ~ icon = Image.open("favicon.png")
 
# ~ img_w, img_h = img.size
# ~ factor = 4
# ~ size_w = int(img_w / factor)
# ~ size_h = int(img_h / factor)
 
# ~ icon_w, icon_h = icon.size
# ~ if icon_w > size_w:
  # ~ icon_w = size_w
# ~ if icon_h > size_h:
  # ~ icon_h = size_h
# ~ icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
 
# ~ w = int((img_w - icon_w) / 2)
# ~ h = int((img_h - icon_h) / 2)
# ~ img.paste(icon, (w, h), icon)
 
# ~ img.save("dhqme_qrcode.png")
