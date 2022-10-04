# E**ntry-level algorithms**

# **Python (coding): entry-level algorithms**

This coding test assesses a candidate's ability to program a small algorithm in Python, testing their basic programming skills. Using a short and straightforward coding task, this test helps you identify developers with the most essential Python skills.

## **Description**

Python is a general-purpose language that has become very popular, in part due to the wide range of use cases, from web development to data science and machine learning. Good Python developers are therefore highly sought after. 

Strong foundational knowledge of programming in Python is essential for junior programmers. Those candidates are able to hit the ground running and set themselves up for further professional growth.

This Python test gives candidates 10 minutes of time to complete a straightforward coding task involving entry-level algorithms. The code is evaluated against a set of test cases, some of which are available to the candidate to determine if they are on the right track.

This is a great initial screening test that allows you to effectively screen candidates based on essential skills. For more difficult coding challenges, you can consider a Python debugging test or other Python coding tests at an intermediate or advanced level.

We recommend combining coding tests with at least one of our cognitive ability tests evaluating numerical or analytical skills.

[1 - Str to List](https://www.notion.so/1-Str-to-List-9ddae5de82c54ea6af70953f23726d1f)

## 1 - Str to List

Given a string, return a list containing the characteres of the string. If a character in the string is a space or a digit greater than 5, remove them and do not include them in the array.

**Examples:**

input: “my string”

Output: [”m”,”y”,”s”,”t”,”r”,”i”,”n”,”g”]

def str_to_list(str):
	new_str = ""
    
	for c in str:
		if c != " ":
			new_str += c
	str = new_str
	list = []
	for c in str:
		if (c >= '0' and c <= '9'):
			if (c <= '5'):
				list.append(c)
		else: list.append(c)
	return list