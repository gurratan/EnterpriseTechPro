def deleteRecord(collection):
    sid = input("Enter the student Id whose record you want to delete")
    myquery = {"SID": sid}
    collection.delete_one(myquery)
    print("Record deleted successfully .. !! ")