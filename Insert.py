def insertRecord(collection):
    sid = input("Enter student ID : ")
    firstName = input("Enter Student First Name : ")
    lastName = input("Enter student Last Name : ")
    GPA = input("Enter GPA : ")
    course = input("Enter student course name : ")
    coop = input("Is student eligible for coop : ")

    mystudent = {
        "SID": sid,
        "FirstName": firstName,
        "LastName": lastName,
        "GPA": GPA,
        "Course": course,
        "Co-op": coop
    }

    x = collection.insert_one(mystudent)
    print(x)
    print("Record entered successfully  user can check the record by pressing 3 ")