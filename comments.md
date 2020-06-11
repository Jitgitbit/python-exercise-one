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

NOTE: adding to a set is relatively safe, python will only add uniques, if a value already exists, it will be ignored !

NOTE: List Comprehensions: nesting within nesting within nesting... . Why blockchain is the blockchain! 

NOTE: The Lambda fn =kindOfLike= an anonymous inline helperfunction.

NOTE: sha256 is simply an algorythm which creates a 64 character hash !

NOTE: Nonce stands for Number used once (-> used as proof, from Proof of Work)

NOTE: Reading Multi-Line Content: '\n' is regarded by Python as one character !

NOTE: There is an alternative for data storage in using JSON which is Pickle, this works with binary though, so it's not very practical here, because we
want to humanly read our data and JSON converts Data to Text.

NOTE: IOError --> groups all file related errors

NOTE: Classes in Python:
    * self. =kindOfLike= this.
    * __init__(self) is Python's version for constructor()        (-> called one of the so called DUNDER methods, (-> Double Under))
    * there are also DUNDER attributes, f.e.: __dict__ , which converts into a dictionary for output !
    * __repr__(self) is actually the print()
    * if you want to make a var or attribut private, you should prefix it by "__" , f.e.: self.__warnings
    * note the bafflingly easy syntax for inheritance: "class Car(Vehicle):"
    * using the super() is pretty much the same

pip3 install --upgrade pip

python3 node.py

in @classmethod, cls is a convention !

NOTE: private attributes: the chain and open_transactions should be only editable from inside the blockchain class, that's why we made them private now.