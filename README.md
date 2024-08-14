# r_python_comp

By default, the built-in libraries in both Python (scipy.stats.ttest_ind) and R (t.test) use Welch's t-test which does not assume equal variances and assumes the data distributions are approximately normal. Therefore, there shouldn’t be any statistical significance in p-value calculation caused by the use of different languages. This code also calculates the p-value assuming equal variances and gets the same results.
