# Python Bank, Inc.
A simple web banking simulator built with Python. Complete with a database, ledger, and activity logger.

### More about this program
User data (UserID, password, account balance) is stored in a simple plaintext database: `database.txt`.

Tranfers between users are recorded on `ledger.txt` with a timestamp.

All activity (new accounts, logins, signouts, deposits, withdrawals, transfers) is logged in `log.txt` with a timestamp.

### Current working features
* Create new account (Sign-up)
* User login
* Check account balance
* Deposit money
* Withdraw money
* Trasnfer money between accounts
* Activity logger records all actions with timestamps

### To-do list
* Change database format from `txt` to `JSON`
* Add password hash function
* Add custom username functionality
* Get started with Django - web app coming soon!

### Changelog
* Sept. 28 - Project creation & first commit 
* Sept. 29 - Transfers added, activity logger implemented

Made by Lucca Rodrigues - 09/2020
