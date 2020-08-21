def updateRecord(collection):
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