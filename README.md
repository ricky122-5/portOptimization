# Portfolio Optimization Tool

## Overview

The Portfolio Optimization Tool is a Python-based application that uses Modern Portfolio Theory (MPT) to optimize a portfolio of financial assets. The tool allows users to input various assets, collect historical price data, and compute the optimal asset allocation that maximizes return for a given level of risk (or minimizes risk for a given level of return). The tool also provides visualizations, including the efficient frontier, which shows the trade-off between risk and return.

## Key Features

- **Data Collection**: Automatically fetch historical price data for a wide range of assets using APIs like Yahoo Finance.
- **Mean-Variance Optimization**: Implement the mean-variance optimization algorithm to calculate the optimal portfolio.
- **Efficient Frontier**: Visualize the efficient frontier, displaying the relationship between expected return and risk.
- **Customizable Constraints**: Apply constraints such as maximum allocation per asset or sector, no short-selling, and minimum allocation requirements.
- **Backtesting**: Test the performance of the optimized portfolio against historical data.
- **User Interface**: Interact with the tool via a command-line interface (CLI).

## Mathematical Optimization Process

### Objective of the Optimization

The goal of portfolio optimization is to determine the best possible allocation of assets that either maximizes return for a given level of risk or minimizes risk for a given level of return. This is achieved through the mathematical process known as **mean-variance optimization**.


### Solving the Optimization Problem

The portfolio optimization problem is solved using **Quadratic Programming (QP)**, where the objective is to minimize portfolio variance (risk) while satisfying the constraints. The optimization uses algorithms like **Sequential Least Squares Programming (SLSQP)** to iteratively adjust asset weights until the optimal solution is found.

### Efficient Frontier Calculation

To generate the efficient frontier, the optimization process is repeated for different target returns. By varying the target return, the efficient frontier shows the optimal trade-off between risk and return for a portfolio.

### Handling Constraints

The project allows for the inclusion of various constraints, such as:
- **Maximum or Minimum Weights:** Limiting the allocation to specific assets or sectors.
- **No Short-Selling:** Ensuring all weights are non-negative.
- **Risk Constraints:** Ensuring the portfolio risk does not exceed a predefined level.

These constraints are integrated into the optimization process, guiding the solver to find the optimal portfolio that meets the user-defined criteria.

