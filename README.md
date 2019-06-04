# strypes_assignment

Start the application by executing start.py. If no arguments are provided
the app will initialise a user interface where you can choose the following:

    1 - Run one or multiple tests from /tests
    2 - Run one or more tests manually
    3 - Generate new random test
    4 - Quit

    1. The app scans all valid files in the /test folder and lists them to user.
        User can choose to execute from one to all tests available
        #note - every time the app is executed, database is updated
    2. User can choose to run test/test from another location - just type the
        absolute path to the file/s. When the file is run, the app automatically
        adds it to the database(/tests folder).
    3. App creates a random combination of 2D matrix in /tests folder. User can
        choose to run the test afterwards.
    4. App plays Rammstein’s new single (sadly, this functionality is still in
        the works, the app just quits :<  )

If user chooses to start the application start.py with one or more arguments, app
would behave as stated in the assignment doc. If multiple tests are supplied, each
result will be displayed on a new line.
