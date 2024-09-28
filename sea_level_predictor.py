import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')
    
    # Create first line of best fit (using all data)
    slope_all, intercept_all, r_value_all, p_value_all, std_err_all = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred_all = intercept_all + slope_all * years_extended
    plt.plot(years_extended, sea_level_pred_all, color='red', label='Best Fit Line (1880-2050)')
    
    # Create second line of best fit (using data from year 2000 onwards)
    data_recent = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = pd.Series(range(2000, 2051))
    sea_level_pred_recent = intercept_recent + slope_recent * years_recent_extended
    plt.plot(years_recent_extended, sea_level_pred_recent, color='green', label='Best Fit Line (2000-2050)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True)

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()