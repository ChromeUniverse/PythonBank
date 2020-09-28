import os

# printing splash screen

print()
print(" ////////////////////////")
print("   Welcome to BANK INC.  ")
print(" ////////////////////////")
print()

# PATH for database
dbPath = 'C:\\Users\\omnic\\Documents\\Programming\\banking_py\\database.txt'
# PATH for ledger
legderPath = 'C:\\Users\\omnic\\Documents\\Programming\\banking_py\\ledger.txt'
# PATH for app log
logPath = 'C:\\Users\\omnic\\Documents\\Programming\\banking_py\\log.txt'

# opening database and storing contents
dbFile = open(dbPath)
dbContent = dbFile.readlines()
userCount = len(dbContent)-1
dbFile.close()

# implementing a User object

class User(object):
    #initializing a User object
    def __init__(self, id, password, balance=' 0.00'):
        # NOTE: id, password and balance are all STRINGS
        self.id = id
        self.password = password
        self.balance = balance

    # getting UserID
    def get_id(self):
        return self.id

    # getting password
    def get_password(self):
        return self.password

    # getting balance from database
    def get_balance(self):
        id_num = int(self.id)
        # opening database to retrieve balance
        dbFile = open(dbPath)
        dbContent = dbFile.readlines()
        dbFile.close()
        # User's entry in database
        userEntry = dbContent[id_num]
        balance_float = float(userEntry[16:21])
        self.balance = balance_float
        return self.balance

    # updating database with new balance
    def set_balance(self, new_balance):
        id_num = int(self.id)

        # opening database and spliting it into lines
        dbFile = open(dbPath)
        dbLines = dbFile.readlines()
        print(dbLines)
        dbFile.close()

        # accessing User's entry in database
        userEntry = dbLines[id_num]
        print(userEntry)

        # modifying "funds" section in database
        userEntryList = list(userEntry)
        print(userEntryList)
        # too lazy for loops :-P
        userEntryList[16] = list("{:5.2f}".format(new_balance))[0]
        userEntryList[17] = list("{:5.2f}".format(new_balance))[1]
        userEntryList[18] = list("{:5.2f}".format(new_balance))[2]
        userEntryList[19] = list("{:5.2f}".format(new_balance))[3]
        userEntryList[20] = list("{:5.2f}".format(new_balance))[4]
        print(userEntryList)

        # updating database with new User Entry
        userEntry = ''.join(userEntryList)
        dbLines[id_num] = userEntry
        # rejoining database
        print(dbLines[id_num])
        dbNew = ''.join(dbLines)
        print(dbNew)

        # updating the *actual* database.txt file
        dbFile = open(dbPath, 'w')
        dbFile.write(dbNew)
        dbFile.close()

    # authenticate user with the given credentials
    def authenticate(self):
        id_num = int(self.id)
        inputPassword = self.password

        # opening database and reading contents
        dbFile = open(dbPath)
        dbContent = dbFile.readlines()
        dbFile.close()

        if id_num > len(dbContent):
            return False

        userEntry = dbContent[id_num]
        dbPassword = userEntry[6:12]

        if dbPassword == inputPassword:
            return True
        else:
            return False

    # Adding money to balance
    def deposit(self, amount):
        current_balance = float(self.balance)
        new_balance = current_balance + float(amount)
        self.balance = str(new_balance)
        # update database
        print(self.balance)
        self.set_balance(new_balance)
        # update log
        print()

    # Withdraw money from account
    def withdraw(self, amount):
        current_balance = float(self.balance)
        new_balance = current_balance - float(amount)
        self.balance = str(new_balance)
        # update database
        print(self.balance)
        self.set_balance(new_balance)
        # update log
        print()


    # Transfering money from one account tp another
    def transfer(self, other, amount):
        print()
        # update database
        # update log
        # update ledger


def createUser(pass_input):
    # creating a new User entry in the database!
    print("Current number of users: " + str(userCount))
    userCount += 1
    print("Updated number of users: " + str(userCount))
    # UserID for the new user
    newID = str(userCount).zfill(3)
    # editing the database
    dbFile = open(dbPath, 'a')
    dbFile.write(newID + "   " + input_pass + "    " + "00.00" + "\n")
    dbFile.close()

def print_menu1():
    print()
    print("1 - LOGIN")
    print("2 - SIGNUP")
    print("3 - EXIT")
    print()

def print_menu2():
    print()
    print("Login selected")
    print()

def print_menu3():
    print()
    print("Sign-up selected")
    print()

def print_menu4():
    print()
    print("Bye-bye!")
    print()

# main program loop
while True:
    # menu
    print_menu1()

    option1  = int(input("Please select an option: "))

    if option1 == 1:
        # Login selected
        print_menu2()

        id = input("Enter UserID: ")
        password = input("Enter password: ")

        user = User(id, password)

        if user.authenticate() == False:
            print("Please try again.")
        else:
            print("Login successful. Welcome, USER#" + user.get_id())

            # Run main account loop

            while True:
                print()
                print("Select an option:")
                print("1 - DEPOSIT")
                print("2 - WITHDRAW")
                print("3 - TRANSFER")
                print()

                option2 = int(input("Please select an option: "))

                if option2 == 1:
                    print()
                    print("Deposit selected.")
                    print()
                    print("Select an amount to deposit:")
                    amount = float(input())
                    user.deposit(amount)

                if option2 == 2:
                    print()
                    print("Deposit selected.")
                    print()
                    print("Select an amount to deposit:")
                    amount = float(input())
                    user.withdraw(amount)

                if option2 == 3:
                    print()
                    print("Transfer selected.")


    if option1 == 2:
        # Sign-up selected
        print_menu2()

        input_pass = input("Enter your password: ")
        print()

        createUser(input_pass)

        print("Thank you for opening a new account with BANK INC.")
        print("Your UserID is: " + newID)
        print("Your password is: " + input_pass)


    if option1 == 3:
        # Farewell message
        print_menu4()
        break
