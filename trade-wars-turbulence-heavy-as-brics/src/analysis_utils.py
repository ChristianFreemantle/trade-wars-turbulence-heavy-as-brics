# Helper functions for analysis and visualization
Jupyter
import pandas as pd

#diplay scv, run python 3 in the same folder as csv file or add path from root directory
df = pd.read_csv("brics_trade_data_enriched_final.csv")
df.head()

#import software to help with visuals
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create trade balance chart
plt.figure(figsize=(12, 6))

for country in df['Country'].unique():
    country_data = df[df['Country'] == country]
    plt.plot(country_data['Year'], country_data['Trade_Balance'], label=country)

plt.title("Trade Balance Over Time (2010–2025)")
plt.xlabel("Year")
plt.ylabel("Trade Balance (USD Billion)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#create GDP Growth by country chart
plt.figure(figsize=(12, 6))

for country in df['Country'].unique():
    country_data = df[df['Country'] == country]
    plt.plot(country_data['Year'], country_data['GDP_USD_Trillion'], label=country)

plt.title("GDP Growth by Country (2010–2025)")
plt.xlabel("Year")
plt.ylabel("GDP (USD Trillion)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#create Sanctions impact pivot table 
pivot = df.pivot_table(index="Year", columns="Country", values="Sanctions_Impact_Index")
plt.figure(figsize=(10, 6))
sns.heatmap(pivot, annot=True, cmap="YlOrRd", linewidths=0.5)
plt.title("Sanctions Impact Index (2010–2025)")
plt.show()

#Create Correlation Heatmap: Economic Indicators & Sanctions pivot table figure
import seaborn as sns
import matplotlib.pyplot as plt

corr_df = df[[
    'GDP_USD_Trillion',
    'Exports_USD_Billion',
    'Imports_USD_Billion',
    'Trade_Balance',
    'Sanctions_Impact_Index',
    'Currency_Stability_Index'
]]

correlation = corr_df.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap: Economic Indicators & Sanctions")
plt.show()

#Create USA vs China: Trade Balance During the Trade War Figure Chart
import matplotlib.pyplot as plt


filtered_df = df[
    (df['Country'].isin(['USA', 'China'])) & 
    (df['Year'] >= 2010)
]


pivot_df = filtered_df.pivot(index='Year', columns='Country', values='Trade_Balance')


pivot_df.plot(kind='bar', figsize=(12, 6), colormap='Set2')
plt.title("USA vs China: Trade Balance During the Trade War (2010–2025)")
plt.xlabel("Year")
plt.ylabel("Trade Balance (USD Billion)")
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True)
plt.legend(title="Country")
plt.tight_layout()
plt.show()

#Create USA vs China: Imports & Exports figure bar charts
import matplotlib.pyplot as plt
import numpy as np


trade_data = df[(df['Country'].isin(['USA', 'China'])) & (df['Year'] >= 2010)]


exports = trade_data.pivot(index='Year', columns='Country', values='Exports_USD_Billion')
imports = trade_data.pivot(index='Year', columns='Country', values='Imports_USD_Billion')


years = exports.index
x = np.arange(len(years))  
width = 0.35  

fig, ax = plt.subplots(figsize=(14, 6))


ax.bar(x - width/2, exports['USA'], width, label='USA Exports', color='#1f77b4')
ax.bar(x + width/2, exports['China'], width, label='China Exports', color='#ff7f0e')


fig2, ax2 = plt.subplots(figsize=(14, 6))
ax2.bar(x - width/2, imports['USA'], width, label='USA Imports', color='#2ca02c')
ax2.bar(x + width/2, imports['China'], width, label='China Imports', color='#d62728')


ax.set_title('USA vs China: Exports (2010–2025)')
ax.set_xlabel('Year')
ax.set_ylabel('Exports (USD Billion)')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.grid(True)


ax2.set_title('USA vs China: Imports (2010–2025)')
ax2.set_xlabel('Year')
ax2.set_ylabel('Imports (USD Billion)')
ax2.set_xticks(x)
ax2.set_xticklabels(years)
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()

#create USA vs China — Trade War Dashboard 
import matplotlib.pyplot as plt
import numpy as np


trade_data = df[(df['Country'].isin(['USA', 'China'])) & (df['Year'] >= 2010)]
years = sorted(trade_data['Year'].unique())
x = np.arange(len(years))
width = 0.35


exports = trade_data.pivot(index='Year', columns='Country', values='Exports_USD_Billion')
imports = trade_data.pivot(index='Year', columns='Country', values='Imports_USD_Billion')
balance = trade_data.pivot(index='Year', columns='Country', values='Trade_Balance')


fig, axs = plt.subplots(1, 3, figsize=(20, 6), sharex=True)


axs[0].bar(x - width/2, exports['USA'], width, label='USA', color='#1f77b4')
axs[0].bar(x + width/2, exports['China'], width, label='China', color='#ff7f0e')
axs[0].set_title("Exports (USD Billion)")
axs[0].set_xticks(x)
axs[0].set_xticklabels(years)
axs[0].set_ylabel("Exports")
axs[0].legend()
axs[0].grid(True)

axs[1].bar(x - width/2, imports['USA'], width, label='USA', color='#2ca02c')
axs[1].bar(x + width/2, imports['China'], width, label='China', color='#d62728')
axs[1].set_title("Imports (USD Billion)")
axs[1].set_xticks(x)
axs[1].set_xticklabels(years)
axs[1].set_ylabel("Imports")
axs[1].legend()
axs[1].grid(True)


axs[2].bar(x - width/2, balance['USA'], width, label='USA', color='#9467bd')
axs[2].bar(x + width/2, balance['China'], width, label='China', color='#8c564b')
axs[2].set_title("Trade Balance (Exports - Imports)")
axs[2].set_xticks(x)
axs[2].set_xticklabels(years)
axs[2].set_ylabel("Trade Balance")
axs[2].axhline(0, color='black', linestyle='--', linewidth=0.8)
axs[2].legend()
axs[2].grid(True)


plt.suptitle("USA vs China — Trade War Dashboard (2018–2025)", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

#Create South Africa Trade Balance (2010–2025) — Government Impact Bar Chart
import matplotlib.pyplot as plt


sa_df = df[(df['Country'] == 'South Africa') & (df['Year'] >= 2010)]


plt.figure(figsize=(14, 6))
bars = plt.bar(
    sa_df['Year'],
    sa_df['Trade_Balance'],
    color=['green' if x > 0 else 'red' for x in sa_df['Trade_Balance']]
)

plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.title("South Africa Trade Balance (2010–2025) — Government Impact")
plt.xlabel("Year")
plt.ylabel("Trade Balance (USD Billion)")
plt.grid(axis='y', linestyle='--', linewidth=0.5)


for i, row in sa_df.iterrows():
    note = str(row['Notes'])
    y = row['Trade_Balance']
    
   
    short_note = note[:60] + "..." if len(note) > 60 else note
    if note.strip() and note != 'nan':
        plt.text(row['Year'], y + (1 if y > 0 else -2), short_note, ha='center', fontsize=7, rotation=90)

plt.tight_layout()
plt.show()
