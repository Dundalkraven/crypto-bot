import pandas as pd
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
ax = plt.gca()


ax.type(exp)plot(max_drawdown_df['ticker'], max_drawdown_df['max_drawdown'], marker='o', linestyle='-', color='b', label='Max Drawdown')

# Title and labels
plt.title('Max Drawdown per Coin', fontsize=14)
plt.xlabel('Coin', fontsize=12)
plt.ylabel('Max Drawdown', fontsize=12)

# Annotating the points with the ticker names (coins)
for i, row in max_drawdown_df.iterrows():
    ax.text(row['ticker'], row['max_drawdown'], f"{row['ticker']}: {row['max_drawdown']:.2f}",
            ha='center', va='bottom', fontsize=10, color='black')

# Hide top and right spines
ax.spines[['top', 'right']].set_visible(False)

# Show grid for better readability
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()