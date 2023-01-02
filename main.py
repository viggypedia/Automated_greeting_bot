import time
import pywhatkit as wh


def message1():
    wh.sendwhatmsg_to_group_instantly("Fm8I1scESQQ07Vh1nZpxAM","Good Evening, hope you all had an amazing day!")

def message2():
    wh.sendwhatmsg_to_group_instantly("Fm8I1scESQQ07Vh1nZpxAM","Good Morning Fam!\nWishing you all a great day full of motivation and success.\nCarpe Diem!\n")

    
    
def sending():
    time_now=time.strftime("%H:%M:%S", time.localtime())
    if (str(time_now)=="19:15:00"):
        message1()
    if (str(time_now)=="06:00:00"):
        message2()
            

while True:
    sending()
    
    
