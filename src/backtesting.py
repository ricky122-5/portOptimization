# src/backtesting.py

import pandas as pd

def backtest_portfolio(weights, data):
    returns = data.pct_change().dropna()
    portfolio_returns = returns.dot(weights)
    cumulative_returns = (1 + portfolio_returns).cumprod()
    return cumulative_returns

def compare_with_benchmark(portfolio_cum_returns, benchmark_data):
    benchmark_returns = (1 + benchmark_data.pct_change().dropna()).cumprod()
    comparison = pd.DataFrame({
        'Portfolio': portfolio_cum_returns,
        'Benchmark': benchmark_returns
    })
    comparison.plot(title='Portfolio vs Benchmark')
