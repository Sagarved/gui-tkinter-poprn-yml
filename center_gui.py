#!/usr/bin/python3

import logging
import time
from tkinter import *

import start_container as sc
import device_api as dev

logging.info('Welcome to LoRa In A Box')
root = Tk()
root.title("Welcome to LoRa In A Box") 
root.geometry("1920x1080")
root.configure(background='black')
count_num = 0

font_creator = ('Helvetica', 25,'bold')
#gridFrame = Frame(root, bg='black')

step_text = {"step_1": "System Up", "step_2": "LNS Up", "step_3": "Dashboard", "step": "Device Connected"}
#Creating label for four steps
step_1 = Label(root, text="System Up", bg='yellow', padx=10, pady=10, font=font_creator, height=3, relief= RAISED)
step_2 = Label(root, text="LNS Up", bg='yellow', padx=10, pady=10, font=font_creator, height=3,  relief= RAISED)
step_3 = Label(root, text="LoRa Dashboard", bg='yellow', padx=10, font=font_creator, pady=10, height=3, relief= RAISED)
step_4 = Label(root, text="Devices Connected", bg='yellow', padx=10, font=font_creator, pady=10, height=3, relief= RAISED)

#Data flow Arrow
white_image = PhotoImage(file='/home/wrdlab/white.gif')
green_image = PhotoImage(file='/home/wrdlab/green.gif')
#python_gif_image = PhotoImage(file='/home/wrdlab/gifarrow.gif')
st12_label = Label(root, image=white_image)
st23_label = Label(root, image=white_image)
st34_label = Label(root, image=white_image)

#Arrow positioning row=1
#Even column
st12_label.grid(row=1, column=2)
st23_label.grid(row=1, column=4)
st34_label.grid(row=1, column=6)

#Vertical position of data stores in Row 1 and odd column
step_1.grid(row=1,column=1)
step_2.grid(row=1,column=3)
step_3.grid(row=1,column=5)
step_4.grid(row=1,column=7)

#Central object placement using equal weight to row 1,2, and 3
root.rowconfigure(0,weight=1) 
root.rowconfigure(1,weight=1) 
root.rowconfigure(2,weight=1) 

#Central horizontal placement with the same weightage on all column
#If new steps are added add in column space
root.columnconfigure(1,weight=2) 
root.columnconfigure(3,weight=2) 
root.columnconfigure(5,weight=2) 
root.columnconfigure(7,weight=2)
#Data flow image dynamic width
root.columnconfigure(2,weight=1) 
root.columnconfigure(4,weight=1) 
root.columnconfigure(6,weight=1) 

#color annotation
ready = Label(root, text="Ready", bg='green', padx=25, pady=10).grid(row=9,column=0)
progress = Label(root, text="In Progress", bg='#5f0fff',padx=10, pady= 10).grid(row=10,column=0)#light blue #5f0fff
pending = Label(root, text="Not_Ready", bg='yellow', padx=10, pady=10).grid(row=11,column=0)

def status_check():
    global count_num
    check_dockers = sc.step_2()
    #print(check_dockers)
    if count_num <4:
        step_check=['3000', 'recovserver', 'starting','200'] # 3000 and starting for step1 and step2, third starting is actually healthy, 200 is api response
        step_list = [step_1,step_2,step_3,step_4]
        data_list = [st12_label,st23_label,st34_label]
        if step_check[count_num] in check_dockers and count_num < 2: 
            print(step_check[count_num])
            #Change color and data flow image
            step_list[count_num].configure(bg='green')
            count_num += 1
            step_list[count_num].configure(bg='#5f0fff')
            if count_num > 1:
                data_list[count_num-2].configure(image=green_image)
        elif step_check[count_num] not in check_dockers and count_num==2:
            print(step_check[count_num])
            #Change color and data flow image
            step_list[count_num].configure(bg='green')
            count_num += 1
            step_list[count_num].configure(bg='#5f0fff')
            if count_num > 1:
                data_list[count_num-2].configure(image=green_image)
        elif count_num ==3:
            resp = dev.dev_api()
            #print(resp,devices)

            if '200' in str(resp):
                #Number of devices
                devices = resp[1]
                print(step_check[count_num])
                #Change color and data flow image
                step_list[count_num].configure(text= str(devices)+ ' Devices Connected',bg='green')
                count_num += 1
                if count_num > 1:
                   data_list[count_num-2].configure(image=green_image)
                  
        root.after(3000, status_check)
    
       
       


def ready_check():
        #check if system is ready with both container status Healthy
        check = False
        check = sc.step_2()
        print(check)
        if check:
              ready.configure(text= 'System Ready', bg='green', padx=20, pady=20)
        else:
              ready.configure(text='System not ready, wait for sometime')

"""def basic():
   global count_num
   if count_num > 0:
        step_1.configure(bg='green')
        count_num = 0
   elif count_num == 0:
        step_1.configure(bg='red')
        count_num += 1  
   #After 2 second update status color
   root.after(2000, basic)
"""
if __name__=="__main__":
    #After 1 millisecond call basic

    root.after(1, status_check)
    root.mainloop()

