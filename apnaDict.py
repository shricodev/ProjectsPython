
userInput = input("What do you wanna search:\n")
low = userInput.lower()
# print(low)
'''In a dictionary itself we can make another dictionary'''

'''We can add anything to a dictionary by 
diction["Test"] = "test" 
'''

diction = {
    "name" : "piyush",
    "sets" : "Sets are used to store multiple items in a single variable.",
    "dictionary" : "Dictionaries are used to store data values in key:value pairs.",
    "tuple" : "Tuples are used to store multiple items in a single variable.",
    "piyushfeed" : {
        "breakfast" : "Python",
        "lunch" : "Java",
        "dinner": "C++"
        }
}

if low in diction and low != "piyushfeed":
    print(f"Your search for {low}'s output is:\n{diction[low]}")
elif low == "piyushfeed":
    userInput2 = input("What do you want to see breakfast, lunch, or dinner:\n")
    low2 = userInput2.lower()
    print(f"piyush eats {diction[low][low2]} in {low2}\U0001F923 .")
else:
    print(f"Your given data {low} is not found in our dictionary")