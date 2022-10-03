# D****ata structures & objects****

# **Python (coding): data structures & objects**

This Python data structures & objects test evaluates your candidate's object-oriented programming skills. In 30 minutes, they will work with Python objects and implement a data structure. This test will help you hire mid-level Python developers.

## **Covered skills**

Data structures & objects

## **This test is relevant for**

Any developer who is expected to have practical experience using Python. The difficulty level of these questions is geared to mid-level developers.

## **Description**

Python is a general-purpose language that has become very popular, in part due to the wide range of use cases, from web development to data science and machine learning. Good Python developers are therefore highly sought after.

Working with and implementing data structures is crucial to the success of a developer. An effective data structure will enable you to effectively manage, organize, and represent your data. Data structures are often implemented as objects, so the ability to effectively work with objects and understand object-oriented programming is an important skill to have.

This coding test presents a real-life scenario to your candidates. They have 30 minutes to implement a data structure that meets the given requirements. Candidates can run the code against a selected number of test cases to see if they are on track. After submission, the code is automatically scored based on another set of test cases that also covers exceptions or corner cases. You will be able to play back how the code came about in the coding editor. 

We recommend combining this coding test with other programming tests such as Django and SQL, as well as cognitive ability tests.

## 01 - Special Tree

You are tasked to implement a special tree data structure where the parent node must always be larger in value than all of its children nodes.

The skeleton class MySpecialTree is given. You need to implement the following two functions:

1. _ _**max_treeify_ _**(self, x) : this function adds the given value into the tree. Make sure that the parent node is always larger in value than any of its children nodes.
2. pop_max_value(self) : this function removes the max value from the tree and returns that value. After removing the max value, you might need to call _ _**max_treeify_ _** to make sure the tree is still satisfying the requirement that the parent node is larger in value than any of its children nodes.

The _ *init* _ _ , parent, left_child and rigth_child functions are already completed for you.

The **MySpecialTree** class takes an array of integers and integer k representanting the number of times your **pop_max_value** function will be called.

Note: the initial code in the editor uses tabs for indentation. Don’t mix it with spaces.

Two examples: 

input:

. values = [1, 8, 3, 0, 4, 2, 9]

. k = 1

Output: [9]

Input:

. values = [1, 8, 3, 0, 4, 2, 9]

. k = 1

Output: [9, 8, 4]

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
			pass

		def pop_max_value(self):
			pass