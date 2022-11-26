'''
Piece of code using which I download the images for my dataset from given links.
'''
import os
import requests
from bs4 import BeautifulSoup
import random


urls = [
"https://www.google.com/search?q=acer+tree&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi585TSzLT3AhXSPOwKHeEoB8UQ_AUoAXoECAMQAw&biw=1536&bih=731&dpr=1.25",  #acer
"https://www.google.com/search?q=olympic+swimming+pool&tbm=isch&ved=2ahUKEwiu4KKVzbT3AhVOwgIHHef2BGsQ2-cCegQIABAA&oq=olymswimming+pool&gs_lcp=CgNpbWcQARgAMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB46BAgAEEM6BQgAEIAEUMYPWMkTYL8eaABwAHgAgAFLiAHtApIBATWYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=LmdpYq6RDM6Ei-gP5-2T2AY&bih=731&biw=1536",  #pool
"https://www.google.com/search?q=lilek&hl=cs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjY9YDhz7T3AhWlOOwKHWqTCuIQ_AUoAXoECAIQAw&biw=1536&bih=731&dpr=1.25#imgrc=mhGmNdIuN4vYgM",  # lilek
"https://www.google.com/search?q=tule%C5%88&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj37MCP07T3AhWH2aQKHdvTBb8Q_AUoAXoECAIQAw&biw=1536&bih=674&dpr=1.25", #tulen
"https://www.google.com/search?q=dobromysl+obecn%C3%A1&tbm=isch&ved=2ahUKEwia486v07T3AhVQDOwKHTInBtIQ2-cCegQIABAA&oq=dobromy&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoECAAQQzoGCAAQBxAeOgQIABAeOggIABCABBCxAzoHCAAQsQMQQzoICAAQsQMQgwE6CwgAEIAEELEDEIMBUMQFWInEBmD20wZoAHAAeACAAd0BiAGKDJIBBjE5LjAuMZgBAKABAaoBC2d3cy13aXotaW1nsAEAwAEB&sclient=img&ei=sG1pYprLA9CYsAeyzpiQDQ&bih=674&biw=1519&hl=cs" # dobromysel
]

index = 1
curls = []
classes = ["acer", "pool", "lilek", "tulen", "dobromysl"]
# my dataset contains 5 classes of following numbers of images 
# acer - 69 images
# dobromysl - 77 images
# lilek - 78 images
# pool - 70 images
# tulen - 76 images

i = 0
for url in urls:
    page = requests.get(url).text
    soup = BeautifulSoup(page, features="html.parser")
    for img in soup.find_all("img")[:30]:
        curls.append(("curl " + img.attrs['src'][:-2] + " > ", classes[i]))
    i += 1

random.shuffle(curls)

for curl in curls:
    os.system(curl[0] + "./database/" + str(curl[1]) + str(index).zfill(3) + ".png")
    index += 1
