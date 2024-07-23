#---QUIZ GAME---
print('''Welcome to quiz game !!
write only index of the correct answer
      
''')

score = 0

# ---------------QUESTION 1-----------------------

print("• QUESTION 1 :\n What arthematic operator does this ** symbol represent?"'\n''options:')
options1={ 
    'a':"multiplication", 
    'b':'exponential', 
    'c':'division'
    }
print(options1)
answer1=input("select your option: ").lower()    
if answer1 == 'b':
    score +=10
    print('correct! you earned 10 points''\n')        
else:
    print('Incorrect!, correct answer is option b : exponential''\n' )
    
# ---------------QUESTION 2-----------------------

print("• QUESTION 2 :\nhow do you print a statement in python?"'\n''options:')
options2={ 
    'a':"print()", 
    'b':'printf()', 
    'c':'system.out.println()'
    }
print(options2)
answer2=input("select your option: ").lower()    
if answer2 == 'a':
    score +=10
    print('correct! you earned 10 points''\n')        
else:
    print('Incorrect!, correct answer is option a : print()''\n' )

# ---------------QUESTION 3-----------------------

print("• QUESTION 3:\nWhich of the following is mutable data type? "'\n''options:')
options3={ 
    'a':"tuple", 
    'b':'list', 
    'c':'string'
    }
print(options3)
answer3=input("select your option: ").lower()    
if answer3 == 'b':
    score +=10
    print('correct! you earned 10 points''\n')        
else:
    print('Incorrect!, correct answer is option b : List''\n' )

# ---------------QUESTION 4-----------------------

print("• QUESTION 4:\nWho developed Python programming language?"'\n''options:')
options4={ 
    'a':"Guido Van Rossum", 
    'b':'Zim den', 
    'c':'Wick Van Rossum'
    }
print(options4)
answer4=input("select your option: ").lower()    
if answer4 == 'a':
    score +=10
    print('correct! you earned 10 points' '\n')        
else:
    print('Incorrect!, correct answer is option a : Guido Van Rossum''\n')

#----------------Display Result---------------------

print("Final Score:",score)


  
 





