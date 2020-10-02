# Python Bank, Inc.
A simple web banking simulator built with Python. Complete with a database, ledger, and activity logger.

This mini-project was built mostly to test out some things related to object-oriented programming and simple databases. 

## More about this program
User data (UserID, password, account balance) is stored in a simple plaintext database: `database.txt`.

Tranfers between users are recorded on `ledger.txt` with a timestamp.

All activity (new accounts, logins, signouts, deposits, withdrawals, transfers) is logged in `log.txt` with a timestamp.

## Usage 

### Setup

Make sure you have Python 3 installed beforehand. No additional packages or modules are required.

You can clone this repo using the new GitHub CLI, or just plain Git.

Run `bank.py` on your machine using your Terminal or Command Line.

On the first time you run `bank.py`, it will automatically create a new folder named `bank_file`. It's located in the script's CWD (a.k.a `./`). `bank.py` then changes its CWD to `./bank_files`.

Three plaintext (`.txt`) files are automatically created and initialized in this folder: `database`, `ledger` and `log`. They're used for storing user data, recording transactions, and monitoring user activity. Open them with any text editor to see more details.


### Creating a new account

In the main menu, select `2`. Your UserID is created automatically, so you only have to enter your password.

```
 ////////////////////////
   Welcome to BANK INC.
 ////////////////////////


1 - LOGIN
2 - SIGNUP
3 - EXIT

Please select an option: 2

Sign-up selected

Enter your password: 123456

Thank you for opening a new account with BANK INC.
Your UserID is: 001
Your password is: 123456
Your balance is empty. Why not deposit some cash?
```

Make sure your password is 6 characters long!

### Login

Select `1` in the main menu. Enter your UserID and password.

```
1 - LOGIN
2 - SIGNUP
3 - EXIT

Please select an option: 1

Login selected

Enter UserID: 001
Enter password: 123456

Login successful. Welcome, USER#001
```

### Main account page

```
Select an option:
1 - BALANCE
2 - DEPOSIT
3 - WITHDRAW
4 - TRANSFER
5 - SIGNOUT

Please select an option:
```
The menus should be fairly straightforward to interact with.

When asked to input any amount of money, make sure to always add two decimal places: use `5.00` instead of `5`.

You can access `database.txt`, `ledger.txt` and `log.txt` using any text editor (Notepad, Atom, Emacs, what have you) to verify that `bank.py` is reading and writing data properly.

And that's about it. Go have some fun depositing and withdrawing money.

## Current working features
* Create new account (Sign-up)
* User login and sign-out
* Check account balance
* Deposit money
* Withdraw money
* Transfer money between accounts
* Activity logger with timestamps
* Ledger - records transfers
* `bank.py` now automatically creates a folder called `bank_files` (located in the CWD) to store the extra files
* `database.txt`, `ledger.txt` and `log.txt` are automatically created and initialized
* All file create/read/write operations are now cross-compatibile between OSes!
 
## To-do list
* Function definitions and classes/objects should be in separate files...  
* Add function to make sure transfers are valid (valid UserID, Receiver UserID isn't the same as Sender UserID, etc.)
* `User` object - should the default argument for `User.balance` be `' 0.01' <class 'str'>` or `0.00 <class 'float'>` ?
* Improve cross-platform compatibility
* Add more flexibility for passwords - variable length, etc.
* Add password hashing and salting
* Add custom usernames
* Change database format from `.txt` to `.json` or `.csv` - or maybe even switch to SQL, why not?
* Get started with Django - web app coming soon (maybe)!

## Changelog
Check `bank.py` commit history and commit descriptions for more details.
* Sep. 28 - Project creation & first commit 
* Sep. 29 - Added transfers 
* Sep. 29 - Added activity logger 
* Sep. 30 - Added ledger
* Sep. 30 - First version of "Usage" section in `README.md`
* Oct. 01 - Added automatic file creation and initialization
* Oct. 02 - Updated "Usage - Setup" section
* Oct. 02 - Minor bug fixes


Spotted any issues? Want to contibute? Open a new issue or make a pull request. 

Made by Lucca Rodrigues - 2020
