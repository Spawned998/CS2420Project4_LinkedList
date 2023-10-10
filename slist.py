
class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None
            
        #def __repr__(self):
            #pass
            #return "{}".format(self.value)

    def __init__ (self):
        self._head = None
        self._size = 0
        
    
###########################################################################################
    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, passedValue):
        #Create instance of SListNode
        newNode = self.SListNode(passedValue)
        
        #Check if list is empty
        if self._head == None:
            self._head = newNode
        
        #Check if passedValue is less than head
        elif (self._head.value > newNode.value):
            newNode.next = self._head
            self._head = newNode
            
        else:
            currentNode = self._head
            
            while(currentNode.next != None):
                #Check next nodes value
                if(currentNode.next.value <= passedValue):
                    currentNode = currentNode.next
                    
                else:
                    #Insert node
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                    break
            
            #PassedValue is greater than all in list
            currentNode.next = newNode
            
        #Increase size of list
        self._size += 1
        
    
#########################################################################


    def size(self):
        return self._size
    
#########################################################################


    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        
        #Check if list is empty
        if(self._head == None):
            return None

        #Check if head is the value
        elif(self._head.value == value):
            return self._head
        
        else:
            if(self._head.next == None):
                return None
            
            currentNode = self._head
            while(currentNode.next != None):
                if(currentNode.value == value):
                    return currentNode
                else:
                    currentNode = currentNode.next
                    
            #Test last node
            if(currentNode.value == value):
                    return currentNode
            else:
                return None
                
            #Value not found
            return False


#########################################################################


    '''Remove the first occurance of value.'''
    def remove(self, value):
        
        #Check if list is empty
        if(self._head == None):
            return False

        #Check if head is the value
        elif(self._head.value == value):
            #Check if anything past head
            if(self._head.next == None):
                self._head = None
            else:
                self._head = self._head.next
            
            #Decrease list size
            self._size -= 1
            return True
        
        else:
            if(self._head.next == None):
                return False
            
            currentNode = self._head
            while(currentNode.next != None):
                if(currentNode.next.value == value):
                    currentNode.next = currentNode.next.next
                    #Decrease list size
                    self._size -= 1
                    return True
                else:
                    currentNode = currentNode.next
                
            #Value not found
            return False




#########################################################################

    '''Remove all instances of value'''
    def remove_all(self, value):
        foundValue = True
        
        while(foundValue == True):
            foundValue = self.remove(value)
            
##########################################################################

    '''Convert the list to a string and return it'''
    def __str__(self):
        #If list is empty
        if(self._head == None):
            return "[]"
        
        output = "["
        #iterate through list, inserting each value into output
        currentNode = self._head
        
        #What if list is empty?

        while(currentNode.next != None):
            output += ((currentNode.value.__str__()) + ",")
            currentNode = currentNode.next
            
        #End of list
        output += ((currentNode.value.__str__()) + "]")
        
        #output += (str(currentNode.value.__str__()) + "]")
        
        return output


#########################################################################


    '''Return an iterator for the list'''
    def __iter__(self):
        return IterableSortedList(self)


#########################################################################

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        
        #Check if list is empty
        if(self._head == None):
            raise IndexError("Passed value is out of list range.")
        
        if(index < 0):
            raise IndexError("Passed value is out of list range.")

        
        elif(index >= self._size):
            raise IndexError("Passed value is out of list range.")

    
        else:
            counter = 0
            currentNode = self._head
            
            while(counter < index):
                currentNode = currentNode.next
                counter += 1
                
            return currentNode.value
    
#########################################################################


    def __len__(self):
        pass

#########################################################################


class IterableSortedList:
    #Use this as iterator rather than SList object itself
    #Constructor takes a list as a parameter
    def __init__(self, passedList):
        self.currentNode = None
        self.nextNode = passedList._head

    def __next__(self):
        #Check for stop condition
        if self.nextNode is None:
            raise StopIteration
        
        self.currentNode = self.nextNode
        self.nextNode = self.nextNode.next
        return self.currentNode.value    