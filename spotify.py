#-------------Setup & Data Preprocessing:-----------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
import math

#Load dataset:
file_path="D:\VS CODE\AI & DATA SCIENCE\DATA SETS\Spotify_2024_Global_Streaming_Data.csv"
df=pd.read_csv(file_path)

print("Dataset:")
print(df,"\n")

#Display basic info:
print('Display Basic info:')
print(df.info(),'\n')

#Drop null & Duplicate valuse in dataset:
print('Drop Null valuse in dataset:')
print(df.isnull(),'\n')

print('After removing null values in the dataset:')
print(df.dropna(),'\n')

print("After removing Duplicates:")
print(df.drop_duplicates(),'\n')

#view first 10 rows in the dataset:
print(df.head(21),'\n') 

#dataset columns:
print('Dataset Columns:')
print(df.columns,"\n")

print("Count of each rows in the columns:")
print(df.count(),'\n')

#dataset in transpose form:
print("view data in transpose:")
print(df.transpose(),'\n')


#finding missing values in columns:
print('null valuse:')
print(df.isnull().sum(),'\n')

print("finding missing values in columns:")
print(df.isnull().sum(axis=1),"\n")

#specific remdon column wise:
column_name='Total Hours Streamed (Millions)'

#Round up Value
data=df[column_name].apply(math.ceil).dropna()

#Round down Value
'''data=df[column_name].apply(math.floor).dropna()'''

#Using String Manipulation (Remove Decimal Without Rounding)
'''data=df[column_name].split('.')[0]'''

#Using int() (Truncate the decimal)
'''data=df.int([column_name])'''

#Using math.floor() (Round Down)
'''data=df.math.floor([column_name])'''

# Using math.ceil() (Round Up)
'''data=df.math.ceil([column_name])'''

#Using round() (Round to the nearest whole number)
'''data=df.round([column_name])'''

#Using statistics to find Mean, Median, Mode:

mean_value=statistics.mean(data)
median_value=statistics.median(data)
Mode_value=statistics.mode(data)
range_value=max(data)-min(data)
variance_value=statistics.variance(data)
std_dev_value=statistics.stdev(data)

#Statistics values:

print('Print Results:')
print(f'mean: {mean_value}')
print(f'median: {median_value}')
print(f'mode: {Mode_value}')
print(f'range: {range_value}')
print(f'sample variance: {variance_value}')
print(f'sample standard derivation: {std_dev_value}\n')

#convert data types in needed:
df['Total Streams (Millions)']=pd.to_numeric(df['Total Streams (Millions)'],errors='coerce')

print("Data types in needed:")
print(df['Total Streams (Millions)'],'\n')

df['Monthly Listeners (Millions)']=pd.to_numeric(df['Monthly Listeners (Millions)'],errors='coerce')
print("Data types in needed:")

print(df['Monthly Listeners (Millions)'],'\n')

#-------------------Genre Popularity analysis:-----------------------

# Aggregate total streams per genre:
print("Aggregate Total strems per genre:")

genre_popularity=df.groupby("Genre")["Total Streams (Millions)"].sum().sort_values(ascending=False)
print(genre_popularity,'\n')

#------------------------Visualize top genres:-----------------------

#visualize top genres:      [1]
print("Visualize top genres:")
plt.figure(figsize=(12,6))
sns.barplot(x=genre_popularity.index, y=genre_popularity.values, color='lime') #orient="h") #=> seaborn horizontal bar chat just added this atribute in the syntax " orient='h' "
plt.xticks(rotation=40)
plt.xlabel("Genre")
plt.ylabel("Total Streams (Millions)")
plt.title("Top Streaming Genres")
plt.legend(["Genres",'Total Streams'])

plt.show()

#------------------------Last 30 days Streamed albums:----------------------

#Last 30 days Streamed alblums:
print("Last 30 days Streamed albums:")

album_Streaming=df.groupby("Album")['Streams Last 30 Days (Millions)'].sum().sort_values(ascending=False)
print(album_Streaming,'\n')

#                           [2]
plt.figure(figsize=(10,5))
sns.lineplot(x=album_Streaming.index, y=album_Streaming.values)
plt.xticks(rotation=45)
plt.xlabel("Album")
plt.ylabel("Streams Last 30 Days (Millions)")
plt.title("Last 30 days Streamed albums")
plt.legend(["Streams Last 30 Days (Millions)"])

plt.show()

#-----------------Skip Rate Impact Analysis:------------------------

# Correlation between Skip Rate and Total Streams:

#                           [3]
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["Skip Rate (%)"], y=df['Total Streams (Millions)'], color=['blue'],alpha=0.5)
plt.xlabel("Skip Rate (%)")
plt.ylabel("Total Streams (Millions)")
plt.title("Skip Rate vs. streaming Popularity")
plt.legend(['Skip Rate','streaming Popularity'])

plt.show()

#-----------------------Platform Type Comparison:-------------------------

# Streaming trends across Free & Premium platforms:
platform_popularity=df.groupby("Platform Type")["Total Streams (Millions)"].sum()
print(platform_popularity,'\n')

#                           [4]
#pie_chat:
plt.figure(figsize=(6,6))
platform_popularity.plot(kind="pie", colors=['lightgreen','salmon'])
plt.title('Total Streams by Plotform Type')
plt.ylabel("")
plt.legend(["Free",'Premium'])

plt.show()

#---------------------Genre Distribution Across Countries:------------------

#Aggregate total streams by country and genre:
genre_by_country=df.groupby(['Country','Genre'])['Total Streams (Millions)'].sum().unstack()

print('Genre Distribution Across Countries:')
print(genre_by_country,'\n')

#                           [5]
#Heatmap visualization:
plt.figure(figsize=(10,6))
sns.heatmap(genre_by_country, cmap='coolwarm',linewidths=0.5)
plt.xlabel('Genre')
plt.ylabel('Country')
plt.title('Genre Popularity Across Countries')

plt.show()

#--------------------Skip Rate Distribution Across Genres:-----------------

Skip_Rate_Across_Genre=df.groupby(['Genre','Skip Rate (%)'])['Total Streams (Millions)'].sum()
print(Skip_Rate_Across_Genre,'\n')

#                           [6]
# Box plot for skip rates
plt.figure(figsize=(10,6))
sns.boxplot(x=df['Genre'], y=df['Skip Rate (%)'],palette='muted')
plt.xticks(rotation=45)
plt.xlabel('Genre')
plt.ylabel('Skip Rate (%)')
plt.title("Skip Rate Distribution Across Genres")

plt.show()

#----------------------Streaming Trends Over Release Years:----------------

# total streams per release year:
Streams_by_year=df.groupby('Release Year')['Total Streams (Millions)'].sum()
print(Streams_by_year,'\n')

#                              [7]
#Line graph:
plt.figure(figsize=(10,6))
plt.plot(Streams_by_year.index, Streams_by_year.values, marker='o', linestyle='-', color='teal')
plt.xlabel('Release Year')
plt.ylabel('Total Streams (Millions)')
plt.title('Streaming Treands Over time')
plt.grid(False)

plt.show()

#-----------------------Streams vs. Monthly Listeners Correlation------------

#                               [8]
# Scatter plot for correlation analysis
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["Monthly Listeners (Millions)"], y=df["Total Streams (Millions)"], color='purple', alpha=0.6)
plt.xlabel("Monthly Listeners (Millions)")
plt.ylabel("Total Streams (Millions)")
plt.title("Monthly Listeners vs. Total Streams")

plt.show()