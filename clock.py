import time

print("This is a simple clock by Piyush Acharya")

hour = int(input("Enter current hour: "))
minute = int(input("Enter current minute: "))
second = int(input("Enter current second: "))

def display():
    print(f"{hour} : {minute} : {second}")

def change():
    global hour
    global minute
    global second

    second = second + 1

    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 24:
        hour = 0

print('\n')

while True:
    time.sleep(1)
    change()
    display()

