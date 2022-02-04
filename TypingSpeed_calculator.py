from time import *
import random as r

def mistake(para,user):
        error = 0
        for i in range(len(para)):
                try:
                        if para[i]!=user[i]:
                                error = error + 1
                except:
                        error = error+1
        return error

def typing_speed(time_s,time_e,user):
        time_delay = time_e - time_s
        time_round = round(time_delay,2)
        speed = len(user)/time_round
        return round(speed)
if __name__ == "__main__":
        while True:
                ck = input(" Are you ready : yes/no :")
                if ck =="yes".lower():
                        test = ["One morning a carpenter was sawing a log of wood under a tree.",
                                " He was wearing a bright blue shirt.",
                                " The carpenter wanted to cut the log into two parts."]
                        test1 = r.choice(test)
                        print("         ************ Typing * Speed ***********         ")
                        print(test1)
                        print()
                        print()
                        time_1 = time()
                        testinput = input("Enter :")
                        time_2 = time()

                        print("Speed :", typing_speed(time_1,time_2,testinput)," w/sec")
                        print("Error :", mistake(test1,testinput))
                elif ck =="no".lower():
                        print("Be ready next time")
                        break
                else:
                        print("Wrong input")
