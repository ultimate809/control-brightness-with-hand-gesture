#Shaurya Khurana
#AIT
#Pune
########### open your palm till the webcam for about 3 secs and then close your palm for 3 seconds 
###########                           or vice versa    

import cv2
import numpy as np
import time
import os
import tkinter as tk
from tkinter import *
CAMERA_TYPE=1 													### FOR external camera (usb)
																### 0 for webcam inbuilt

# In[18]:


face_cas=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cas=cv2.CascadeClassifier('haarcascade_eye.xml')
eye_cas2=cv2.CascadeClassifier('eye_cascade.xml')
smile_cas=cv2.CascadeClassifier('smile.xml')
palm_cas=cv2.CascadeClassifier('palm.xml')
open_palm_cas=cv2.CascadeClassifier('open_palm.xml')
closed_palm_cas=cv2.CascadeClassifier('closed_palm.xml')


# In[19]:


open_count=0
closed_count=0
fo=0
fc=0
exit1=0


# In[20]:


cap = cv2.VideoCapture(CAMERA_TYPE)


# In[21]:


def countdown(i):
    label=Label(w, text=str(i))
    label.place(relx=0.45, rely=0.45)
    label.configure(font=("Courier", 40),foreground='blue',background='green')


# In[22]:


w = tk.Tk()
w.geometry("350x350")
label1=Label(w, text="Shaurya ne banaya hai")
label1.place(relx=0.58, rely=0.95)
w.configure(background='red')

w.after(0, lambda: countdown(3) )
w.after(1000, lambda: countdown(2) )
w.after(2000, lambda: countdown(1) )
w.after(3000, lambda: countdown("GO") )
w.after(3200, lambda: w.destroy() )
w.mainloop()


# In[23]:


while True:
    ret,img=cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    open_palm=open_palm_cas.detectMultiScale(gray,1.3,5)                   #open palm detection 
    for  x , y , w, h in open_palm:
        cv2.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0), 2)
    if len(open_palm)>0:
        open_count+=1
        
        
    closed_palm=closed_palm_cas.detectMultiScale(gray,1.3,5)                #closed palm detection 
    for  x , y , w, h in closed_palm:
        cv2.rectangle(img , (x,y) , (x+w,y+h) , (255,0,0), 2)
    if len(closed_palm)>0:
        closed_count+=1
    
    
    if open_count>12 :
        fo=1
        exit1=1
    elif closed_count>12 :
        fc=1
        exit1=1
        
        
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27 or exit1==1:
        break
cap.release()
cv2.destroyAllWindows()


# In[24]:


print(open_count)
print(closed_count)


# In[25]:


open_count=0
closed_count=0
lo=0
lc=0
exit2=0


# In[26]:


time.sleep(1)


# In[27]:


cap = cv2.VideoCapture(CAMERA_TYPE)


# In[28]:


while True:
    ret,img=cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    open_palm=open_palm_cas.detectMultiScale(gray,1.3,5)                   #open palm detection 
    for  x , y , w, h in open_palm:
        cv2.rectangle(img , (x,y) , (x+w,y+h) , (0,255,0), 2)
    if len(open_palm)>0:
        open_count+=1
        
        
    closed_palm=closed_palm_cas.detectMultiScale(gray,1.3,5)                #closed palm detection 
    for  x , y , w, h in closed_palm:
        cv2.rectangle(img , (x,y) , (x+w,y+h) , (255,0,0), 2)
    if len(closed_palm)>0:
        closed_count+=1
    
    
    if open_count>12 :
        lo=1
        exit2=1
    elif closed_count>12 :
        lc=1
        exit2=1
        
        
    cv2.imshow('img',img)
    k=cv2.waitKey(30) & 0xff
    if k==27 or exit2==1:
        break
cap.release()
cv2.destroyAllWindows()


# In[29]:


def contant():
    print("Brightneess remains constant")


# In[30]:


def reduce():
    os.system('xbacklight -dec 40')


# In[31]:


def increase():
    os.system('xbacklight -inc 40')


# In[32]:


if fo==1 and lo==1 :
    constant()
elif fc==1 and lc==1:
    constant()
elif fo==1 and lc==1:
    reduce()
elif fc==1 and lo==1:
    increase()

