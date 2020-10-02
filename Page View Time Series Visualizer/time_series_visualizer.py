import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date', parse_dates=['date'])

# Clean data
df = df[df['value'] >= df['value'].quantile(0.025)]
df = df[df['value'] <= df['value'].quantile(0.975)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20,8))

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    sns.lineplot(data=df, x="date", y="value")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.reset_index()
    #df_bar = df
    df_bar['year']= pd.DatetimeIndex(df_bar['date']).year
    df_bar['month']= pd.DatetimeIndex(df_bar['date']).month_name() 

    # Draw bar plot

    fig, ax = plt.subplots(figsize=(12,8))

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')


    sns.barplot(x='year', y='value', data = df_bar, hue='month')
    ax.legend(title = 'Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, ax = plt.subplots(figsize=(18,5))

    plt.subplot(1, 2, 1)

    plt.title('Year-wise Box Plot (Trend)')
    sns.boxplot(x='year', y='value', data = df_box)

    plt.subplot(1, 2, 2)

    plt.title('Month-wise Box Plot (Seasonality)')
    sns.boxplot(x='month', y='value', data = df_box)
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
