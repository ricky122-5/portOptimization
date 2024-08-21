# src/optimization.py

import numpy as np
from scipy.optimize import minimize

def portfolio_variance(weights, cov_matrix):
    return np.dot(weights.T, np.dot(cov_matrix, weights))

def portfolio_return(weights, mean_returns):
    return np.sum(mean_returns * weights)


def minimize_variance(mean_returns, cov_matrix, target_return, sector_weights=None):
    num_assets = len(mean_returns)
    args = (cov_matrix,)

    constraints = [
        {'type': 'eq', 'fun': lambda x: portfolio_return(x, mean_returns) - target_return},
        {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
    ]

    bounds = tuple((0, 0.3) for asset in range(num_assets))

    if sector_weights:
        for sector, max_weight in sector_weights.items():
            constraints.append({'type': 'ineq', 'fun': lambda x: max_weight - np.sum(x[sector])})

    result = minimize(portfolio_variance, num_assets * [1. / num_assets, ], args=args,
                      method='SLSQP', bounds=bounds, constraints=constraints)
    return result.x
