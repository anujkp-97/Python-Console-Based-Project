from crud import Database


def main():
    db = Database()
    while True:
        print("**********--WELCOME--***********")
        print()
        print("Press 1 for insert new user(userId, name, phone)")
        print("Press 2 for fetch all user")
        print("Press 3 for delete the user(userId)")
        print("Press 4 for update user(userName, phone) details")
        print("Press 5 to exit() program")
        print()
        try:
            choice = int(input())
            if(choice==1):
                uid = int(input("Enter user id: "))
                userName = input("Enter user name: ")
                phone = input("Enter user phone: ")
                db.insert_data(uid, userName, phone)
               
            elif(choice ==2):
               
                db.get_data()
                
            elif(choice ==3):
                uid = int(input("Enter user id to delete: "))
                db.delete_user(uid)
               
            elif(choice ==4):
                uid = int(input("Enter user id to update: "))
                newName = input("New name: ")
                newPhone = input("New phone: ")
                db.update(uid,newName, newPhone)
               
            elif(choice ==5):
                break
            else:
                print("Invalid details, Try again!")
        except Exception as e:
            print(e)
            print("Invalid details, Try again!")


if __name__ == "__main__":
    main()
