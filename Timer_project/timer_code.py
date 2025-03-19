import time


def timer_watch(seconds):
 while seconds > 0:
    mins , sec = divmod(seconds, 60)
    hour , mins = divmod(mins, 60)
    print(f'{hour:02}:{mins:02}:{sec:02}')
    
    time.sleep(1)
    seconds -= 1
    
 print("Times Up!!")    
 
time_in_sec = int(input("Enter the time in seconds: "))
timer_watch(time_in_sec)
