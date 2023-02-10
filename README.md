For each of the scenario below, we do 10 trials on each to analyze the performance of four bin packing algorithms based on 10000 randomly generated items.

1. All items are randomly distributed from 0 to 1. 

On average, first fit = 5123.5, first fit decreasing = 5015.9, best fit = 5069.6, best fit decreasing = 5015.9. We can conclude that first fit decreasing and best fit drcreasing have really similar performance and they will require fewer bins than first fit or best fit. Best fit will be better than first fit. 

Conclusion: first fit decreasing ~ best fit decreasing > best fit > first fit, 
first fit: first fit decreasing : best fit : best fit decreasing = 1.021 : 1 : 1.011 : 1


2. All items are sorted by weight ascendingly

The items are similar to the ones generated from case one unless the items are sorted in increasing order by weights. On average, first fit =  6454.2 first fit desc =  5035.4 best fit =  6454.2 best fit desc =  5035.4. We can see that the decreasing algorithms are a lot better than non decreasing algorithms.

Conclusion: first fit decreasing ~ best fit decreasing >> first fit ~ best fit
first fit: first fit decreasing : best fit : best fit decreasing = 1.281 : 1 : 1.281 : 1

3. Lots of big items (60% big, 40% small)

60% of the items have weights > 0.5, and 40% of the items have weights < 0.5. On average, first fit =  7007.1 first fit desc =  6001.0 best fit =  7004.5 best fit desc =  6001.0. In this case, decreasing algorithms are significantly better, and first fit is also very similar to best fit.

first fit decreasing ~ best fit decreasing > best fit ~ first fit
first fit: first fit decreasing : best fit : best fit decreasing = 1.168 : 1 : 1.167 : 1

4. Mostly big items (80% big, 20% small)
I want to increase the precentage of big items to see what how its affecting the performance of different algorithms. Now 80% of the items have weights > 0.5, and 20% of the items have weights < 0.5. On average, first fit =  8507.5, first fit desc =  8000.5, best fit =  8505.9, best fit desc =  8000.5. It is interesting that both decreasing algorithms are giving the same result almost every time. In this case, first fit is also very similar to best fit. Compared to case 3, the differece in performance is smaller. This makes sense to becauses if most items are greater than 0.5, the results would be similar.

first fit decreasing ~ best fit decreasing > best fit ~ first fit
first fit: first fit decreasing : best fit : best fit decreasing = 1.063 : 1 : 1.063 : 1

5. Lot of small items (40% big, 60% small)
60% of the items have weights < 0.5, and 20% have weights > 0.5. On average, first fit =  5516.3 first fit desc =  4504.2 best fit =  5513.3 best fit desc =  4504.1.
first fit decreasing ~ best fit decreasing > best fit ~ first fit
first fit: first fit decreasing : best fit : best fit decreasing = 1.225 : 1 : 1.224 : 1

4. Mostly small items (20% big, 80% small)
80% of the items have weights < 0.5, and 20% have weights > 0.5. first fit =  4019.9 first fit desc =  3503.1 best fit =  4015.9 best fit desc =  3503.1.

first fit decreasing ~ best fit decreasing > best fit ~ first fit
first fit: first fit decreasing : best fit : best fit decreasing = 1.147 : 1 : 1.146 : 1

5. All small items (80% tiny (< 0.1) )
80% of the items have weights < 0.1, and 20% have weights > 0.3. On average of 10 trials, first fit =  703.9 first fit desc =  702.0 best fit =  703.5 best fit desc =  702.0. The results seem to be pretty similar. 

first fit ~ best fit ~ first fit descending ~ best fit descending
first fit: first fit decreasing : best fit : best fit decreasing = 1 : 1 : 1 : 1

CONCLUSION
In general, best fit decreasing and first fit decreasing are better than first fit and last fit, and they produce very similar results. If all item weights are randomly distributed from 0 to 1, best fit decreasing and first fit decreasing are better than best fit and first fit by roughly 2%. Best fit is slightly better than first fit. 
When all the items are tiny compared to the bin, picking an algorithm wouldn't matter too much. Sorting all items in increasing order will have big negative impact on first fit and best fit. When there are big and small items but items are mostly small, first fit and best fit also become less optimal. 



