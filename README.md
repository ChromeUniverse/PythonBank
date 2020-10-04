# Python Bank, Inc.

The goal of this branch is to switch database, ledger and log file formats from `.txt` to `.csv` using Python's built-in `csv` module.

Check the "To-Do" below for a more comprehensive list of featuers to be added in this branch.

Switching to CSV unlocks some cool features:
* Easy creation and storage of extra data attributes for `User` objects
* Custom usernames
* Variable-length passwords
* Effortless database read/write
* and more!

## Current working features
* Create new account (Sign-up)
* Custom usernames and variable-legnth passwords 
* User login and sign-out
* Check account balance
* Deposit money
* Withdraw money
* Transfer money between accounts
* User activity is stored in `log.csv`
* Transfers are recorded on `ledger.csv`
* `bank.py` now automatically creates the `./bank_files` dir 
* `database.csv`, `log.csv` and `ledger.csv` are automatically created and stored in `./bank_files`
* Sign-up and login attempt limit (3 tries)
* Validity checks during sign-up: no `' '` (blankspace) chars in username, checks if username in already registered 

 
## To-do list

* Make sure all file create/read/write operations are cross-compatibile between OSes
* Function definitions and classes/objects should be in separate files...  
* Add function to make sure transfers are valid (valid UserID, Receiver UserID isn't the same as Sender UserID, etc.)
* Validity check functions (User IDs, passwords, useranames, deposits, withdrawals, transfers)

## Changelog
Check `bank.py` commit history and commit descriptions for more details.
* Oct. 3 - Created `/CSV` branch, first branch commit
* Oct. 4 - "Ported" database, ledger and log from `.txt` to `.csv`
* Oct. 4 - Added automatic directory/file creation
* Oct. 4 - Added 3-try attempt limit for sign-up and login
* Oct. 4 - Added minor validity checks for usernames during sign-up 


## License

Copyright (C) 2020 Lucca D. Rodrigues

This open-souce project is realeased under the GNU GPL V3 License. Check this repo's LICENSE for more details.
