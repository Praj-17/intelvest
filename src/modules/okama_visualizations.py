import pandas as pd
import plotly.graph_objects as go
import okama as ok
import os
from dotenv import load_dotenv
load_dotenv()
import plotly.express as px


import json

with open(os.getenv("okama_visualizations", "r")) as f:
    visualization_attributes = json.load(f)
def plot_asset_allocation(portfolio):
    weights = portfolio.weights
    symbols = portfolio.symbols
    fig = px.pie(values=weights, names=symbols, title='Asset Allocation')
    return fig.to_html(full_html=False, include_plotlyjs=False)



def plot_wealth_index(portfolio):
    """
    This function takes a wealth_index Series, converts its index to a DatetimeIndex if it's a PeriodIndex,
    and plots the wealth index over time using Plotly.

    Parameters:
    wealth_index (pd.Series): A Pandas Series containing the wealth index with a date-based index.

    Returns:
    str: The HTML string of the plot, without Plotly.js included.
    """
    wealth_index  = portfolio.wealth_index
    # Convert wealth_index.index to DatetimeIndex if it's a PeriodIndex
    if isinstance(wealth_index.index, pd.PeriodIndex):
        wealth_index.index = wealth_index.index.to_timestamp()

    # Create the plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=wealth_index.index, y=wealth_index, mode='lines', name='Wealth Index'))
    fig.update_layout(title='Wealth Index Over Time', xaxis_title='Date', yaxis_title='Wealth Index')

    # Return the HTML string of the plot without Plotly.js included
    return fig.to_html(full_html=False, include_plotlyjs=False)


def plot_drawdowns(portfolio):
  drawdowns = portfolio.drawdowns
  if isinstance(drawdowns.index, pd.PeriodIndex):
      drawdowns.index = drawdowns.index.to_timestamp()

  # Plotting Drawdowns (Line graph)
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=drawdowns.index, y=drawdowns, mode='lines', name='Drawdowns'))
  fig.update_layout(title='Portfolio Drawdowns', xaxis_title='Date', yaxis_title='Drawdown (%)')
  return fig.to_html(full_html=False, include_plotlyjs=False)



def plot_distribution_test(portfolio):
    # Accessing 'distribution_test' data - modify to match actual data structure
    try:
        portfolio_data = portfolio['distribution_test']
        # Convert dictionary to pandas Series for plotting
        import pandas as pd
        portfolio_data = pd.Series(portfolio_data)
        portfolio_data.index = pd.to_datetime(portfolio_data.index)
    except (KeyError, TypeError):
        raise AttributeError("The 'portfolio' object does not have 'distribution_test' data "
                             "in the expected format. Please ensure it's a dictionary "
                             "with dates as keys and values as distribution values.") from None

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=portfolio_data.index, y=portfolio_data.values, mode='lines', name='Distribution Test'))
    fig.update_layout(title='Distribution Test', xaxis_title='Date', yaxis_title='Distribution Value')
    return fig.to_html(full_html=False, include_plotlyjs=False)


def plot_weight_time_series(portfolio):  # Add wealth_index as an argument
    # weight_ts = portfolio.weights  # Remove this line, as portfolio doesn't have a 'weights' attribute
    # Assuming rf3.wealth_index is a pandas Series or DataFrame
    wealth_index  = portfolio.wealth_index
    fig = go.Figure()
    # Use wealth_index for both x and y, assuming it has a DatetimeIndex
    fig.add_trace(go.Scatter(x=wealth_index.index, y=wealth_index.values, mode='lines', name='Wealth Index'))
    fig.update_layout(title='Wealth Index Over Time', xaxis_title='Date', yaxis_title='Wealth Index')
    return fig.to_html(full_html=False, include_plotlyjs=False)

# Convert risk_annual.index to DatetimeIndex if it's a PeriodIndex
def plot_annual_risk(portfolio):  # Change argument to risk_annual
  # risk_annual = portfolio.risk_annual  # Remove this line, as risk_annual is already passed as argument
  risk_annual = portfolio.risk_annual
  if isinstance(risk_annual.index, pd.PeriodIndex):
      risk_annual.index = risk_annual.index.to_timestamp()

  fig = go.Figure()
  fig.add_trace(go.Scatter(x=risk_annual.index, y=risk_annual, mode='lines', name='Annual Risk'))
  fig.update_layout(title='Annual Risk Over Time', xaxis_title='Date', yaxis_title='Annual Risk')
  return fig.to_html(full_html=False, include_plotlyjs=False)

# Assuming annual_return_ts is a pandas Series
# Convert PeriodIndex to strings for serialization
def plot_annual_return(portfolio): # Change the function argument to annual_return_ts
  # annual_return_ts = portfolio.annual_return_ts # Remove this line, as annual_return_ts is now the function argument
  annual_return_ts = portfolio.annual_return_ts
  if isinstance(annual_return_ts.index, pd.PeriodIndex):
      annual_return_ts.index = annual_return_ts.index.astype(str)
  fig = go.Figure(data=[go.Bar(x=annual_return_ts.index.astype(str), y=annual_return_ts)])
  fig.update_layout(title='Annual Returns', xaxis_title='Year', yaxis_title='Annual Return')
  return fig.to_html(full_html=False, include_plotlyjs=False)

def plot_dividend_yield(portfolio):  # Change argument to dividend_yield_data
  # dividend_yield = portfolio.dividend_yield  # Remove this line, it's incorrect
  dividend_yield_data = portfolio.dividend_yield
  if isinstance(dividend_yield_data.index, pd.PeriodIndex):
      dividend_yield_data.index = dividend_yield_data.index.astype(str)

  fig = go.Figure(data=[go.Scatter(x=dividend_yield_data.index, y=dividend_yield_data, mode='lines')]) # Changed to Scatter plot
  fig.update_layout(title='Dividend Yield Over Time', xaxis_title='Date', yaxis_title='Dividend Yield')
  return fig.to_html(full_html=False, include_plotlyjs=False)

def map_plots_with_attributes(attribute, portfolio):
    out = None
    Reason = ""
    if attribute in visualization_attributes:
        if attribute == "weights" or attribute == "table":
            out = plot_asset_allocation(portfolio)
        elif attribute == "wealth_index" or attribute == "wealth_index_with_assets":
            out = plot_wealth_index(portfolio)
        elif attribute == "drawdowns":
            out = plot_drawdowns(portfolio)
        elif attribute == "weights_ts":
            out = plot_weight_time_series(portfolio)
        elif attribute == "risk_annual":
            out = plot_annual_risk(portfolio)
        elif attribute == "annual_return_ts":
            out = plot_annual_return(portfolio)
        elif attribute == "dividend_yield":
            out = plot_dividend_yield(portfolio)
    else:
        Reason = 'Incorrrect visualization name or visualization not implemented'
    return out , Reason

if __name__ == "__main__":
    # Example portfolio
    print("Creating object")
    portfolio = ok.Portfolio(assets=['SPY.US', 'AGG.US'], weights=[0.7, 0.3])
    print("Created object")


    # # Getting portfolio data
    # wealth_index = portfolio.wealth_index
    # rolling_cagr = portfolio.get_rolling_cagr(window=252)
    # drawdowns = portfolio.drawdowns
    # annual_return_ts = portfolio.annual_return_ts
    # risk_annual = portfolio.risk_annual
    # dividend_yield = portfolio.dividend_yield
    # weight_ts = portfolio.weights
    aatr = "dividend_yield"
    html = map_plots_with_attributes(aatr, portfolio)

    with open(f"{aatr}.html", "w+", encoding = "utf-8") as f:
        f.write(html)

