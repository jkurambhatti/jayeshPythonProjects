'''
as we saw in earlier tutorial how to use default arguments
suppose func foo( arg1='arg1' , arg2='arg2', arg3='arg3', arg4='arg4')
    and we want to set value only for 1 and 3, or 3 and 4, or 1 and 4 etc
    then we can use  the name of arg as keyword to set values
    this also enables us to set values in any order
    Let's see how
'''

def function(name = 'jayesh', office = 'vayavyalabs', lives = 'btm'):
    print name, office, lives

function()
function(name = 'akash', lives = 'ahmedabad')       #arguments act as keywords
function(lives='bengaluru', name = 'rishi')         #arguments can be passed in any order

# VARIABLE ARGUMENTS
'''
now let's study how variable arguments is handled in python
'''

def add_nums(*args):
    #sum = 0
    sum = ""
    for i in args:
        sum = sum + i
    print sum

#add_nums(10,20)
#add_nums(10,30,50,70,80)
add_nums("abc", "def", "ghijk")


# UNPACKING ARGUMENTS

def ROI(principle, interest, years):
    total = principle * interest *years
    print total

ROI(1000, 1.5, 10)  # one way
acct_data = [1000, 1.5, 10]
ROI(acct_data[0], acct_data[1], acct_data[2])   #2nd way

ROI(*acct_data)     # 3rd way This is called unpacking of arguments

# so the * symbol before the arguments notifies that it has to unpacked.
# it saves a lot of typing











