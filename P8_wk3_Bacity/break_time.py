
import time  
import webbrowser # used to access the browser functions

total_break = 3;
break_count = 0
print("The music has started " + time.ctime()) # time.ctime() displays the current time on the system 
while (break_count < total_break):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=yPB9ENSd1Xc")
    break_count = break_count + 1

