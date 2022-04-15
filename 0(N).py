# an algorithm that runs through a loop has a big 0 0f 0(N)
# below is an example of such

class BigO_Of_ON():
    def __init__(self,lst):
        self.lst = lst
    def looping(self):
        for ele in self.lst:
            print(ele)  
            
even_numbers = BigO_Of_ON([1,3,4,5,6]) 
even_numbers.looping()     
  
    