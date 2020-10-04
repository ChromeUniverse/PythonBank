import os
import csv
import datetime


# printing splash screen
print()
print(" ////////////////////////")
print("   Welcome to BANK INC.  ")
print(" ////////////////////////")
print()

# initializing 'bank_files' directory and DB, ledger and log files

folder_name = 'bank_files'

if os.path.exists(os.path.join('.', folder_name)) == False:
    os.makedirs(os.path.join('.', folder_name))

# changes CWD to .\bank_files
os.chdir(os.path.join('.', folder_name))

# initializing files with the appropriate headers
def file_init(filename):
    file = open(filename, 'wb')
    file.close()

# checking if files exist - if not, we create & init them
def file_check(filename):
    if not os.path.exists(filename):
        file = open(filename,'w+')
        file_init(filename)
        file.close()

# PATH to database
dbPath = 'database.csv'
# PATH to ledger
ledgerPath = 'ledger.csv'
# PATH to log
logPath = 'log.csv'

# making sure we have our files ready
file_check(dbPath)
file_check(ledgerPath)
file_check(logPath)

# opening database and storing contents
dbFile = open(dbPath)
# Getting number of registered users
userCount = len(dbFile.readlines())-1
dbFile.close()

# implementing a User object

class User(object):
    #initializing a User object
    def __init__(self, name, password=None, id='000', balance=0.0):
        # NOTE: id, password and balance are all STRINGS
        self.name = name
        self.password = password
        self.id = id
        self.balance = balance

    def get_id(self):
        # opening database and retrieving user balance
        dbFile = open(dbPath)
        dbReader = csv.reader(dbFile)
        # iterating through CSV file (linear search)
        for row in dbReader:
            # username found in DB!
            if row[0] == self.name:
                self.id = row[2]
                dbFile.close()
                return row[2]
        # if we didn't find username, then user isn't registered in the DB
        dbFile.close()
        return False

    # getting password
    def get_password(self):
        return self.password

    # getting balance from database
    def get_balance(self):
        # opening database and retrieving user balance
        dbFile = open(dbPath)
        dbReader = csv.reader(dbFile)

        id_num = int(self.id)
        balance = list(dbReader)[id_num-1][3]
        dbFile.close()
        self.balance = float(balance)
        return self.balance

    # updating database with new balance
    def set_balance(self, new_balance):
        # Updating the User object's 'balance' data attribute
        self.balance = new_balance
        id_num = self.id

        # opening database and spliting it into lines
        dbFile = open(dbPath)
        dbReader = csv.reader(dbFile)

        dbCopy = []

        for row in dbReader:
            if row[2] == self.id:
                row[3] = new_balance
            dbCopy.append(row)
        dbFile.close()

        dbFile = open(dbPath, 'w', newline='')
        dbWriter = csv.writer(dbFile)

        for row in dbCopy:
            dbWriter.writerow(row)

        dbFile.close()


    # authenticate user with the given credentials
    def authenticate(self):
        input_name = self.name
        input_pass = self.password

        dbFile = open(dbPath)
        dbReader = csv.reader(dbFile)

        if self.get_id() == False:
            # username not found in the database
            print('\nUser not found in DB\n')
            return False

        userEntry = list(dbReader)[int(self.id)-1]
        db_pass = userEntry[1]

        dbFile.close()

        if db_pass == input_pass:
            # login successful!
            print('\nLogin successful! Welcome, ' + self.name + '#' + self.id + '\n')
            self.update_log('login')
            return True
        else:
            # incorrect credentials
            print('\nPlease try again\n')
            return False


    def signout(self):
        self.update_log('signout')

    # Adding money to balance
    def deposit(self, amount):
        if valid_amount(amount) == False:
            # Deposit failed
            print("Invalid input. Please try again.")
            return False
        # arithmetic
        current_balance = float(self.get_balance())
        new_balance = float(current_balance) + float(amount)
        # updating the balance
        self.set_balance(new_balance)
        # update log
        self.update_log('deposit')
        print("Deposit successful.")
        return True

    # Withdraw money from account
    def withdraw(self, amount):
        if valid_amount(amount) == False:
            # Deposit failed
            print("Invalid input. Please try again.")
            return False
        # arithmetic
        current_balance = float(self.get_balance())
        new_balance = current_balance - float(amount)
        # updating the balance
        self.set_balance(new_balance)
        # update log
        self.update_log('withdraw')
        print("Withdraw successful.")
        return True


    # Transfering money from one account tp another
    def transfer(self, amount, otherID):
        print()
        # creating otherUser object - taking advantage of default arguments
        otherUser = User(None,None,otherID)
        # also useful for "initializing" balance
        otherUser.get_balance()
        # a transfer is just a simultaneous withdrawal and deposit

        # simple arithmetic!
        my_new_balance = float(self.get_balance()) - float(amount)
        self.set_balance(my_new_balance)
        other_new_balance = float(otherUser.get_balance()) + float(amount)
        otherUser.set_balance(other_new_balance)

        # update log
        self.update_log('transfer')
        # update ledger
        self.update_ledger(amount, otherUser)

    def update_log(self, action):
        # creating a new log entry
        newLogEntry = []
        # adding userID
        newLogEntry.append("USER#" + self.id)
        # specifying type of activity
        newLogEntry.append(action)
        # adding time (formatted as "HH-MM-SS")
        newLogEntry.append(datetime.datetime.now().strftime("%H:%M:%S"))
        # adding date (formatted as "YYYY-mm-dd")
        newLogEntry.append(datetime.datetime.now().strftime("%Y-%m-%d"))

        # opening log file in append mode
        logFile = open(logPath, 'a', newline='')
        logWriter = csv.writer(logFile)
        # updating log.txt
        logWriter.writerow(newLogEntry)
        #closing log file
        logFile.close()


    def update_ledger(self, amount, otherUser):
        # creating a new ledger entry
        newLedgerEntry = []
        # sender userID
        newLedgerEntry.append("USER#" + self.id)
        # receiver UserID
        newLedgerEntry.append("USER#" + otherUser.id)
        # adding amount transferred
        newLedgerEntry.append(str(amount))
        # adding time (formatted as "HH-MM-SS")
        newLedgerEntry.append(datetime.datetime.now().strftime("%H:%M:%S"))
        # adding date (formatted as "YYYY-mm-dd")
        newLedgerEntry.append(datetime.datetime.now().strftime("%Y-%m-%d"))

        # opening log file in append mode
        ledgerFile = open(ledgerPath, 'a', newline='')
        ledgerWriter = csv.writer(ledgerFile)
        # updating log.txt
        ledgerWriter.writerow(newLedgerEntry)
        #closing log file
        ledgerFile.close()

