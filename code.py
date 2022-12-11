import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#handling dataset
def manipulate_data(path):
    ''' the Function is used for generating two dataset with country and year as columns
    parameters: Path- path of the dataset.
    returns: two dataframes.
    '''
    temp_df = pd.read_csv(path)
    temp_df=temp_df.drop(columns=['Indicator Code','Country Code'])
    temp2_df = temp_df.transpose()
    temp2_df.columns = temp2_df.iloc[0].values.tolist()
    temp2_df=temp2_df.iloc[1:]
    return temp_df,temp2_df

country_data,year_data=manipulate_data('climate_data.csv')

columns=year_data.iloc[0].unique()

asian_countries=['China','India','Russian Federation','Japan']

country_select=year_data[asian_countries]

#plotting bar graphs
def bars_plot(data_input,indicator):
    '''
    The function is used to plot the bar graphs for the given data and its indicators
    parameters: data_input- dataset, indicator- indicators to plot
    '''
    temp=[]
    c= indicator
    for i in range(4):
        temp.append(data_input.iloc[:,c])
        i=i+1
        c=c+76
    d= pd.DataFrame(temp)
    d=d.iloc[:,1:]
    d=d.transpose()
    d.iloc[[30,40,50,58]].plot(kind='bar',figsize=(15,8),xlabel='Years',ylabel=columns[indicator],title=columns[indicator]+' from 1990 to 2019')
    plt.show()
bars_plot(country_select,0)
bars_plot(country_select,44)

#plotting correlation
country=year_data[['India']]
temp=[]
indicators_index=[0,10,11,49,67,44]
for i in indicators_index:
    temp.append(country.iloc[:,i])
d= pd.DataFrame(temp)
d=d.transpose()
d.columns=d.iloc[0]
d=d[31:60]
d=d[1:]
d=d.fillna(d.median())
ax = sns.heatmap(
    d.corr(), 
    cmap="YlGnBu", annot=True
)
plt.title(" India indicators correlation")
plt.show()

#plotting correlation
country=year_data[['Japan']]
temp=[]
indicators_index=[0,10,11,49,67,44]
for i in indicators_index:
    temp.append(country.iloc[:,i])
d= pd.DataFrame(temp)
d=d.transpose()
d.columns=d.iloc[0]
d=d[31:60]

d=d.fillna(d.median())
ax = sns.heatmap(
    d.corr(), 
    cmap="YlGnBu", annot=True
)
plt.title(" Japan indicators correlation")
plt.show()

#plotting line graph
def line_plot(data_input,indicator):
    '''
    The function is used to plot the line graphs for the given data and its indicators
    parameters: data_input- dataset, indicator- indicators to plot
    '''
    temp=[]
    c= indicator
    for i in range(4):
        temp.append(data_input.iloc[:,c])
        i=i+1
        c=c+76
    d= pd.DataFrame(temp)
    d=d.iloc[:,1:]
    d=d.transpose()
    d.iloc[30:58].plot(kind='line',figsize=(15,8),xlabel='Years',ylabel=columns[indicator],title=columns[indicator]+' from 1990 to 2015')
    plt.show()

line_plot(country_select,58)
line_plot(country_select,47)







