# CMPS 2200 Reciation 6
## Answers

**Name:**______JT McDermott___________________


Place all written answers from `recitation-06.md` here for easier grading.

|      n |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|--------|---------------------|----------------------|------------|
|     10 |               0.045 |                0.059 |      0.002 |
|     50 |               0.288 |                0.306 |      0.008 |
|    100 |               0.573 |                0.752 |      0.017 |
|    500 |               3.896 |                3.987 |      0.105 |
|   1000 |              38.769 |               12.460 |      0.223 |
|   5000 |              90.389 |              106.527 |      1.255 |
|  10000 |             215.160 |              260.712 |      1.714 |
|  20000 |             321.465 |              496.245 |      6.784 |
|  50000 |            1194.417 |              716.461 |      9.328 |
| 200000 |            4911.916 |             6372.585 |    126.687 |
 





- **1b.**

The asymptotic run time of qsort_fixed is O(n^2), the expected runtime of qsort_random is O(n). We see qsort_fixed follow its expected runtime, while qsort_random performs worse than we would expect, but performs better in some cases compared to qsort_fixed. Overall, the two are quite comparable.




- **1c.**
Timsort wildly outperforms both qsort_fixed and qsort_random. Timsort appears to grow logarithmically as a factor of the input size n,, much better than the previous examples.