def valid_amount(amount):
    if amount <= 0.0 or type(amount) != float:
        return False
    else:
        return True

def get_userCount():
    numUsers = 0
    dbFile = open(dbPath)
    dbReader = csv.reader(dbFile)
    for row in dbReader:
        numUsers += 1
    return numUsers


# creates a new User entry in the database
def signUp():
    # setting up new UserID
    newID = get_userCount() + 1

    # getting user input
    name_input = input("Enter your username: ")
    pass_input = input("Enter your password: ")

    user_input = User(name_input,pass_input,str(newID).zfill(3))



    # invalid username conditions

    # checking for blank usernames
    if name_input == '' or ' ' in name_input:
        # can't have no blank usernames floating aroung, no siree
        print('\nNo spaces in usernames, please.')
        return False

    # checking for "UN already taken"
    dbFile = open(dbPath)
    dbReader = csv.reader(dbFile)
    for row in dbReader:
        # username already taken
        if row[0] == name_input:
            print('\nUsername already taken.')
            return False


    # updating database
    dbFile = open(dbPath, 'a', newline='')
    dbWriter = csv.writer(dbFile)
    dbWriter.writerow([name_input, pass_input, str(newID).zfill(3), str(0.0)])
    dbFile.close()
    print('\nUser created successfully!\n')

    # updating log
    user_input.update_log('new_acc')

    print("\nThank you for opening a new account with BANK INC.")
    print("Your UserID is: " + str(newID).zfill(3))
    print("Your username is: " + name_input)
    print("Your password is: " + pass_input)
    print("Your balance is empty. Why not deposit some cash?\n")

    # signup was successful
    return True

def login(name_input,pass_input):
    # Login!
    print('\nLogin Selected!\n')
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    input_cred = User(username, password)
    return input_cred.authenticate()





def print_menu1():
    print()
    print("1 - LOGIN")
    print("2 - SIGNUP")
    print("3 - EXIT")
    print()

def print_menu2():
    print()
    print("Select an option:")
    print("1 - BALANCE")
    print("2 - DEPOSIT")
    print("3 - WITHDRAW")
    print("4 - TRANSFER")
    print("5 - SIGNOUT")
    print()

def print_login():
    print()
    print("Login selected")
    print()

def print_signup():
    print()
    print("Sign-up selected")
    print()

def print_exit():
    print()
    print("Bye-bye!")
    print()


def print_deposit():
    print()
    print("Deposit selected.")
    print()
    print("Select an amount to deposit:")

def print_withdraw():
    print()
    print("Withdraw selected.")
    print()
    print("Select an amount to withdraw:")

def print_transfer():
    print()
    print("Transfer selected.")
    print()

def print_signout():
    print()
    print("Sign-out selected.")
    print()










# main program loop
while True:
    # menu
    print_menu1()

    option1  = int(input("Please select an option: "))

    if option1 < 1 or option1 > 3:
        print("Invalid input. Please try again.")

    if option1 == 1:
        # Login selected
        print_login()

        access = False

        # loops until the user has logged-in
        for i in range(3):
            name_input = input("Enter your username: ")
            pass_input = input("Enter your password: ")

            user = User(name_input, pass_input)
            access = user.authenticate()
            if access == True:
                break
            if access == False and i == 2:
                print('\nLogin attempt limit reached. Please try again.\n')


        # Run main account loop
        while True and access == True:
            print_menu2()
            option2 = int(input("Please select an option: "))

            if option1 < 1 or option1 > 5:
                print("Invalid input. Please try again.")

            # Balance check selected
            if option2 == 1:
                balance_string = "{:5.2f}".format(user.get_balance())
                print("Your current account balance is: " + balance_string)

            # deposit selected
            if option2 == 2:
                print_deposit()
                amount = float(input())
                user.deposit(amount)

            # withdraw selected
            if option2 == 3:
                print_withdraw()
                amount = float(input())
                user.withdraw(amount)
                print(str(amount) + " bucks were withdrawn successfully.")

            # transfer selected
            if option2 == 4:
                print_transfer()
                receiverID = input("Enter ID of receiver: ")
                print("Select an amount to transfer: ")
                amount = float(input())
                user.transfer(amount, receiverID)
                print(str(amount) + " bucks were transferred successfully.")

            # signout selected
            if option2 == 5:
                print_signout()
                user.signout()
                print("Logged out successfully.")
                break

    # Sign-up selected
    if option1 == 2:
        print_signup()

        # looks until SignUp is finished
        for i in range(3):
            signUp_done = signUp()
            if signUp_done == False:
                print("\nPlease try again.\n")
                if i == 2:
                    print("\nSign-Up attempt limit reached.\n")
            else:
                break


    if option1 == 3:
        # Farewell message
        print_exit()
        break
