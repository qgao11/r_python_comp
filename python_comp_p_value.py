import numpy as np
from scipy import stats

# KMT2D blood glucose levels
kmt2d_glucose = np.array([0.78, 1.2, 0.6, 1.7, 0.7, 1.0, 1.33, 0.85, 1.4, 1.5, 0.95, 1.25])

# KDM6A blood glucose levels
kdm6a_glucose = np.array([0.87, 0.66, 0.92, 1.21, 0.63, 0.63, 1.23, 0.96, 0.55, 0.88, 0.55, 0.55])

# Perform an independent t-test
t_stat, p_value = stats.ttest_ind(kmt2d_glucose, kdm6a_glucose)

# Print the t-test results
print("t-statistic:", t_stat)
print("p-value:", p_value)

# Display the p-value
print(f"The p-value is: {p_value:.5f}")
