import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Harman:Mongo123@cluster0.ivfl1.mongodb.net/myStudentLambton?retryWrites"
                               "=true&w=majority")
db = myclient.test

database = myclient['myStudentLambton']
collection = database['studentRecord']



print(database.list_collection_names())
x = 1
while x != 5:
    print("Press 1 to insert data into DB")
    print("Press 2 to update the record ")
    print("Press 3 to display all the record in the database")
    print("Press 4 to delete the record")
    print("Press 5 to Exit")
    x = int(input("Enter your choice .. "))
    if x == 1:
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
    elif x == 2:
        sid = input("Enter the student ID whose information you want to update")
        attribute = input("Please enter what you want to update. we can update - FirstName , LastName , GPA, Course")
        value = input("Enter the new value ")
        myquery = {"SID": sid}
        newvalues = {"$set": {attribute: value}}

        collection.update_one(myquery, newvalues)
        print("Record updated successfully .. !!")
        # print "students" after the update:
        for x in collection.find():
            print(x)

    elif x == 3:
        for x in collection.find():
            print(x)
    elif x == 4:
        sid = input("Enter the student Id whose record you want to delete")
        myquery = {"SID": sid}
        collection.delete_one(myquery)
        print("Record deleted successfully .. !! ")
print("Thank you for using School Database Management System.. !! ")
