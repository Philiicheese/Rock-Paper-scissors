#RPS


import time
import random


print("Choose Rock, Paper, or Scissors")
hand = input()

def countdown(t):
    while t :
 #       mins = t // 60
        secs = t % 60
        timer = '{:2d}'.format(secs)
        print(timer, end="\r")
        time.sleep(1)        
        t -= 1
    print("Shoot!!!")
t = int(3)

countdown(int(t))

print("Self: " + hand)

items = ['Rock',"Paper",'Scissors']

op = random.choice(items)
print("Computer: " + op)

if hand == "Rock":
    if op == "Rock":
        print("Tie!")
    if op =="Paper":
        print("Computer Wins!")
    if op == "Scissors": 
        print("You Wins!")   
if hand == "Paper":
    if op == "Rock":
        print("You Wins!")
    if op =="Paper":
        print("Tie!")
    if op == "Scissors": 
        print("Computer Wins!")   
if hand == "Scissors":
    if op == "Rock":
        print("Computer Wins!")
    if op =="Paper":
        print("You Wins!")
    if op == "Scissors": 
        print("Tie!")   
    