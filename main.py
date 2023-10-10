from cgi import print_exception
from slist import SList
from slist import IterableSortedList
from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.value.grade() * course.value.credit_hr()
        credits += course.value.credit_hr()
    if credits == 0:
        return 0
    return sumGrades / credits

def is_sorted(lyst):
    for i in range(0, len(lyst)  - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True

def main():
    
    #Create Course objects for testing
    cs2550 = Course()
    cs2421 = Course(2420, "Duplicate to test remove all", 3.0, 3.0)
    cs2300 = Course(2300, "Discrete Mathematics I", 3.86, 3.69)
    cs2420 = Course(2420, "Algorithms & Data Structures", 3.0, 3.8)
    
    #Test Course Creation w/ no parameters
    print(cs2550)
    
    #Test Course Creation w/ Parameters
    print(cs2420)
    
    #Test Empty Course List
    my_Slist = SList()
    
    #Show my_Slist is empty
    print(my_Slist._size)
    
    #Test Insert
    my_Slist.insert(cs2420)
    print(my_Slist)
    
    #Test Remove
    my_Slist.remove(cs2420)
    print(my_Slist._size)
    
    #Test Remove All
    my_Slist.insert(cs2420)
    my_Slist.insert(cs2421)
    #my_Slist.insert(cs2300)
    print(my_Slist)
    
    my_Slist.remove_all(2420)
    
    #Print list showing both 2420 courses are removed.
    print(my_Slist._size)
    print(my_Slist)
    
    #Test GPA
    my_Slist.insert(cs2420)
    my_Slist.insert(cs2421)
    #print(calculate_gpa(my_Slist))
    
    #Test iterate list
    for x in my_Slist:
        print(x)
    
    
  
if __name__ == "__main__":
    main()
