import time
seconds = input("ENTER THE NUMBER IN SECONDS ")
def countdowntimer(seconds):
    while seconds > 0:
        mins = int(seconds/60)
        sec = int(seconds % 60)
        timer = f'{mins} : {sec}'
        print(timer) 
        time.sleep(1)
        seconds = seconds-1
    print("TIME IS UP ")

countdowntimer(int(seconds))