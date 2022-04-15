class big0_of_01():
    """this class shows the big o notation for 0(1)"""
    def __init__(self, num):
        """initializing the variables"""
        self.num = num
        self.lst = list(range(1,self.num))
         
    def chosing_the_first(self):
        """this function prints out the first number in the list"""
        print(self.lst[0])
        
case1 = big0_of_01(10)
case1.chosing_the_first()

case2 =big0_of_01(1555)
case2.chosing_the_first()
        
