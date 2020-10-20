#!flask/bin/python

import sys
from flask import Flask, render_template, request, redirect, Response
import random, json
import numpy as np
import socket
import re

gcounter = 0
response = "Hello, let's talk!.  "
ip="127.0.0.1"
port=5010
nusers = 1
user = "user"+str(nusers)
historial=[]
ip_address={}

qa = {}

app = Flask(__name__)

def loadDataset(filename):
    f = open(filename,"r")
    lines = f.readlines()
    f.close()
    for line in lines:
        l = line.replace("\n","").split("-;-")

        words = l[0].split(" ")

        w = ""
        for word in words:
            if w == "":
                w += word
            else:
                w += " " + word
            qa[w] = l[1]
           
    return qa

def getAnswer(question):
    global qa
    words = question.split(" ")
    answer = "    R: Sorry, I have not answer for it"
    q = ""
    for word in words:
        q += re.sub('[^A-Za-z0-9 ,]+', '',word)
        try:
            answer = "    R: " + qa[q]
            q += " "
        except:
            pass

    return answer

def getIPAddress():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipaddress = s.getsockname()[0]
    s.close()
    return ipaddress

@app.route('/')
def my_form():
    global response,port, user, nusers
    user = "user"+str(nusers)
    nusers += 1
    return render_template('form2.html', response=response, ip=getIPAddress(), port=str(port), user=str(user), historial=historial)

#@app.route('/receiver', methods=['POST'])
@app.route('/', methods=['POST'])
def my_form_post():
    global gcounter, response, port, user, nusers,qa
    question = request.form['fquestion']
    ruser = request.form['fuser']
    user = ruser
    remote_ip = request.remote_addr
    ip_address[remote_ip] = user

    if question != "":
        gcounter += 1
        print(question)
        answer = getAnswer(question.lower())
        print(answer)
        mrequest = "[" + str(gcounter) + "] "
        mquestion = "<" + user + ">: " + question
        response = mrequest + mquestion + answer
        historial.append([mrequest + mquestion,answer])
        #print(response)
    else:
        response = ""
    return render_template('form2.html', response=response, ip=getIPAddress(), port=str(port), user=str(user), historial=historial)

if __name__ == '__main__':
    filename = "./dataset2.csv"
    lines = loadDataset(filename)
    #print(lines)
    # run!
    app.run(debug=True)



