import pandas as pd

df = pd.read_csv("Instagram data.csv", encoding='latin1')


# Quick look at data
print(df.head())
print(df.info())
print(df.describe(include='all'))

df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Check for nulls
print(df.isnull().sum())

# Fill or drop missing values (based on context)
df.fillna(method='ffill', inplace=True)

import matplotlib.pyplot as plt
import seaborn as sns

# Add a short caption preview column
df['Caption_Preview'] = df['Caption'].str.slice(0, 40) + '...'

top_follows = df.sort_values(by='Follows', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(y='Caption_Preview', x='Follows', data=top_follows, palette='magma')
plt.title("Top 10 Posts by Follows Gained")
plt.xlabel("Follows")
plt.ylabel("Caption Preview")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Impressions', y='Likes', data=df)
plt.title("Likes vs Impressions")
plt.xlabel("Impressions")
plt.ylabel("Likes")
plt.grid(True)
plt.tight_layout()
plt.show()

df['Engagement_Rate'] = ((df['Likes'] + df['Comments'] + df['Shares'] + df['Saves']) / df['Impressions']) * 100

top_engaged = df.sort_values(by='Engagement_Rate', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(y='Caption_Preview', x='Engagement_Rate', data=top_engaged, palette='coolwarm')
plt.title("Top 10 Posts by Engagement Rate (%)")
plt.xlabel("Engagement Rate (%)")
plt.ylabel("Caption Preview")
plt.tight_layout()
plt.show()


plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='YlOrRd')
plt.title("Correlation Between Metrics")
plt.tight_layout()
plt.show()


