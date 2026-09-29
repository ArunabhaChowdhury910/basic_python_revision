import csv
from State.state import state
class main(state) :
    def user(self):
        
        a=input("Do you have Acount!!type Y/N for yes and no :")
        if a=='Y':
            #after creating state it will ask for which account current or savings 
            b=input("which account details DO You Want to see [C/S] for current and Saving : ")
            if b=='C':
                #directed to the current function
                print("directed to the current function..")
            elif b=='S':
                #directed to the savings
                print("directed to the savings...")
            else :
                print("Invalid!!")

        elif a=="N":
            print("Lets Sign in!!")
            username=input("craete your Username:")
            passward = input("create your passward:")
            print("Wvhich Account do you want")
            print("1. Savings!!")
            print("2. Current!!")
            print("3. Both!!")
            choose=int(input("enter OPtion :"))
            while(1):
             
                if choose== 1:
                    sav=float(input("enter the ammount (minimum balance is 150/-) :"))
                    if sav >= 150:
                        with open("database.csv","a",newline="")as file:
                                writer= csv.writer(file)

                                writer.writerow([username,passward,sav,0])
                                #directed to the login 
                        print("Your account has been created successfully !!!")
                        break

                    else:
                            print("pls enter the amt more than 150/-")

                elif choose == 2:
                    curr=float(input("enter the ammount (minimum balance is 250/-) :"))
                    if curr >= 250:
                        with open("database.csv","a",newline="")as file:
                            writer= csv.writer(file)

                        writer.writerow([username,passward,0,curr])
                        #directed to the login 
                        print("Your account has been created successfully !!!")
                        break

                    else:
                        print("pls enter the amt more than 150/-")

                elif choose==3:
                    sav=float(input("enter the ammount for savings  (minimum balance is 150/-) :"))
                    curr=float(input("enter the ammount for curret  (minimum balance is 250/-) :"))

                    if sav>=150 and curr>=250:
                        with open("database.csv","a",newline="")as f:

                            write=csv.writer(f)
                            write.writerow([username,passward,sav,curr])

                        print("Your account has been created successfully !!!")

                        break

                    else:
                        print("pls check the amount you enter is below minimum limit...")

                else:
                    print("Invalid option .....")