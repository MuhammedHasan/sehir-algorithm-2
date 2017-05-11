# Assignment 2

Muhammed Hasan Çelik - 213960832

## Q.1

Function named `best_route_tables` is writen to fill two dynamic programming table one holds best scores for each cell in mountain and other to hold previous best place to come current place.

```
init scores with copying mountain and prevs tables 
for each row_index, cell_index, cell_value in scores then
	for each next_row_index, next_cell_index, next_cell_value in scores then
		if cell_value  + mountain[next_row_index][next_cell_index] >= next_cell_value then
			update score of next_cell
			prevs[next_row_index, next_cell_index] = (cell_row, cell_index)
    return scores, prevs
```

then I use this too table to calculate best route and score as follow:

```
bestScore, indexes = get max value and its indexes in last row
path = list()
while indexes in prevs then
	add prev to path
	update indexes with new previous node
return path, bestScore
```

Complexity: O(n) where n is number of cell in mountain. Becasue it itearate all node and just iterate next not for each node. Moreover, each node has two next node then complexity is O(2n) = O(n).

## Q.2


```
inputData = convert input data list of tuple of 4 item which are (start, end, participants, conference)
sort this data by end time
prevs = calculate closed unintersectining previous event for each event
init table with len of input + 1 with all zero expect second value which hold participant of first conference

for i in range(1, len(inputData)):
	table[i + 1] = max(inputData[i][2] + table[prevs[i]], table[i])

conferences = calculate conferences with using previous and table
return last item of scores and conferences
```

Complexity: O(n log(n)) beacuse we sort all conferences in beginning and dynamic programming part is just linear beacuse of one time iteration of all conferences.

## Q.3

```
init dynamic programming table
table[0][0] = 1
table[1][1] = 1
for i in range(1, n + 1):
	c = 0
    for j in range(1, i + 1):
		c += table[i - j][min(i - j, j)]
		table[i][j] = c
return table[n][n] - 1
```

Code above is basicly

g(x, y) = partitions of all number of y with using at most x in partition numbers 
f(n) = sum of g(0, n), g(1, n), g(2, n) ... g(n - 1, 1)

g function is memories and reused in with table. 

Complexity: O(n^2) because n number iterated with two nested for loop. 
