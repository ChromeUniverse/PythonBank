# Python Bank, Inc.

The goal of this branch is to switch database, ledger and log formats to CSV files using Python's built-in `csv` module.

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
 
## To-do list

* Rebuild automatic folder creation and file creation/initialization
* Make sure all file create/read/write operations are cross-compatibile between OSes
* Make sure usernames are unique (signup fail prompt: "This username isn't available, please pick another one blah blah blah...")
* Function definitions and classes/objects should be in separate files...  
* Add function to make sure transfers are valid (valid UserID, Receiver UserID isn't the same as Sender UserID, etc.)
* `User` object - should the default argument for `User.balance` be `' 0.01' <class 'str'>` or `0.00 <class 'float'>` ?
* Validity check functions (User IDs, passwords, useranames, deposits, withdrawals, transfers)

## Changelog
Check `bank.py` commit history and commit descriptions for more details.
* Oct. 3 - Branch created, first branch commit
* Oct. 4 - "Ported" database, ledger and log from `.txt` to `.csv`


## License

Copyright (C) 2020 Lucca D. Rodrigues

This open-souce project is realeased under the GNU GPL V3 License. Check this repo's LICENSE for more details.
