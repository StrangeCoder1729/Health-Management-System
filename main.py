def getdate():
    import datetime
    return datetime.datetime.now()
 


def Harry():
    print("Which Section :-")
    print("(1) Exercises")
    print("(2) Diet")
    time_1 = getdate()
    user_harry = int(input("Enter (Serial number) : "))

    if(user_harry == 1):
        with open("1_harry_exercise.txt","a") as f:
            harry_input_0 = input("["+str(time_1)+"] : "+"")
            f.write("["+str(time_1)+"] : " + harry_input_0 + "\n")
        print("Successfully documented !!")

    elif(user_harry == 2):
        with open("1_harry_diet.txt","a") as f:
            harry_input_1 = input("["+str(time_1)+"] : "+"")
            f.write("["+str(time_1)+"] : " + harry_input_1 + "\n")
        print("Successfully documented !!")



def Rohan():
    print("Which Section :-")
    print("(1) Exercises")
    print("(2) Diet")
    time_1 = getdate()
    user_Rohan = int(input("Enter (Serial number) : "))

    if(user_Rohan == 1):
        with open("1_Rohan_exercise.txt","a") as f:
            Rohan_input_0 = input("["+str(time_1)+"] : "+"")
            f.write("["+str(time_1)+"] : " + Rohan_input_0 + "\n")
        print("Successfully documented !!")

    elif(user_Rohan == 2):
        with open("1_Rohan_diet.txt","a") as f:
            Rohan_input_1 = input("["+str(time_1)+"] : "+"")
            f.write("["+str(time_1)+"] : " + Rohan_input_1 + "\n")
        print("Successfully documented !!")

def Hammad():
    print("Which Section :-")
    print("(1) Exercises")
    print("(2) Diet")
    time_1 = getdate()
    user_Hammad = int(input("Enter (Serial number) : "))

    if(user_Hammad == 1):
        with open("1_Hammad_exercise.txt","a") as f:
            Hammad_input_0 = input("["+str(time_1)+"] : "+"")
            f.write("["+str(time_1)+"] : " + Hammad_input_0 + "\n")
        print("Successfully documented !!")

    elif(user_Hammad == 2):
        with open("1_Hammad_diet.txt","a") as f:
            Hammad_input_1 = input("["+str(time_1)+"] : "+"")
            f.write("["+str(time_1)+"] : " + Hammad_input_1 + "\n")
        print("Successfully documented !!")

def Harry_hist():
    print("Which Section do you want to look into :-")
    print("(1) Exercises")
    print("(2) Diet")
    user_harry_log = int(input("Enter (Serial Number): "))
    if(user_harry_log == 1):
        with open("1_harry_exercise.txt","rt") as f:
            print(f.read())
    elif(user_harry_log == 2):
        with open("1_harry_diet.txt","rt") as f:
            print(f.read())

def Rohan_hist():
    print("Which Section do you want to look into :-")
    print("(1) Exercises")
    print("(2) Diet")
    user_Rohan_log = int(input("Enter (Serial Number): "))
    if(user_Rohan_log == 1):
        with open("2_Rohan_exercise.txt","rt") as f:
            print(f.read())
    elif(user_Rohan_log == 2):
        with open("2_Rohan_diet.txt","rt") as f:
            print(f.read())

def Hammad_hist():
    print("Which Section do you want to look into :-")
    print("(1) Exercises")
    print("(2) Diet")
    user_Hammad_log = int(input("Enter (Serial Number): "))
    if(user_Hammad_log == 1):
        with open("3_Hammad_exercise.txt","rt") as f:
            print(f.read())
    elif(user_Hammad_log == 2):
        with open("3_Hammad_diet.txt","rt") as f:
            print(f.read())

c = getdate()
print("["+str(c)+"]")

print("\t\t\t\tHealth Management System")


print("What are you going to do ?")
print("(1) Documenting")
print("(2) Seeing history")
user_option = int(input("Enter (Serial Number) : "))
 
if(user_option == 1):
    try:
        print("3 People :-")
        print("(1) Harry")
        print("(2) Rohan")
        print("(3) Hammad")
        user = int(input("Enter (Serial Number) : "))
    
        if(user == 1):
            Harry()
        elif(user ==2):
            Rohan()
        elif(user == 3):
            Hammad()
        else:
            print("Wrong Input !!!")

    except Exception as e:
        print("Invalid Input")

elif(user_option == 2):
    print("Patient's Logs :-")
    print("(1) Harry")
    print("(2) Rohan")
    print("(3) Hammad")
    try:
        user_input_hist = int(input("Of whom do you want to see the history of : "))
        if(user_input_hist == 1):
            Harry_hist()
        elif(user_input_hist == 2):
            Rohan_hist()
        elif(user_input_hist == 3):
            Hammad_hist()
    except Exception as e:
        print("Invalid Input")



