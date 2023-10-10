''' Course Class for Project 4 of CS 2420 '''

class Course:
    ''' Course object '''
    def __init__(self, number = 0, name = "Unnamed Course", credit_hour = 0.0, grade = 0.0):
        self.number = number
        self.name = name
        self.credit_hour = credit_hour
        self.grade = grade
        
        #Parameter Evaluation
        if (isinstance(self.number, int) != True):
            raise ValueError("Passed value not of type int.")
    
        if (isinstance(name, str) != True):
            raise ValueError("Passed value not of type string.")

        if (isinstance(self.credit_hour, float) != True):
            raise ValueError("Passed value not of type float.")
        
        if (isinstance(self.grade, float) != True):
            raise ValueError("Passed value not of type float.")
        
        if(self.grade < 0.0 or self.grade > 4.0):
            raise ValueError("Passed value for grade outside parameters.")

    def number(self):
        return self.number()
    
    def name(self):
        return self.name
    
    def credit_hr(self):
        return self.credit_hour
    
    def grade(self):
        return self.grade
    
    def __eq__(self, other):
        return self.number == other
      
    def __ne__(self, other):
        return self.number != other
      
    def __lt__(self, other):
        return self.number < other
      
    def __gt__(self, other):
        return self.number > other
      
    def __le__(self, other):
        return self.number <= other
      
    def __ge__(self, other):
        return self.number >= other
      
    def __str__(self):
        return (f"{self.number} {self.name} Grade: {self.grade} Credit Hours: {self.credit_hour}")