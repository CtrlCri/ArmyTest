## 01 Treasure Hunter

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