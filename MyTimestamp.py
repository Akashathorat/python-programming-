import time
name=input("enter your name:- ")
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
# hour = int(input("enter hour: "))
print(hour)

if(hour>=0 and hour<12):
    print("good morning", name)
elif(hour>=12 and hour<18):
    print("good afternoon", name)
if(hour>=18 and hour<23):
    print("good night", name)

