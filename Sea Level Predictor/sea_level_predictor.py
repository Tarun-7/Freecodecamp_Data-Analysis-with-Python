import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (10,5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    x_pred = pd.Series([i for i in range(1880,2050)])
    y_pred = slope*x_pred + intercept

    plt.plot(x_pred, y_pred, "r", label='Predicted line from 1875')

    df_new = df.loc[df["Year"] >=2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])

    # Create second line of best fit
    x2_pred = pd.Series([i for i in range(2000,2050)])
    y2_pred = slope*x2_pred + intercept
    plt.plot(x2_pred, y2_pred, "g", label='Predicted line from 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()