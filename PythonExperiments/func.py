# hey there now we will study about functions in python

def add_2_nos(no1, no2):
    print "adding ", no1, "and ", no2
    print no1 + no2
    return no2 , no1, no2, "really cool"    # Unlike C, 'return can return multiple value' it is taken as an array

result = add_2_nos(10,20)
print "result : ", result       #result :  (20, 10, 20, 'really cool')

def approp_age_date(your_age):
    girls_age = your_age // 2 + 7
    return girls_age

all_friends_ages = [20,25,30,35,42,55,60]
for i in all_friends_ages:
    print approp_age_date(i)

'''
this illustrates default arguments
suppose in the signup form some one does not select his gender
then we shaould have a default 'unknown' value for it. Let's see
'''

def get_gender(gen = 'unknown'):
    if gen is 'm':
        gen = 'male'
    elif gen is 'f':
        gen = 'female'
    print gen


get_gender()        #unknown
get_gender('m')     #male
get_gender('f')     #female










