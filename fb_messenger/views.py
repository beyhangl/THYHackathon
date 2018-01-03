# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import unicodedata
import urllib2
import time
import glob
import os
from PIL import Image

# yomamabot/fb_yomamabot/views.

from django.views import generic

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json,requests, random, re
from pprint import pprint
from django.utils.decorators import method_decorator
import sqltest as sqlop
from fbmq import Page
import fbmq
from fbmq import Attachment, Template, QuickReply, Page
def post_facebook_message(fbid, recevied_message):           

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAXTQIyKBiwBAI6kqZCGufDexs3kzHHOunEqJcwhMlQMwJyIGcGnYlCzpxbNVAtJaQdAatBbtwMDOZAaFJuwNGTIFWH6ZAg8mSkZBx8jH20c3R3PXbdvHcodjGIGLxbpNZBhLQrLDbiY9nFmJqDZBanNhyo4DS9CHsSCokpD7z1QZDZD' 

    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})

    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())



# Create your views here.
class YoMamaBotView(generic.View):
    page = fbmq.Page('EAAXTQIyKBiwBAMnl26FWLW7T6ZBCsD3TFPRcRxIaYU4YkMjrKosWZBwXDyLZBRzWfIXZCvWLLZCGF8bqixLDKXm8mFA7SNSbJjTfnagkDmeZBLM6ZA9yTDD5RRjTbcoRQWexH0qcnNM8ZAsFrUs3oQxgbtAJYlHaFZCS88cr1d90pawZDZD')
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '2318934571':
            print('verify is ok')
            return HttpResponse(self.request.GET['hub.challenge'])

        else:

            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):

        # Converts the text payload into a python dictionary
        page = fbmq.Page('EAAXTQIyKBiwBAMnl26FWLW7T6ZBCsD3TFPRcRxIaYU4YkMjrKosWZBwXDyLZBRzWfIXZCvWLLZCGF8bqixLDKXm8mFA7SNSbJjTfnagkDmeZBLM6ZA9yTDD5RRjTbcoRQWexH0qcnNM8ZAsFrUs3oQxgbtAJYlHaFZCS88cr1d90pawZDZD')

        incoming_message = json.loads(self.request.body.decode('utf-8'))
        #pprint(incoming_message)
        #print(str(incoming_message)+ ' +++++')
        try:
 
         img_url=incoming_message['entry'][0]['messaging'][0]['message']['attachments'][0]['payload']['url']        # Facebook recommends going through every entry since t      #page = fbmq.Page('EAAXTQIyKBiwBAMnl26FWLW7T6ZBCsD3TFPRcRxIaYU4YkMjrKosWZBwXDyLZBRzWfIXZCvWLLZCGF8bqixLDKXm8mFA7SNSbJjTfnagkDmeZBLM6ZA9yTDD5RRjTbcoRQWexH0qcnNM8ZAsFrUs3oQxgbtAJYlHaFZCS88cr1d90pawZDZ        #page.send('1488848524485107', "hello wor        img_url=incoming_message['entry'][0]['messaging'][0]['message']['attachments'][0]['payload']['url']
         pprint(img_url)
         img = urllib2.urlopen(img_url)
         localFile = open('/home/kafein/thy_hackathon/images/deeesktop.jpg', 'wb')
         localFile.write(img.read())
         localFile.close()
         pprint('testttttt')
         time.sleep(5)
         list_of_files = glob.glob('/home/kafein/thy_hackathon/check-in/*') # * means all if need specific format then *.csv
	 pprint('heyooooo')
         latest_file = max(list_of_files, key=os.path.getctime)
         image_url=latest_file
         recipient_id=incoming_message['entry'][0]['id']
         pprint(recipient_id)
         pprint(image_url)
         im = Image.open(str(image_url))
	 dosya_adi=im.filename
	 pprint(dosya_adi)
	 pprint(str(dosya_adi).split('check-in/')[1].split('.jpg')[0])
	 dosya_adi=str(dosya_adi).split('check-in/')[1].split('.jpg')[0]
         cumle='Sayin '+str(str(dosya_adi).split('_')[1])+' kimlik numarali '+str(dosya_adi.split('.')[0])+' ' + str(dosya_adi.split('.')[1].split('_')[0]) + ' ' +str(dosya_adi.split('_')[2]) +' ucaginizda koltuk numaraniz '+ str(dosya_adi.split('_')[3])+ ' olarak ayarlanmistir. Iyi Yolculuklar Dileriz!'      
	 pprint(cumle)           	    
	 page.send('1488848524485107', str(cumle))
        except:
          pass
        
                    # Print the message to the terminal
                    #print(message['message']+ ' ++++ message text')  
        try:
                     pprint('TETE')
                     
        except:
                     pprint('Kayit olmadi')
                     post_facebook_message(message['sender']['id'],'Üzgünüm sizi anlayamadım')
        return HttpResponse()

