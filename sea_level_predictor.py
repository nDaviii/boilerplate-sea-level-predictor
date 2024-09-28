import pandas as pd 
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Observed Data')

    # Create first line of best fit (using all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))  # Years from 1880 to 2050
    sea_level_fit_all = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_fit_all, color='orange', label='Best Fit Line (All Data)')

    # Create second line of best fit (using data from year 2000 onward)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = pd.Series(range(2000, 2051))  # Years from 2000 to 2050
    sea_level_fit_recent = slope_recent * years_recent_extended + intercept_recent
    plt.plot(years_recent_extended, sea_level_fit_recent, color='red', label='Best Fit Line (2000 Onwards)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Call the function to generate the plot
draw_plot()
