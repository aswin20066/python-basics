from win import read_json,write_json
from tabulate import tabulate
def register():
    data=read_json()
    stud_dict={
        "Sno":len(data["students"])+1,
        "Name":input("Enter student Name :"),
        "Age":input("Enter student Age :"),
        "Address":input("Enter student Address:"),
        "course":input("Enter student course :"),
        "Duration":input("Enter course Duration :")
    }
    data["students"].append(stud_dict)
    write_json(data)
    print(f"{stud_dict["Name"]} Registeration is completed !!")
    

def view():
    data=read_json()
    # print("Sno\tName\tAge\tAddress\tCourse\tDuration")
    # for stud in data["student"]:
    #     print(f"{stud['Sno']}\t{stud['Name']}\t{stud['Age']}\t{stud['Address']}\t{stud['course']}\t{stud['Duration']}")
    table=[]
    for stud in data["students"]:
        row=[stud["Sno"],stud["Name"],stud["Age"],stud["Address"],stud["course"],stud["Duration"]]
        table.append(row)
    print(tabulate(table,headers=["Sno","Name","Age","Address","Course","Duration"],tablefmt="rounded_grid"))
def update():
    view()
    data=read_json()
    sno=input("Enter sno of student you want to update :")
    name=""
    print("1.Name\n2.Age\n3.Adderess\n4.Course\n5.Duration")
    option=input("Enter your update option[1,2,3,4,5] :")
    for stud in data["students"]:
        if str(stud["Sno"])==sno:
            name=stud["Name"]
            
            
            if option=="1":
                mod=input("Enter student updated name :")
                stud["Name"]=mod
            elif option=="2":
                mod=input("Enter student updated Age :")
                stud["Age"]=mod
            elif option=="3":
                mod=("Enter student changed Address : ")
                stud["Address"]=mod
            elif option=="4":
                mod=input("Enter student updated Course :")
                stud["course"]=mod
            elif option=="5":
                mod=input("Enter student  updated Duration :")
                stud["Duration"]=mod
            else:
                print(" Invalid Option !!!")
            break
    
    if name!="":
        print(f"{name} was updated successfully!!")
        write_json(data)
    else:
        print(f"{sno} is not present")
        

def delete():
    view()
    data=read_json()
    sno=input("Enter sno of student you want to delete :")
    name=""
    for stud in data["students"]:
        if str(stud["Sno"])==sno:
            name=stud["Name"]
            data["students"].remove(stud)
            break
    sno1=1
    for stud in data["students"]:
        stud["Sno"]=sno1
        sno1+=1
    if name!="":
        print(f"{name} deleted suceessfully")
        write_json(data)
    else:
        print(f"{sno} is not present")
            