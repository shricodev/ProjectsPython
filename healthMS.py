
client_list = {
    1 : "Piyush",
    2 : "Harry",
    3 : "Peshal",
    4 : "Suyash",
}

log_list = {
    1 : "Exercise",
    2 : "Diet"
}

def gettime():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Client Name: ")
    for key, value in client_list.items():
        # print(client_list.items())
        print("Press", key, "for", value, "\n", end = "")
    client_name = int(input())

    print("Selected Client: ", client_list[client_name], "\n", end= "")

    print("Press 1 for log")
    print("Press 2 for retrieve")

    op = int(input())

    if op is 1:
        for key, value in log_list.items():
            print("Press", key, "to log",value, "\n", end ="")
        log_name = int(input())
        print("Selected Job: ", log_list[log_name])
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
        k = "y"
        while k is not "n":
            print("Enter", log_list[log_name], "\n", end = "")
            mytext = input()
            f.write("[" + str(gettime()) + "]: " + mytext + "\n")
            k = input("Add more? y/n: ")
            continue
        f.close()

    elif op is 2:
        for key, value in log_list.items():
            print("Press", key, "to retrieve", value, "\n", end= "")
        log_name = int(input())
        print(client_list[client_name], "-", log_list[log_name], "Report:", "\n", end = "")
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input")

except Exception as e:
    print("Wrong Input")

