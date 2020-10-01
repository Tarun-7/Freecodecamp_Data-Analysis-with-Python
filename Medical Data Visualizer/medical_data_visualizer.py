import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

bmi = (df['weight']/ (df['height']/ 100)**2)

a = []
for x in bmi:
    if x > 25 :
        a.append(1) 
    else:
        a.append(0) 

# Add 'overweight' column
df['overweight'] = pd.Series(a)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'][df['cholesterol'] == 1] = 0
df['gluc'][df['gluc'] == 1] = 0

df['cholesterol'][df['cholesterol'] > 1] = 1
df['gluc'][df['gluc'] > 1] = 1


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.melt(df,id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
    
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=df_cat, x='variable', hue='value', kind='count', col='cardio')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat[df['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat[df['height'] <= df['height'].quantile(0.975)]
    df_heat = df_heat[df['weight'] >= df['weight'].quantile(0.025)]
    df_heat = df_heat[df['weight'] <= df['weight'].quantile(0.975)]


    # Calculate the correlation matrix
    corr =  df_heat.corr()
    

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
