#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 15:32:56 2020

@author: jbourg
    # used to learn TKiter
"""

import tkinter as tk
import requests
import json

import PIL


#from contextlib import closing
#from urllib.request import urlopen

H = 500*1.4
W = 800*1.5

def get_word(word):
   
   
    app_id  = 'a5010fd3'   #'<a5010fd3>'
    app_key = '682ecae4d3d509965fc7936d19829a62'#'<682ecae4d3d509965fc7936d19829a62>'
    
    language    = 'en-gb'
    word_id     = word
    fields      = 'pronunciations'
    strictMatch = 'false'
    
    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    #print(r.text)
    
    #var = json.dumps(r.json())
    #print(type(var))
    #print("json \n" + json.dumps(r.json()))
    
    Tab =  r.text.split()
    
    Str = ""
    for u in range(len(Tab)):
        Str = Str + '\n'*((u%7)== 0) +Tab[u]
        
    L2['text'] = Str   #+ r.text["lexicalCategory"]
         
    
    
def Response_format(response):
    name = response['name']
    desc = response['weather'][0]['description']    
    wind = str(response['wind']['speed'])
    print(name)
    print(desc)
    print(wind)
    
    final_str = 'name : ' + name + '  description :' + desc + '  wind :' + wind
    
    return final_str
     
root = tk.Tk()

CV = tk.Canvas(root, height = H, width = W)
CV.pack()


bg_image = tk.PhotoImage(file = "Book.png")
bg_label = tk.Label(root, image = bg_image)
bg_label.place(x = 0, y = 0,relwidth = 1, relheight = 1)

FR = tk.Frame(root, bg = 'blue',bd = 5)
FR.place(relx = .5,rely = .05, relwidth = .8, relheight =.15, anchor = 'n')

#CV = tk.Canvas(FR, height = H, width = W, bg = 'blue')
#CV.pack()


E1 = tk.Entry(FR, font = 40)
E1.place(relwidth= .65, relheight = 1) 
E1.config(font=("Times", 14))


B1 = tk.Button(FR, text ="Word meaning (EN)", font = ("Times", 14), command = lambda: get_word(E1.get()))
B1.place(relx = 0.7 , relheight = 1, relwidth = .3)


LFR = tk.Frame(root, bg = 'blue', bd = 10)
LFR.place(relx = .5, rely = .25, relwidth = .8, relheight = .6, anchor = 'n')

L2  = tk.Label(LFR)
L2.place( relwidth = 1, relheight = 1)
L2.config(font=("Times", 14))

#L1 = tk.Label(FR, text ="Hello", bg = 'yellow')
#L1.place(relx = 0.3 , rely = 0,relwidth= .45, relheight = .25)


root.mainloop()








