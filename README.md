For each of the scenario below, we do 10 trials on each to analyze the performance of four bin packing algorithms based on 10000 randomly generated items.

1. All items are randomly distributed from 0 to 1. 

On average, first fit = 5123.5, first fit decreasing = 5015.9, best fit = 5069.6, best fit decreasing = 5015.9. We can conclude that first fit decreasing and best fit drcreasing have really similar performance and they will require fewer bins than first fit or best fit. Best fit will be better than first fit. 
first fit decreasing ~ best fit decreasing > best fit > first fit

2. All items are sorted by weight ascendingly

The items are similar to the ones generated from case one unless the items are sorted in increasing order by weights. On average, first fit =  6454.2 first fit desc =  5035.4 best fit =  6454.2 best fit desc =  5035.4. We can see that the decreasing algorithms are a lot better than non decreasing algorithms.
first fit decreasing ~ best fit decreasing >> first fit ~ best fit


3. All items are small


4. All items are large


5. items such that every bin = 1 in OPT


