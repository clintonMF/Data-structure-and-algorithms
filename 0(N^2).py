# an algorithm that runs through a loop twice(nested loops) has a big o of N-square

class BigO_of_Nsquare():
    lst = []
    lst1 = []
    def __init__(self):
        """initializing the class list- so it can be used in the methods"""
        self.lst = BigO_of_Nsquare.lst
        self.lst1 = BigO_of_Nsquare.lst1
    def adding_list(self,llst):
        """this is a function to add new list to the class list"""
        self.lst.append(llst)
    def looping_through(self):
        for lists in self.lst:
            for num in lists:
                self.lst1.append(num)
    def show_list(self):
        print(self.lst)
        print(self.lst1)


clinton = BigO_of_Nsquare()
clinton.adding_list([1,2,3])
clinton.adding_list([4,6,8])
clinton.show_list()
clinton.looping_through()
clinton.show_list()