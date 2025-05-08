import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url1 = 'data.csv'
df1 = pd.read_csv(url1)
url2 = 'screen_time.csv'
df2 = pd.read_csv(url2)

attention_map = {
    "Less than 10 minutes": 5,
    "10–30 minutes": 20,
    "30–60 minutes": 45,
    "More than 1 hour": 75
}
df1["Attention_numeric"] = df1["Attention Span"].map(attention_map)

def makeGraph5_1():
    usage_simple = df1['Usage of Productivity Apps'].fillna('').apply(lambda x: 'Yes' if x.strip().lower().startswith('yes') else 'No')

    # Count occurrences
    counts = usage_simple.value_counts()

    # Plot
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', colors=['lightblue', 'lightgreen'], startangle=90)
    ax.set_title('Productivity App Usage (Yes vs No)')
    ax.axis('equal')  # Equal aspect ratio makes the pie round
    plt.close(fig)
    return fig

def makeGraph5_2():
    df1["Productivity_Usage_Simple"] = df1["Usage of Productivity Apps"].map(lambda x: "Yes" if "Yes" in x else "No")
    age_groups = sorted(df1["Age Group"].unique(), key=lambda x: int(x.split('-')[0]) if '-' in x else 100)
    grouped = df1.groupby(['Productivity_Usage_Simple', 'Age Group'])['Attention_numeric'].mean().unstack()
    labels = age_groups
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]
    yes_values = grouped.loc['Yes', labels].fillna(0).tolist() + [grouped.loc['Yes', labels].fillna(0).tolist()[0]]
    no_values = grouped.loc['No', labels].fillna(0).tolist() + [grouped.loc['No', labels].fillna(0).tolist()[0]]
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, yes_values, label="Yes", color="dodgerblue", linewidth=2)
    ax.fill(angles, yes_values, color="dodgerblue", alpha=0.4)
    ax.plot(angles, no_values, label="No", color="deepskyblue", linewidth=2)
    ax.fill(angles, no_values, color="deepskyblue", alpha=0.3)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_yticks([0, 20, 40, 60, 80])
    ax.set_yticklabels(['0', '20', '40', '60', '80'])
    ax.set_ylim(0, max(max(yes_values), max(no_values)))
    ax.set_title("Which ages do and do not use productivity apps?")
    ax.legend(loc='lower right', bbox_to_anchor=(1.25, -0.1))
    return fig
