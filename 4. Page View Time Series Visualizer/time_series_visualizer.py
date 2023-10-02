'''
Project No.: 4
Project Title: Page View Time Series Visualizer
Date Completed: 2023-04-26



Instructions: 
    For this project, you will visualize time series data using a line chart, bar chart, and box plots. You will use Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

    Use the data to complete the following tasks:

        - Use Pandas to import the data. Set the index to the date column.
        - Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
        - Create a draw_line_plot function that uses Matplotlib to draw a line chart. The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
        - Create a draw_bar_plot function that draws a bar chart. It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
        - Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots. These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly.
'''


# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime





# Importing the data
df = pd.read_csv(
    "fcc_forum_pageviews.csv", 
    parse_dates = True, 
    index_col = 'date'
    )



# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df.loc[
    (df['value'] <= df['value'].quantile(0.975)) & 
    (df['value'] >= df['value'].quantile(0.025))
    ]



def draw_line_plot():
    fig = plt.figure(
        figsize = (12, 8), 
        dpi= 100
        )

    plt.title(
        label = 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
        pad = 20
        )

    plt.xlabel(
        xlabel = 'Date',
        labelpad = 20
        )

    plt.ylabel(
        ylabel = 'Page Views',
        labelpad = 20
        )



    plt.plot(
        df.index,
        df['value'],
        'g-'
        )





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
    




def draw_bar_plot():
    plt.figure(
        figsize = (12, 8),
        dpi = 100
        )

    df_bar = df.copy()
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar = df_bar.groupby(by = ['year', 'month'])['value'].mean().unstack()



    fig = df_bar.plot.bar()
    fig = fig.figure

    label_month = ['January', 
                   'February', 
                   'March', 
                   'April', 
                   'May', 
                   'June', 
                   'July', 
                   'August', 
                   'September', 
                   'October', 
                   'November', 
                   'December'
                ]

    plt.xlabel(
        xlabel = 'Years',
        labelpad = 15,
        )

    plt.xticks(rotation = 0)

    plt.ylabel(
        ylabel = 'Average Page Views',
        labelpad = 15
        )

    plt.legend(
        title = 'Months', 
        labels = label_month
        )





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig





def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace = True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]


    
    fig, ax = plt.subplots(
        nrows = 1, 
        ncols = 2
        )
    
    sns.set(rc = {'figure.figsize' : (16, 6)})
    sns.set_style(style = 'white')



    sns.boxplot(
        data = df_box,
        x = df_box['year'],
        y = df_box['value'],
        ax = ax[0]
        ).set(title = 'Year-wise Box Plot (Trend)',
              xlabel = 'Year',
              ylabel = 'Page Views'
            )

    sns.boxplot(
        data = df_box,
        x = sorted(df_box['month'],
                   key = lambda m: datetime.strptime(m, "%b")
                ),
        y = df_box['value'],
        ax = ax[1]
        ).set(title = 'Month-wise Box Plot (Seasonality)',
              xlabel = 'Month',
              ylabel = 'Page Views'
            )
    



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig