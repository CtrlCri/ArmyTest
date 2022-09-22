## **Description**

Python is a high-level, general-purpose language that can be used in anything from web development to data science and machine learning. As an open-source programming language with a strong community, Python offers an expansive library of resources such as web frameworks, testing instruments, and data analysis tools. 

One of the skills required of good Python developers is working with arrays. Arrays are special variables that hold collections of related values. Arrays allow developers to work with a large number of variables quickly and efficiently. 

This test assesses candidates’ skills in working with Python arrays. The test provides candidates with a task description in the appropriate context and specifies the algorithms that need to be developed and the requirements to satisfy. It also provides a few examples to illustrate how the function should behave and asks candidates to solve the task. You can see a complete and functional example of a task by clicking the “preview questions” tab on this page. 

Candidates can run their code to see if certain pre-defined inputs return the expected result. The test is scored automatically using a different set of test cases, which include more challenging corner cases. Once the test is complete, you can inspect the code of the candidate and play it back to interpret their thought process. You can also see the efficiency of the code shown in the results.

1 

You are a treasure hunter and you've recently discovered a map that indicates how many precious items are located in every city on the map. Although you would like to find as many treasures as possible, you are fearful of going into a city that is heavily guarded. You will get caught by the guards and be sent to jail.

The map is represented by a 2D array. Each element represents a city and the value at that index is the number of treasures in that city. The heavily guarded cities are represented on the map by zeros.

Write a function:

max_treasure( treasure_map )

that, given 2D array treasure_map, returns an integer representing the maximum amount of treasures you can collect by traveling from city to city.

Take the following into account:

. You can start anywhere on the map

. You must avoid heavily guarded cities

. You may only travel up, down, left, or right, 1 index at a time

.It is possible for different paths to yield the same amount of treasures

. An empty map should return 0

. If the map contains anything else than positive integers, the function should return -1

Examples

On the map:

[[3, 0, 0, 1, 2],

[0, 1, 4, 0, 0],

[5, 0, 0, **3**, **3**]]

your maximum reward would be 6 precious items, by looting the two bolded cities (3, 3).

On the map:

[[3, 0, 0, 1, 2],

[0, **1**, **4**, 0, 0],

[**5**, 0, 0, 3, 0]]

your maximum reward would be 5 precious items. There are two ways to achieve that: either loot cities 4 and 1, or loot city 5.

Input parameters: ([[1,2,0],[3,0,5],[0,0,1],])
Result: (5,)
Expected: (6,)

Input parameters: ([[-3,0],[4,0],])
Result: (4,)
Expected: (-1,)