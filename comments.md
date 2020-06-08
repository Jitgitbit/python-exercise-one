closing the REPL --------> controlD
exiting a running program ----> controlZ 
clear

python3 blockchain.py

blockchain.append([blockchain[-1], 5.3])   (--> with [-1], we are accessing the last item in the list)

tx_amount = float(input('Input your transaction amount please: '))            (---> we use float because input always returns strings)

NOTE: Very handy DocString technique allowed by Python, checkout the Screenshot, notice how the highlighted function gets explained
by the use of the added DocString !!! This is a huge plus !! Respect !

NOTE: elif, break and continue: continue stops the loop on the line and brings the loop back to it's starting position, break exits the loop !

NOTE: Python does not know "switch case statements" just the simple if-checks !

NOTE: There is no for(i = 0; i < 10; i++) loop in Python! remarkable ! Instead Python uses range() !

NOTE: Dictionaries =kindOfLike= JS Objects ! And: the key is always written in '' !

NOTE: Tuples: we can ommit the parentheses ! Except if you have a Tuple with only one element, in that case:  (element, ) !

NOTE: enumerate() -> returns a Tuple (index, element) ! Handy for indexing a list !