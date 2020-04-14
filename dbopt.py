from pymongo import MongoClient
def main():

    while (1):
        # chossing option to do CRUD operations
        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')

        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        else:
            print('\n INVALID SELECTION \n')
def makeConnection():
    client = MongoClient('localhost:27017')
    db = client.EmployeeData
    return db
def insert():
    db = makeConnection()
    try:
        employeeId = int(input('Enter Employee id :'))
        employeeName = input('Enter Name :')
        employeeAge = int(input('Enter age :'))
        employeeCountry = input('Enter Country :')
        db.Employees.insert_one({

            "id": employeeId,
            "name": employeeName,
            "age": employeeAge,
            "country": employeeCountry
        })
        print('\nInserted data successfully\n')

    except Exception as e:
        print(str(e))

def update():
    pass
def read():
    db = makeConnection()
    try:
        empCol = db.Employees.find()
        print('\n All data from EmployeeData Database \n')
        for emp in empCol:
            print(emp)

    except Exception as e:
        print(str(e))
def delete():
    pass

if __name__ == '__main__':
    main()