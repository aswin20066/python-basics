from azwin import*

print("Welcome to Student Management !!")

while True:
    print("You can perform thhe following process !!")
    print("1.Registeration\n2.View student\n3.Update Student\n4.Delete student")
    print("5.Exit")
    choice=input("Enter your choice[1,2,3,4,5] : ")
    if choice=="1":
        print("you choose student Registeration !!")
        register()
    elif choice=="2":
        print("you choose view student !!")
        view()
    elif choice=="3":
        print("you choose Update student !!")
        update()
    elif choice=="4":
        print("you choose Delete student !!")
        delete()
    elif choice=="5":
        print("Thanks for using the App !!")
        exit()
    else:
        print("Invalid inputs !!!")
        
    cont=input("Do You Want To Continue[y/n] :") 
    if cont=="y":
        continue
    else:
        print("Thanks for Using this Applicaton")
        exit()
        