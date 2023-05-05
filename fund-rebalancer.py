import numpy as np
from scipy.optimize import minimize

# Inputs
fund_names = np.array(["SWISX", "SWTSX", "SWAGX"])
current_values = np.array([9236.59, 25511.75, 1804.51])  # Current values of A, B, and C
desired_allocation = np.array([0.25, 0.7, 0.05])  # Desired allocation for A, B, and C
new_investment = 8000  # Additional investment amount

# Calculate total current value
total_value = np.sum(current_values)
total_new_value = total_value + new_investment

# Objective function to minimize
def deviation(x):
    new_values = current_values + x
    total_new_value = total_value + new_investment
    actual_allocation = new_values / total_new_value
    return np.sum((actual_allocation - desired_allocation) ** 2)

# Constraints and bounds
cons = {'type': 'eq', 'fun': lambda x: np.sum(x) - new_investment}
bounds = [(0, new_investment) for _ in range(3)]

# Initial guess
initial_guess = new_investment * desired_allocation

# Solve the optimization problem using the SLSQP solver
result = minimize(deviation, initial_guess, constraints=cons, bounds=bounds, method='SLSQP')

# Print the results
new_values = current_values + result.x
print('\t'.join(fund_names))
print("Optimal investment amounts:", result.x)
print('Prior allocations:', current_values / total_value)
print('New allocations:', new_values / total_new_value)
