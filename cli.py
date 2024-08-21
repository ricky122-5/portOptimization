# cli.py

import argparse

import numpy as np

import src.data_collection as dc
import src.optimization as opt
import src.visualization as vis


def print_portfolio_results(weights, tickers, mean_returns, cov_matrix):
    rounded_weights = np.round(weights, 2)
    print("\nOptimal Weights:")
    for i, ticker in enumerate(tickers):
        if rounded_weights[i] > 0.01:
            print(f"- {ticker}: {rounded_weights[i] * 100:.2f}%")

    portfolio_return = opt.portfolio_return(weights, mean_returns)
    portfolio_risk = np.sqrt(opt.portfolio_variance(weights, cov_matrix))
    sharpe_ratio = portfolio_return / portfolio_risk

    print(f"\nPortfolio Return: {portfolio_return:.4f} (or {portfolio_return * 100:.2f}%)")
    print(f"Risk: {portfolio_risk:.4f} (or {portfolio_risk * 100:.2f}%)")
    print(f"Sharpe Ratio: {sharpe_ratio:.4f}")

def main():
    parser = argparse.ArgumentParser(description="Portfolio Optimization Tool")
    parser.add_argument('--tickers', type=str, required=True, help='Comma-separated list of ticker symbols')
    parser.add_argument('--start', type=str, required=True, help='Start date in YYYY-MM-DD format')
    parser.add_argument('--end', type=str, required=True, help='End date in YYYY-MM-DD format')
    parser.add_argument('--target_return', type=float, help='Target return for optimization')

    args = parser.parse_args()

    tickers = args.tickers.split(',')
    start_date = args.start
    end_date = args.end
    target_return = args.target_return

    print(f"Fetching data for tickers: {tickers}")
    data = dc.fetch_data(tickers, start_date, end_date)
    mean_returns, cov_matrix = dc.calculate_returns(data)

    if target_return:
        print(f"Optimizing portfolio for target return: {target_return}")
        weights = opt.minimize_variance(mean_returns, cov_matrix, target_return)
        print_portfolio_results(weights, tickers, mean_returns, cov_matrix)
    else:
        print("Generating Efficient Frontier...")
        portfolios = []
        for tr in np.linspace(mean_returns.min(), mean_returns.max(), 100):
            weights = opt.minimize_variance(mean_returns, cov_matrix, tr)
            portfolios.append({
                'return': opt.portfolio_return(weights, mean_returns),
                'risk': np.sqrt(opt.portfolio_variance(weights, cov_matrix)),
                'sharpe': opt.portfolio_return(weights, mean_returns) / np.sqrt(opt.portfolio_variance(weights, cov_matrix))
            })

        returns = [p['return'] for p in portfolios]
        risks = [p['risk'] for p in portfolios]
        sharpe_ratios = [p['sharpe'] for p in portfolios]

        vis.plot_efficient_frontier(returns, risks, sharpe_ratios, portfolios)

if __name__ == '__main__':
    main()
