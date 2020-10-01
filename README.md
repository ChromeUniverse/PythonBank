# Python Bank, Inc.
A simple web banking simulator built with Python. Complete with a database, ledger, and activity logger.

## More about this program
User data (UserID, password, account balance) is stored in a simple plaintext database: `database.txt`.

Tranfers between users are recorded on `ledger.txt` with a timestamp.

All activity (new accounts, logins, signouts, deposits, withdrawals, transfers) is logged in `log.txt` with a timestamp.

## Usage

### Setup

Make sure you have Python 3 installed beforehand. 

You can clone this repo using the new GitHub CLI. But if you prefer manually copying and pasting files from this repo:

Install `bank.py` on your machine. Doesn't matter where you place it, really.

Create three plaintext (`.txt`) files: `database`, `ledger` and `log`. 

Include a header in the first line of each file. `bank.py` relies on these headers to work properly, so don't forget to include them.

For example, `log.txt` could use a neat header like so: (check out the provided templates for each file for more details)

```
---ID---    --ACTION--    --TIME--    ---DATE---
```

Specify the _absolute_ paths to each file in `bank.py`:  (make sure to use `\\` for Windows and `/` for Mac and Linux)

```
# PATH to database
dbPath = 'C:\\Users\\omnic\\Documents\\Programming\\banking_py\\database.txt'
# PATH to ledger
ledgerPath = 'C:\\Users\\omnic\\Documents\\Programming\\banking_py\\ledger.txt'
# PATH to log
logPath = 'C:\\Users\\omnic\\Documents\\Programming\\banking_py\\log.txt'
```

Now run `bank.py` on your Terminal or Command Line.

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

## To-do list
* Paths to `database.txt`, `ledger.txt` and `log.txt` should be _relative_!
* Automatically create database, ledger and log files in the same parent folder as `bank.py`, if don't already exist
* Add more flexibility for passwords - variable length, etc.
* Add password hashing and salting
* Add custom usernames
* Change database format from `.txt` to `.json` or `.csv` - or maybe even switch to SQL, why not?
* Get started with Django - web app coming soon (maybe)!

## Changelog
Check `bank.py` commit history and commit descriptions for more details.
* Sept. 28 - Project creation & first commit 
* Sept. 29 - Added transfers and activity logger 
* Sept. 30 - Added ledger and first version of "Usage" section in `README.md`


Spotted any issues? Want to contibute? Open a new issue or make a pull request. 

Made by Lucca Rodrigues - Sept. 2020
