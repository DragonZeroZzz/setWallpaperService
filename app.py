from flask import Flask, request
from PIL import Image, ImageDraw,ImageFont
import os


app = Flask(__name__)

@app.route('/')
def main_route():
    return 'Main Hello'

@app.route('/postData',methods=["POST"])
def post_data():
    data = request.get_data()
    data =data.decode("utf-8").split("&")
    name = data[0].strip("data=")
    ip = data[1].strip("data=")
    fnt = ImageFont.truetype("/static/Fonts/DejaVuSans.ttf",30) 
    filename = ""
    filename = filename.join(ip.split("."))
    image = Image.new('RGB',(1920,1080),(191,209,229))
    d = ImageDraw.Draw(image)
    d.text((1350,100),"IP Adress : {}".format(ip),font=fnt,fill=(0,0,0))
    d.text((1350,140),"Bot name : {}".format(name),font=fnt,fill=(0,0,0))
    image.save(os.path.join("./static/wallpapers",filename+".png"))
    return 'Data recieved'


if __name__=="__main__":
    app.run(debug=True, host= "0.0.0.0")