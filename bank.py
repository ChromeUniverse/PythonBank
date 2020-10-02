import os
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
    file = open(filename, 'w+')
    if filename == 'database.txt':
        file.write("UID   PASWRD    FUNDS\n")
    if filename == 'ledger.txt':
        file.write("-SENDER-    RECEIVER    --VALUE--   --TIME--    ---DATE---\n")
    if filename == 'log.txt':
        file.write("---ID---    --ACTION--    --TIME--    ---DATE---\n")
    file.close()


# checking if files exist - if not, we create them
def file_check(filename):
    if not os.path.exists(filename):
        file = open(filename,'w+')
        file_init(filename)
        file.close()
    else:
        file = open(filename, 'r')
        content = file.read()
        file.close()

# making sure we have our files ready
file_check('database.txt')
file_check('ledger.txt')
file_check('log.txt')

# PATH to database
dbPath = 'database.txt'
# PATH to ledger
ledgerPath = 'ledger.txt'
# PATH to log
logPath = 'log.txt'

# opening database and storing contents
dbFile = open(dbPath)
# Getting number of registered users
userCount = len(dbFile.readlines())-1
dbFile.close()

# implementing a User object

class User(object):
    #initializing a User object
    def __init__(self, id, password=None, balance=' 0.00'):
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
        # accessing user's entry in database
        userEntry = dbContent[id_num]
        # Updating the User object's 'balance' data attribute
        self.balance = float(userEntry[16:21])
        # Return formatted string
        return "{:5.2f}".format(self.balance)

    # updating database with new balance
    def set_balance(self, new_balance):
        # Updating the User object's 'balance' data attribute
        self.balance = str(new_balance)
        id_num = int(self.id)

        # opening database and spliting it into lines
        dbFile = open(dbPath)
        dbLines = dbFile.readlines()
        dbFile.close()

        # accessing User's entry in database
        userEntry = dbLines[id_num]

        # modifying "funds" section in database
        userEntryList = list(userEntry)
        # too lazy for loops :-P
        userEntryList[16] = list("{:5.2f}".format(new_balance))[0]
        userEntryList[17] = list("{:5.2f}".format(new_balance))[1]
        userEntryList[18] = list("{:5.2f}".format(new_balance))[2]
        userEntryList[19] = list("{:5.2f}".format(new_balance))[3]
        userEntryList[20] = list("{:5.2f}".format(new_balance))[4]

        # updating database with new User Entry
        userEntry = ''.join(userEntryList)
        dbLines[id_num] = userEntry
        # rejoining database
        dbNew = ''.join(dbLines)

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
            # update log
            self.update_log('login')
            return True
        else:
            return False

    def signout(self):
        self.update_log('signout')

    # Adding money to balance
    def deposit(self, amount):
        # arithmetic
        current_balance = float(self.get_balance())
        new_balance = current_balance + float(amount)
        # updating the balance
        self.set_balance(new_balance)
        # update log
        self.update_log('deposit')

    # Withdraw money from account
    def withdraw(self, amount):
        # trivial arithmetic
        current_balance = float(self.get_balance())
        new_balance = current_balance - float(amount)
        # updating the balance
        self.set_balance(new_balance)
        # update log
        self.update_log('withdraw')


    # Transfering money from one account tp another
    def transfer(self, amount, otherID):
        print()
        # creating otherUser object - taking advantage of default arguments
        otherUser = User(otherID)
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
        newLogEntry = ''
        newLogEntry += "USER#"
        # adding UserID
        newLogEntry += self.id
        newLogEntry += "    "
        # adding tive of activity
        # (10 char left padded string with space char - ' ')
        newLogEntry += action.ljust(10,' ')
        newLogEntry += "    "
        # adding time (formatted as "HH-MM-SS")
        newLogEntry += datetime.datetime.now().strftime("%H:%M:%S")
        newLogEntry += "    "
        # adding date (formatted as "YYYY-mm-dd")
        newLogEntry += datetime.datetime.now().strftime("%Y-%m-%d")
        # adding newline character
        newLogEntry += '\n'

        # opening log file in append mode
        logFile = open(logPath, 'a')
        # updating log.txt
        logFile.write(newLogEntry)
        #closing log file
        logFile.close()

    def update_ledger(self, amount, otherUser):
        # creating a new ledger entry
        newLedgerEntry = ''
        newLedgerEntry += "USER#"
        # sender UserID
        newLedgerEntry += self.id
        newLedgerEntry += "    "
        newLedgerEntry += "USER#"
        # receiver UserID
        newLedgerEntry += otherUser.id
        newLedgerEntry += "        "
        # adding amount transferred
        newLedgerEntry += "{:5.2f}".format(amount)
        newLedgerEntry += "   "
        # adding time (formatted as "HH-MM-SS")
        newLedgerEntry += datetime.datetime.now().strftime("%H:%M:%S")
        newLedgerEntry += "    "
        # adding date (formatted as "YYYY-mm-dd")
        newLedgerEntry += datetime.datetime.now().strftime("%Y-%m-%d")
        # adding newline character
        newLedgerEntry += '\n'

        # opening ledger file in append mode
        ledgerFile = open(ledgerPath, 'a')
        # updating ledger.txt
        ledgerFile.write(newLedgerEntry)
        #closing ledger file
        ledgerFile.close()




# creates a new User entry in the database
def signUp(pass_input, userCount):
    userCount += 1
    # UserID for the new user
    newID = str(userCount).zfill(3)

    # updating the database
    dbFile = open(dbPath, 'a')
    dbFile.write(newID + "   " + pass_input + "    " + " 0.00" + "\n")
    dbFile.close()

    # updating log.txt
    newUser = User(newID, pass_input)
    newUser.update_log('new_acc')

    print("Thank you for opening a new account with BANK INC.")
    print("Your UserID is: " + newID)
    print("Your password is: " + pass_input)
    print("Your balance is empty. Why not deposit some cash?")






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

def print_balance(user):
    print()
    print("Balance selected.")
    print()
    print("Your current account balance is: " + user.get_balance())


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

        while True:
            id = input("Enter UserID: ")
            password = input("Enter password: ")
            print()

            user = User(id, password)

            if user.authenticate() == False:
                print("Incorrect credentials. Please try again.")
                print()
            else:
                print("Login successful. Welcome, USER#" + user.get_id())
                break

        # Run main account loop
        while True:
            print_menu2()
            option2 = int(input("Please select an option: "))

            if option1 < 1 or option1 > 5:
                print("Invalid input. Please try again.")

            if option2 == 1:
                print_balance(user)

            if option2 == 2:
                print_deposit()
                amount = float(input())
                user.deposit(amount)
                print(str(amount) + " bucks were deposited successfully.")

            if option2 == 3:
                print_withdraw()
                amount = float(input())
                user.withdraw(amount)
                print(str(amount) + " bucks were withdrawn successfully.")

            if option2 == 4:
                print_transfer()
                receiverID = input("Enter ID of receiver: ")
                print("Select an amount to transfer: ")
                amount = float(input())
                user.transfer(amount, receiverID)
                print(str(amount) + " bucks were transferred successfully.")

            if option2 == 5:
                print_signout()
                user.signout()
                print("Logged out successfully.")
                break

    # Sign-up selected
    if option1 == 2:
        print_signup()

        input_pass = input("Enter your password: ")
        print()

        signUp(input_pass, userCount)

    if option1 == 3:
        # Farewell message
        print_exit()
        break
