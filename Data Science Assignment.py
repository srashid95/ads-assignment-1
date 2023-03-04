#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:01:56 2023

@author: saniarashid1
"""

import pandas as pd
import matplotlib.pyplot as plt
import random


def line_plot(data, title):
    """
    Parameters
    ----------
    data : DataFrame
        It contains the data for countries and their number of users in a
        specific year who use internet.
    title: String
        Title of graph
    Returns
    -------
    None.
    This function creates a multiple-line graph to display the trend of
    internet usage in multiple countries depending on the number of 
    users.
    
    """
    for cnt in data.columns[:7]:
        if cnt == 'Year':
            continue
        plt.plot(data['Year'], data[cnt], label=cnt)
    plt.xlabel('Year')
    plt.ylabel("Users")
    plt.title(title)
    
    # add the legend
    plt.legend()
    plt.show()
    
    return


def division_pie_plot(data, title):
    """
    Parameters
    ----------
    data : DataFrame
        Data for pie plot.
    title: String
        Title for graph
        
    This function plots a pie graph for some countries to display internet
    users division in those countries. In this case, we suppose that the sum
    of population for these countries is 100%
    Returns
    -------
    None.

    """
    data_1990 = data.iloc[0, :]  # Get data for first row
    data_1990 = data_1990[0:4]  # Get only first 4 countries for specified year

    # Get percentage for each country population for internet usage
    data_percentages = (data_1990 / data_1990.sum()) * 100

    plt.pie(data_percentages, labels=data_percentages.index, autopct='%1.1f%%',
            startangle=90)
    plt.axis('equal')
    plt.title(title)
    plt.show()
    
    return


def gdp_bar_plot(data, title, xlabel, ylabel):
    """
    Parameters
    ----------
    data : DataFrame
        having data for country's GDP.
    title : String
        Title for graph.
    xlabel : String
        lable for x-axis.
    ylabel : String
        label for y-axis.

    Returns
    -------
    None.

    """

    # Remove the extra columns
    plot = data.iloc[4:].plot(kind='bar', figsize=(12, 8), width=0.5)

    plot.set_xlabel("Year")
    plot.set_ylabel("GDP per capita (US$)")
    plot.set_title(title)

    # Draw graph
    plt.show()
    
    return


# Source: https://www.kaggle.com/datasets/pavan9065/internet-usage
internet_users_data = pd.read_csv("/Users/saniarashid1/Downloads" +
                                  "/number-of-internet-users-by-country.csv")
internet_users_data = pd.DataFrame(internet_users_data)

# store the number of internet users' column name in a variable
users_column_name = 'Number of internet users (OWID based on WB & UN)'

# Converted Rows in columns so that we can use the data in line plot
formatted_data = internet_users_data.pivot_table(index='Year',
                                                 columns='Entity',
                                                 values=users_column_name)

# Deleted all the columns containing NaN values
formatted_data = formatted_data.dropna(axis=1)
formatted_data['Year'] = formatted_data.index

# Plot a line graph
line_plot(formatted_data, "Change in Internet Users from 1990 to 2015")
division_pie_plot(formatted_data, "Internet users Distribution in some countries"
                  )


# GDP data
gdp_data = pd.read_csv("/Users/saniarashid1/Downloads" +
                       "/API_NY.GDP.PCAP.CD_DS2_en_csv_v2_4888903 _Cleaned.csv"
                       )
gdp_data = pd.DataFrame(gdp_data)

# Cleaning data by dropping rows having NaN values
gdp_data = gdp_data.dropna()

# Selecting a random Country
country = gdp_data.iloc[random.randint(0, len(gdp_data)), :]

country_name = country['Country Name']
graph_title = "GDP for " + country_name
gdp_bar_plot(country, graph_title, 'Year', "GDP per capita (US$)")
