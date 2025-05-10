import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

url1 = 'data.csv'
df1 = pd.read_csv(url1)
url2 = 'screen_time.csv'
df2 = pd.read_csv(url2)

screen_time_order = ['Less than 2', '2–4', '4–6', '6–8', '8-10', 'More than 10']
age_group_order = ['Below 18', '18–24', '25–34', '35–44', '45 and above']

df1['Average Screen Time'] = pd.Categorical(df1['Average Screen Time'], categories=screen_time_order, ordered=True)
df1['Age Group'] = pd.Categorical(df1['Age Group'], categories=age_group_order, ordered=True)

grouped = df1.groupby(['Age Group', 'Average Screen Time'], observed=False).size().reset_index(name='Count')
pivot_df = grouped.pivot(index='Age Group', columns='Average Screen Time', values='Count').fillna(0)



def makeGraph2():
    fig = go.Figure(data=go.Heatmap(
        z=pivot_df.values,
        x=pivot_df.columns,
        y=pivot_df.index,
        colorscale='YlOrRd'))  # Yellow to Red
    fig.update_layout(title="Heatmap of Respondents",
                      xaxis_title="Screen Time", 
                      yaxis_title="Age Group")
    return fig
