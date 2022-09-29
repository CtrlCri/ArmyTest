

def special_tree( values, k ) :
	####### DO NOT MODIFY THE CODE BELOW #######
	myTree = MySpecialTree(values)
	soln = []
	for val in range(k):
		soln.append(myTree.pop_max_value())

	return soln
	####### DO NOT MODIFY THE CODE ABOVE #######

class MySpecialTree():
    def __init__(self, values=None):
        self.data = values or []
        for x in range(len(values)//2, -1, -1):
            self.__max_treeify__(x)
        
    def parent(self, x):
        return x >> 1
            
    def left_child(self, x):
        return (x << 1) + 1
            
    def right_child(self, x):
        return (x << 1) + 2
        
    def __max_treeify__(self, x):
        if self.right_child(x) in range(len(self.data)):
         
            if self.data[self.right_child(x)] > self.data[self.parent(x)]:
                self.data[self.parent(x)], self.data[self.right_child(x)] = self.data[self.right_child(x)], self.data[self.parent(x)]
            
            if self.data[self.left_child(x)] > self.data[self.parent(x)]:
                self.data[self.parent(x)], self.data[self.left_child(x)] = self.data[self.left_child(x)], self.data[self.parent(x)]

                
         
    
    def pop_max_value(self):
        result = self.data.pop(0)
        for x in range(len(self.data)//2, -1 ,-1):
            self.__max_treeify__(x)

        return result

if __name__ == "__main__":
    values = [1, 8, 3, 0, 4, 2, 9,]
    k = 3
    myTree = MySpecialTree(values)
    print(myTree.data)
    print(special_tree(values, k))
    