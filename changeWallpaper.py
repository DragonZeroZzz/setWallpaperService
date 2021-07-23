import ctypes
import time
import socket
import os
import requests

#client
name = (os.path.basename(__file__)).strip(".py")
ip = socket.gethostbyname(socket.gethostname())
filename = "".join(ip.split("."))+".png"

data = {"data":[name,ip]}

post_url = "https://8c5a661bcfb5.ngrok.io/postData"
get_url = "https://8c5a661bcfb5.ngrok.io/static/wallpapers/"+filename

requests.post(post_url,data=data)

time.sleep(5)
bg_img = requests.get(get_url).content

#open file write and save
file = open("C:\\_TempPhoto\\bg_solid.jpg","wb")
file.write(bg_img)
file.close()

#client
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,"C:\\_TempPhoto\\bg_solid.jpg" , 0)
