import itertools

class Premise():            #creates the ADT for each statement
    def __init__(self, premise):
        self.premise = premise
        self.words = self.premise.split()
        self.premise_variables = [word for word in self.words if len(word) == 1]
        self.premise_type = [word for word in self.words if len(word) != 1]
        self.table = []    
                        
                       
            
class TruthTable():
    def __init__(self):
        self.premises = []
        self.variables = []
        self.var_table = []
        self.conclusion = None
        
        self.valid = None
                    
                    
    def add_vars(self, premise):            #adds variables
        for var in premise.premise_variables:
            if var not in self.variables:
                self.variables.append(var)
                    
    def add_premise(self, premise):        #adds premises     
        self.premises.append(premise)
        
        self.add_vars(premise)
        
        
    def generate_var_table(self):           #generates the table of all the combinations of true and false for the variables
        n = len(self.variables)
        self.var_table = list(itertools.product([True, False], repeat=n))
                
    def _premise_table(self, premise):              #if statement is formated correctly, it gets analyzed correspondingly against the truth table
        if premise.premise_type == ['if', 'then']:
            premise.table = self.if_then(premise.premise_variables)
            
        elif premise.premise_type == ['not']:
            premise.table = self._not(premise.premise_variables)
            
        elif premise.premise_type == ['or']:
            premise.table = self._or(premise.premise_variables)
            
        elif premise.premise_type == ['and']:
            premise.table = self._and(premise.premise_variables)
            
        elif premise.premise_type == []:
            premise.table = self._true(premise.premise_variables)
                
        elif premise.premise_type == ['if', 'and', 'only', 'if']:
            premise.table = self.iff(premise.premise_variables)
            
        else:
            ("Whoops try again")
            
    def premise_table(self):
        for premise in self.premises:
            self._premise_table(premise)
                
    def conclusion_table(self):
        self._premise_table(self.conclusion)
        
        
        
     #the following generate truth tables for the statements   
                
    def if_then(self, premise_variables):
        index_var1 = self.variables.index(premise_variables[0])
        index_var2 = self.variables.index(premise_variables[1])       
        
        premise_table = []
               
        for row in self.var_table:
            if row[index_var1]:
                premise_table.append(row[index_var2])
                
            else:
                premise_table.append(True)
                
                
        return premise_table
    
    def _true(self, premise_variables):
        index_var = self.variables.index(premise_variables[0])
        
        premise_table = []
        for row in self.var_table:
            if row[index_var]:
                premise_table.append(True)
                
            else:
                premise_table.append(False)
                
        return premise_table

    
    def _not(self, premise_variables):
        index_var = self.variables.index(premise_variables[0])
        
        premise_table = []
        for row in self.var_table:
            if row[index_var]:
                premise_table.append(False)
                
            else:
                premise_table.append(True)
                
        return premise_table
    
    def _or(self, premise_variables):
        index_var1 = self.variables.index(premise_variables[0])
        index_var2 = self.variables.index(premise_variables[1])       
        
        premise_table = []
        
        for row in self.var_table:
            if row[index_var1] or row[index_var2]:
                premise_table.append(True)
                
            else:
                premise_table.append(False)
                
        return premise_table
                
    def _and(self, premise_variables):
        index_var1 = self.variables.index(premise_variables[0])
        index_var2 = self.variables.index(premise_variables[1])       
        
        premise_table = []
        
        for row in self.var_table:
            if row[index_var1] and row[index_var2]:
                premise_table.append(True)
                
            else:
                premise_table.append(False)
                
        return premise_table
                
    def iff(self, premise_variables):
        index_var1 = self.variables.index(premise_variables[0])
        index_var2 = self.variables.index(premise_variables[1])       
        
        premise_table = []
        
        for row in self.var_table:
            if row[index_var1] == row[index_var2]:
                premise_table.append(True)
                
            else:
                premise_table.append(False)
        
        return premise_table
        
        #checks if the truth table if premises are true, conclusion is also true
    def validity(self):
        check_indices = []
        false_indices = []
              
                
        for premise in self.premises:
            i = 0
            for row in premise.table:
                
                if row and i not in false_indices:
                    check_indices.append(i)
                    i += 1
                    
                elif not row and i in check_indices:
                    check_indices.remove(i)
                    i += 1
                    
                else:
                    false_indices.append(i)
                    i += 1
               
        for i in check_indices:
            
            if self.conclusion.table[i] == False:
                return False
            
            if i == check_indices[-1]:
                return True
        
        
        
        
        
        
        
def find_validity(premises, conclusion):
    
    truth_table = TruthTable()
    for raw_premise in premises:
        premise = Premise(raw_premise)
        
        #checks if premise is in the valid form
        
        premise_forms = [['if', 'then'], ['or'], ['and'], ['not'], [], ['if', 'and', 'only', 'if']]
        
        if premise.premise_type not in premise_forms:
            return("Invalid premise: '{}' \nTry again.").format(premise.premise) 
        
        truth_table.add_premise(premise)

    truth_table.conclusion = Premise(conclusion)
    
    #checks if there is a variable in conclusion that is not in premises
    
    for var in truth_table.conclusion.premise_variables:
        if var not in truth_table.variables:
            return("Variable in conclusion not in premises.  Try again.")
    
    truth_table.generate_var_table()
    truth_table.premise_table()
    truth_table.conclusion_table()
    
    if truth_table.validity():
        return "The argument is valid." 
    
    else:
        return "The argument is not valid."      
    
    
    
    
       #test cases 
                
if __name__ == '__main__':
    
    premises = ['if p then q', 'if q then r']
    conclusion = 'if p then r'
    
    assert(find_validity(premises, conclusion) == 'The argument is valid.')
    
    
    
    
    
    
    premises2 = ['p or q', 'if p then r', 'if q then r']
    conclusion2 = 'r'
    
    assert(find_validity(premises2, conclusion2) == 'The argument is valid.')
    
    
    
        
    premises3 = ['if p then q', 'q']
    conclusion3 = 'p'
    
    assert(find_validity(premises3, conclusion3) == 'The argument is not valid.')
    
    
    premises4 = ['if p then q', 'not p']
    conclusion4 = 'not q'
    
    assert(find_validity(premises4, conclusion4) == 'The argument is not valid.')

    
    
    premises5 = ['p', 'not q', 'q or r']
    conclusion5 = 'if p then r'
    
    assert(find_validity(premises5, conclusion5) == 'The argument is valid.')

    
    premises6 = ['p if and only if q', 'q and r']
    conclusion6 = 'p'
    
    assert(find_validity(premises6, conclusion6) == 'The argument is valid.')

    
    premises7 = ['not p']
    conclusion7 = 'p'
    
    assert(find_validity(premises7, conclusion7) == 'The argument is not valid.')

    
    pass