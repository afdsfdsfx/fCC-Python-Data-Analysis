'''
Project No.: 5
Project Title: Sea Level Predictor
Date Completed: 2023-05-03



Instructions: 
    You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.

    Use the data to complete the following tasks:

    - Use Pandas to import the data from epa-sea-level.csv.
    - Use Matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    - Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
    - Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    - The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
'''


# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress





def draw_plot():

    # Importing the data
    df = pd.read_csv(
        'epa_sea_level.csv',
        header = 0
        )



    # Scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.figure(
        figsize = (10, 6),
        dpi = 100
        )

    plt.scatter(
        x = x,
        y = y,
        c = 'cyan'
        )



    # 1st regression line
    x_2050 = pd.Series(
        range(2014, 2051), 
        dtype = 'int64',
        name = 'Year'
        )

    df_1 = df.copy()

    df_1 = df.merge(
        right = x_2050,
        on = ['Year'], 
        how = 'outer'
        )
    
    line_1 = linregress(
        x = x,
        y = y
        )

    m_1 = line_1.slope
    b_1 = line_1.intercept

    x_1 = df_1['Year']
    y_1 = (m_1 * x_1) + b_1



    plt.plot(
        x_1,
        y_1,
        'r-'
        )

    

    # 2nd regression line
    df_2 = df_1.copy().loc[df_1['Year'] > 1999]

    line_2 = linregress(
        x = df_2['Year'].loc[df_2['Year'] <= 2013],
        y = df_2['CSIRO Adjusted Sea Level'].loc[df_2['Year'] <= 2013],
        )

    m_2 = line_2.slope
    b_2 = line_2.intercept

    x_2 = df_2['Year']
    y_2 = (m_2 * x_2) + b_2



    plt.plot(
        x_2,
        y_2,
        'g-'
        )



    # Add labels and title
    plt.title(
        label = 'Rise in Sea Level',
        pad = 15
        )

    plt.xlabel(
        xlabel = 'Year',
        labelpad = 15
        )

    plt.ylabel(
        ylabel = 'Sea Level (inches)', 
        labelpad = 15
        )





    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()