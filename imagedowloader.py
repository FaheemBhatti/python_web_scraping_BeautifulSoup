import requests
from bs4 import BeautifulSoup
import os 
from PIL import Image 
from subprocess import Popen, PIPE

#url = "https://www.heisig.com/aktuelle-auftraege"

def imagedown(url, folder):

    if not os.path.exists(os.path.join(os.getcwd() , folder)):
        os.makedirs(os.path.join(os.getcwd() , folder))

    name = '' 
    link = ''

    r = requests.get(url)
    soup = BeautifulSoup(r.text , 'html.parser')

    images = soup.select('div.AnfrageZG > a')

    for image in images:
        link = image['href']
        image_name = image['href'].split("/", 2)[2]
        img_response = requests.get('https://www.heisig.com/'+link, stream = True)
        img = Image.open(img_response.raw)
        img.save(image_name)
        print(img)       

imagedown('https://www.heisig.com/aktuelle-auftraege' , 'img')
        

            
