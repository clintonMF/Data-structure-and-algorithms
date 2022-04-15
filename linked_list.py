class LinkedList():
    """this is a class that creates a linked list and 
    performs different operations on it
    """
    def __init__(self, lst):
        """Initializing the list"""
        self.lst = lst
        
    def add_to_top(self, num):
        """this function adds a number to the top or front of the list

        Args:
            num (integer): this number becomes index (0)
        """
        copy = self.lst[:]
        new_lst = [num]
        self.lst = new_lst + copy
    
    def add_to_bottom(self, num):
        """this function adds the number to the end or bottom of the lsit

        Args:
            num (integer): this number becomes index(-1)
        """
        self.num = num
        self.lst.append(self.num)
        
    def remove_from_top(self):
        """this function removes the first number in the list
        """
        del self.lst[0]
        
    def remove_from_bottom(self):
        """this function removes the first number in the list
        """
        del self.lst[-1]
        
    def num_of_items(self):
        """show the number of items in the list"""
        num = len(self.lst)
        if num == 1:
            print(f"there is {num} item in the list")
        else:
            print(f"there are {num} items in the list")
        
    def show_val(self):
        for num in self.lst:
            print(num)
            
            
even_num  = LinkedList([2,4,6,8])
even_num.remove_from_bottom()
even_num.remove_from_bottom()
even_num.remove_from_bottom()

even_num.show_val()
even_num.num_of_items()