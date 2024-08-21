# src/visualization.py

import matplotlib.pyplot as plt


def plot_efficient_frontier(returns, risks, sharpe_ratios, portfolios):
    plt.figure(figsize=(10, 6))
    plt.scatter(risks, returns, c=sharpe_ratios, cmap='viridis')
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Risk (Std. Deviation)')
    plt.ylabel('Return')
    plt.title('Efficient Frontier')
    plt.show()
