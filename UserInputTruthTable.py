from TruthTable import *

#this file is so a user can interact in the terminal

print("""
      Input Premises and Conclusion in the following format:
      
      Variable is True:
      (variable)
      
      NOT:
      not (variable)
      
      OR:
      (variable 1) or (variable 2)
      
      AND:
      (variable 1) and (variable 2)
      
      IF:
      if (variable 1) then (variable 2)
      
      IFF:
      (variable 1) if and only if (variable 2)  
      
      Variables must be one letter.
      """)

premises = []
premise = None

while premise != 'Next':
    premise = input("Enter premises.  When done enter 'Next'\n")

    if premise != 'Next':
        premises.append(premise)
    
    
print("Premises:", premises)

conclusion = input('Enter conclusion\n')

print("Conclusion:", conclusion)


print(find_validity(premises, conclusion))