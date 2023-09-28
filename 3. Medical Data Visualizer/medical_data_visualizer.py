'''
Project No.: 3
Project Title: Medical Data Visualizer
Date Completed: 2023-03-25



Instructions: 
    The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices. Use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

    Create a chart that shows the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients with cardio = 1 and cardio = 0 in different panels.

    Use the data to complete the following tasks in medical_data_visualizer.py:

        - Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
        - Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.
        - Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by 'Cardio' so there is one chart for each cardio value.
        - Clean the data. Filter out the following patient segments that represent incorrect data:
            - diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
            - height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
            - height is more than the 97.5th percentile
            - weight is less than the 2.5th percentile
            - weight is more than the 97.5th percentile

    Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap() and mask the upper triangle.
'''


# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns





# Importing the data
df = pd.read_csv('medical_examination.csv')


# Removes .loc errors
pd.set_option(
    'mode.chained_assignment', 
    None
    )


# Add 'overweight' column
df['bmi'] = df['weight'] / ((df['height'] / 100 ) ** 2)

df['overweight'] = 0
df['overweight'].loc[df['bmi'] > 25] = 1

df = df.drop(columns = ['bmi'])


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'].loc[df['cholesterol'] == 1] = 0
df['cholesterol'].loc[df['cholesterol'] > 1] = 1

df['gluc'].loc[df['gluc'] == 1] = 0
df['gluc'].loc[df['gluc'] > 1] = 1



def draw_cat_plot():
    
    # Converting df to long format
    df_cat = pd.melt(
        frame = df,
        id_vars = ['cardio'],
        value_vars = [
            'active',
            'alco',
            'cholesterol',
            'gluc',
            'overweight',
            'smoke'
            ]
        )


    # Creating the viz itself
    sns.set_theme()

    catplot = sns.catplot(
            data = df_cat,
            x = 'variable',
            hue = 'value',
            col = 'cardio',
            kind = 'count'
        )

    catplot.set_axis_labels('variable','total')
    fig = catplot.fig



    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig





def draw_heat_map():
    
    # Cleaning the data
    df_heat = df.loc[df['ap_lo'] <= df['ap_hi']]

    df_heat = df_heat.loc[df['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat.loc[df['height'] <= df['height'].quantile(0.975)]

    df_heat = df_heat.loc[df['weight'] >= df['weight'].quantile(0.025)]
    df_heat = df_heat.loc[df['weight'] <= df['weight'].quantile(0.975)]



    # Generate a mask for the upper triangle
    mask = np.zeros_like(df_heat.corr())
    mask[np.triu_indices_from(mask)] = True

    # Creating the viz itself
    fig, ax = plt.subplots()
    fig = plt.figure(figsize = (8, 10))

    heatmap = sns.heatmap(
        data = df_heat.corr(), 
        fmt = '0.1f',
        annot = True,
        annot_kws = {'fontsize': 9},
        linewidths = 0.5,
        linecolor = "white",
        square = True,
        mask = mask
        )



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig