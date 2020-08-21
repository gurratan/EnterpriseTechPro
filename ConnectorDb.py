import pymongo
import Read
import Insert
import Update
import Delete
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
        Insert.insertRecord(collection)
    elif x == 2:
        Update.updateRecord(collection)
    elif x == 3:
        Read.readCollection(collection)
    elif x == 4:
        Delete.deleteRecord(collection)
print("Thank you for using School Database Management System.. !! ")
