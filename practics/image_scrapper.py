from flask import Flask , render_template ,request ,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautyfulSoup 
from urllib.request import urlopen
import logging
import os
import pymongo

logging.basicConfig(filename= "Scrapper2.log" , level=logging.INFO)


app =Flask(__name__)

@app.route('/' , methods = ['GET'])
def home_page():
    return render_template("index2.html")


@pp.route('review' , methods = ['POST' , 'GET'])
def index():
    if request.method=='POST':
        try:

            query = request.form['content']

            save_dir = "image2/"

            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

            response =request.get(f"https://www.google.com/search?q={query}&tbm=isch&ved=2ahUKEwjZ2_2elPT9AhVjoNgFHTrrBaMQ2-cCegQIABAA&oq=ro&gs_lcp=CgNpbWcQARgAMgQIIxAnMgcIABCKBRBDMggIABCxAxCDATIICAAQsQMQgwEyCAgAEIAEELEDMgUIABCABDIICAAQgAQQsQMyCAgAELEDEIMBMgsIABCABBCxAxCDATIICAAQsQMQgwE6BwgjEOoCECc6BAgAEANQygVYlBlg_CFoAXAAeASAAdwBiAHUCpIBBTAuOC4xmAEAoAEBqgELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=pGAdZNn5A-PA4t4PutaXmAo&bih=601&biw=1280&rlz=1C1ONGR_enIN1046IN1046")

            image_html = BeautyfulSoup(response.content, "html.parser")

            image_tag = image_html.find_all['img']

            del image_tag[0]

            mongo_data = []

            for i in image_tag:
                image_url = image_tag['src']
                image_data = request.get(image_url).content
                mydict = {"index" : image_url , "image " : image_data}
                mongo_data.append(mydict)

                with open(os.path.join(save_dir , f"{query}_.jpg"), "wb") as f :
                    f.write(image_data)


        except Exception as q :
            logging.info(q)
            return 'something is wrong'

    
    
    
    
    
    
    else:
        return render_template("index2.html")


if __name__=='__main__':
    app.run(host='0.0.0.0' ,port=8000)
