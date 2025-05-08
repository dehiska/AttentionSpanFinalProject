import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    fig, ax = plt.subplots(figsize=(10, 6))
    for age_group in age_group_order:
        ax.plot(screen_time_order, pivot_df.loc[age_group], marker='o', label=age_group)
    ax.set_xlabel('Average Screen Time (hours)')
    ax.set_ylabel('Number of Respondents')
    ax.set_title('Screen Time Distribution by Age Group')
    ax.legend(title='Age Group')
    ax.grid(True)
    ax.set_xticks(range(len(screen_time_order)))
    ax.set_xticklabels(screen_time_order, rotation=45)
    return fig
