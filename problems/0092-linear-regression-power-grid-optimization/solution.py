import numpy as np
import math

def power_grid_forecast(consumption_data):
    # 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
    # 2) Perform linear regression on the detrended data.
    # 3) Predict day 15's base consumption.
    # 4) Add the day 15 fluctuation back.
    # 5) Round, then add a 5% safety margin (rounded up).
    # 6) Return the final integer.
    
    # Detrend the data
    y = []
    x = []
    for i in range(len(consumption_data)):
        # Subtract the fluctuation for each day
        # Note: use i+1 to match the problem description (days start from 1)
        val = consumption_data[i] - (10 * np.sin((2 * np.pi * (i+1)) / 10))
        y.append(val)
        x.append(i+1)  # Use days starting from 1
    
    # Convert to numpy arrays for easier computation
    x = np.array(x)
    y = np.array(y)
    
    # Linear regression calculations
    n = len(x)
    
    # Slope (m) calculation
    x_y_sum = np.sum(x * y)
    x_sum = np.sum(x