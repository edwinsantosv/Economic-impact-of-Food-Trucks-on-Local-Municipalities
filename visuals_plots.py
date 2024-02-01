import matplotlib.pyplot as plt
import pygwalker as pyg
import numpy as np
import seaborn as sns
import sweetviz as sv


def barplot(x,y,data):


    catplot=sns.catplot(x=x, y=y, data=data)  # Use row instead of col


    # Rotate x-axis labels (bottom labels) to a specified angle (e.g., 45 degrees)
    catplot.set_xticklabels( rotation=45, horizontalalignment='right')


    # Add labels to each bar
    for ax in catplot.axes.flat:
        for p in ax.patches:
            ax.text(p.get_x() + p.get_width() / 2., p.get_height(), f'{p.get_height():.1f}', 
                    ha='center', va='bottom', rotation=90)