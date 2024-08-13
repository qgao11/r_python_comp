import numpy as np
from scipy import stats
from scipy.stats import mannwhitneyu

# KMT2D blood glucose levels
kmt2d_glucose = np.array([0.78, 1.2, 0.6, 1.7, 0.7, 1.0, 1.33, 0.85, 1.4, 1.5, 0.95, 1.25])

# KDM6A blood glucose levels
kdm6a_glucose = np.array([0.87, 0.66, 0.92, 1.21, 0.63, 0.63, 1.23, 0.96, 0.55, 0.88, 0.55, 0.55])

# Perform an independent t-test
t_stat, p_value = stats.ttest_ind(kmt2d_glucose, kdm6a_glucose)

print("t-statistic:", t_stat)
print("p-value:", p_value)


# Check variance assumptions
t_stat, p_value_equal_var = stats.ttest_ind(kmt2d_glucose, kdm6a_glucose, equal_var=True)
print(p_value_equal_var)

# Check normality assumptions
u_stat, p_value_mannwhitney = mannwhitneyu(kmt2d_glucose, kdm6a_glucose, alternative='two-sided')
print(p_value_mannwhitney)
