sparky
======

For logging bets in a calibration game. Runs in bash with Python 2.

Installing and Running
------
1. Grab all the source code.
2. Create a copy of config.py (from config.py.EXAMPLE) and adjust any settings you wish to change.
3. Run Python on \_\_main\_\_.py, or equivalently, run the entire collection as a module.

Usage
-----
Here is an example of a session.

    Welcome to Sparky!
    sparky:) bet 70 My letter arrives in Maryland  
      5.    My letter arrives in Maryland                      2013-11-22
    sparky:) ls
    ============================   50% Bets   ============================
      1.  * Coin flip is heads                                 2013-11-22
      2.  x Coin flip is tails                                 2013-11-22
    ============================   70% Bets   ============================
      0.  x I fail the AIME                                    2013-11-22
      4.    BART does not strike today                         2013-11-22
      5.    My letter arrives in Maryland                      2013-11-22
    ============================   95% Bets   ============================
      3.  * The world does not end today                       2013-11-22
    sparky:) res 4 1
      4.  * BART does not strike today                         2013-11-22
    sparky:) stat
    50%    50.00%    1   1
    70%    50.00%    1   1
    95%   100.00%    1   0
When run in a Bash terminal, there will be colors produced.

Almost all the commands have command-line options.  Type "help" for a full list of commands and "add -h" for a description of the flags.

Todo
------
* Allow editing task weights
* Write some actual documentation
