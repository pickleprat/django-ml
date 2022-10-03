#author: AM0307
from django.shortcuts import render
from django.http import HttpResponse
import os 
import requests as r 
import string
import pickle
import numpy as np 


def filter(chars: str) : 
    for ch in string.punctuation: 
        if ch in chars: 
            chars = chars.replace(ch, '')
    return chars

def death_or_not(derive): 
    if derive == 2: return "Unfortunately, the world has to bear you a little longer. You don't have cancer."
    else: return "Congratulations!!! You're dying!!!"

def display_one(request): 
    with open("TextUtils/one.txt", "rt") as f: 
        string = f.read()
    return HttpResponse(f"<b>{string}</b>")

def get_facebook(request): 
    string = r.get('https://www.facebook.com').text
    return HttpResponse(string)

def get_google(request): 
    string = r.get('https://www.google.com').text
    return HttpResponse(string)

def watch_porn(request): 
    string = r.get('https://www.pornhub.com').text
    return HttpResponse(string)

def back(request):
    string = '<a href="http://127.0.0.1:8000/">Back</a>'
    return HttpResponse(string)

def get_base(request): 
    chars = request.GET.get("text")
    if(chars):
        chars = filter(chars)
        diction = {
            "names":chars, 
        }
        return render(request, "index.html", diction)
    else: return render(request, "index.html")


def post_data(request):
   
    with open('classifier.pickle', 'rb') as file1: 
        clf = pickle.load(file1)
    try:
        data_provided = [
            int(request.GET.get('thickness_clump')), 
            int(request.GET.get('cell_size_uniformity')),
            int(request.GET.get('cell_shape')),
            int(request.GET.get('rate_marginal_adhesion')),
            int(request.GET.get('epithelial_cell')),
            int(request.GET.get('bare_nuclei')),
            int(request.GET.get('bland_chromatin')),
            int(request.GET.get('normal_nuclei')),
            int(request.GET.get('mitosis'))        
        ]
        
    except Exception as e:
        return render(request, 'breastcancer.html')
    if(any(data >10 or data <0 for data in data_provided)):
        return render(request, 'breastcancer.html')
    else: 
        arr = np.array(data_provided).reshape((1, 9))
        prediction = clf.predict(arr)
        determine = death_or_not(prediction[0])
        data = {
            "prediction":determine
        }
        return render(request, "breastcancer.html", data)
        
    

    