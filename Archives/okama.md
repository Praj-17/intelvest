## annual_return_ts

| date | Value      |
|------|------------|
| 2015 | -0.012715  |
| 2016 | 0.110796   |
| 2017 | 0.238511   |
| 2018 | -0.036226  |
| 2019 | 0.329415   |
| 2020 | 0.251170   |
| 2021 | 0.284233   |
| 2022 | -0.219780  |
| 2023 | 0.327853   |
| 2024 | 0.186512   |

*Freq: Y-DEC, Name: portfolio_3420.PF, dtype: float64*

---

## asset_obj_dict

```python
{
    'VOO.US': symbol                         VOO.US
    name             Vanguard S&P 500 ETF
    country                           USA
    exchange                    NYSE ARCA
    currency                          USD
    type                              ETF
    isin                     US9229083632
    first date                    2010-10
    last date                     2024-10
    period length                   14.00
    dtype: object, 
    'SPY.US': symbol                           SPY.US
    name             SPDR S&P 500 ETF Trust
    country                             USA
    exchange                      NYSE ARCA
    currency                            USD
    type                                ETF
    isin                       US78462F1030
    first date                      1993-02
    last date                       2024-10
    period length                     31.70
    dtype: object, 
    'QQQ.US': symbol                      QQQ.US
    name             Invesco QQQ Trust
    country                        USA
    exchange                    NASDAQ
    currency                       USD
    type                           ETF
    isin                  US46090E1038
    first date                 1999-04
    last date                  2024-10
    period length                25.50
    dtype: object
}
```

---

## assets_close_monthly

| date    | VOO.US | SPY.US | QQQ.US |
|---------|--------|--------|--------|
| 2015-11 | 191.37 | 208.69 | 114.02 |
| 2015-12 | 186.93 | 203.87 | 111.86 |
| 2016-01 | 177.75 | 193.72 | 104.13 |
| 2016-02 | 177.38 | 193.56 | 102.50 |
| 2016-03 | 188.56 | 205.52 | 109.20 |
| ...     | ...    | ...    | ...    |
| 2024-04 | 461.43 | 501.98 | 424.59 |
| 2024-05 | 484.62 | 527.37 | 450.71 |
| 2024-06 | 500.13 | 544.22 | 479.11 |
| 2024-07 | 505.93 | 550.81 | 471.07 |
| 2024-08 | 518.04 | 563.68 | 476.27 |

*[106 rows x 3 columns]*

---

## assets_dividend_yield

| date    | VOO.US  | SPY.US  | QQQ.US |
|---------|---------|---------|--------|
| 2015-11 | 0.000000 | 0.000000 | 0.000000 |
| 2015-12 | 0.005842 | 0.005943 | 0.003059 |
| 2016-01 | 0.006143 | 0.006254 | 0.003286 |
| 2016-02 | 0.006156 | 0.006259 | 0.003339 |
| 2016-03 | 0.011126 | 0.011002 | 0.006042 |
| ...     | ...     | ...     | ...    |
| 2024-04 | 0.013897 | 0.013392 | 0.006209 |
| 2024-05 | 0.013232 | 0.012747 | 0.005849 |
| 2024-06 | 0.013237 | 0.012574 | 0.006040 |
| 2024-07 | 0.013085 | 0.012424 | 0.006143 |
| 2024-08 | 0.012779 | 0.012140 | 0.006076 |

*[106 rows x 3 columns]*

---

## assets_first_dates

| Asset     | First Date           |
|-----------|----------------------|
| USD       | 1913-02-01 00:00:00  |
| SPY.US    | 1993-02-01 00:00:00  |
| QQQ.US    | 1999-04-01 00:00:00  |
| VOO.US    | 2010-10-01 00:00:00  |
| USD.INFL  | 1913-02-01 00:00:00  |

---

## assets_last_dates

| Asset     | Last Date             |
|-----------|-----------------------|
| VOO.US    | 2024-10-01 00:00:00   |
| SPY.US    | 2024-10-01 00:00:00   |
| QQQ.US    | 2024-10-01 00:00:00   |
| USD       | 2099-12-01 00:00:00   |
| USD.INFL  | 2024-08-01 00:00:00   |

---

## assets_ror

| date    | VOO.US | SPY.US | QQQ.US |
|---------|--------|--------|--------|
| 2015-11 | 0.0043 | 0.0037 | 0.0061 |
| 2015-12 | -0.0174| -0.0173| -0.0159|
| 2016-01 | -0.0491| 0.0112 | -0.0171|
| 2016-02 | -0.0136| 0.0530 | 0.0291 |
| 2016-03 | 0.0085 | 0.0326 | 0.0323 |
| ...     | ...    | ...    | ...    |
| 2024-04 | -0.0401| -0.0403| -0.0437|
| 2024-05 | 0.0503 | 0.0506 | 0.0615 |
| 2024-06 | 0.0357 | 0.0353 | 0.0647 |
| 2024-07 | 0.0116 | 0.0121 | -0.0168|
| 2024-08 | 0.0239 | 0.0213 | 0.0241 |

*[106 rows x 3 columns]*

---

## assets_weights

```python
{'VOO.US': 0.4, 'SPY.US': 0.4, 'QQQ.US': 0.2}
```

---

## cashflow

0

---

## close_monthly

| date    | Value        |
|---------|--------------|
| 2015-11 | 1000.000000  |
| 2015-12 | 1004.420000  |
| 2016-01 | 987.285070   |
| 2016-02 | 934.572787   |
| 2016-03 | 930.590548   |
| ...     | ...          |
| 2024-04 | 3184.075959  |
| 2024-05 | 3053.144365  |
| 2024-06 | 3216.027977  |
| 2024-07 | 3355.032807  |
| 2024-08 | 3368.844839  |

*Freq: M, Name: portfolio_3420.PF, Length: 106, dtype: float64*

---

## currencies

| Asset      | Currency |
|------------|----------|
| VOO.US     | USD      |
| SPY.US     | USD      |
| QQQ.US     | USD      |
| asset list | USD      |

---

## currency

USD

---

## dcf

```python
<okama.portfolio.PortfolioDCF object at 0x0000024DF6C91460>
```

---

## describe

```python
<bound method Portfolio.describe of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## discount_rate

0.03226367360540672

---

## diversification_ratio

1.010170487025168

---

## dividend_yield

| date    | Value    |
|---------|----------|
| 2015-11 | 0.000000 |
| 2015-12 | 0.005324 |
| 2016-01 | 0.005624 |
| 2016-02 | 0.005648 |
| 2016-03 | 0.010085 |
| ...     | ...      |
| 2024-04 | 0.011694 |
| 2024-05 | 0.011102 |
| 2024-06 | 0.011053 |
| 2024-07 | 0.011008 |
| 2024-08 | 0.010789 |

*Freq: M, Name: portfolio_3420.PF, Length: 106, dtype: float64*

---

## dividend_yield_annual

| Year | VOO.US | SPY.US | QQQ.US |
|------|--------|--------|--------|
| 2015 | 0.005842 | 0.005943 | 0.003059 |
| 2016 | 0.020155 | 0.020306 | 0.010572 |
| 2017 | 0.017807 | 0.017995 | 0.008350 |
| 2018 | 0.020611 | 0.020408 | 0.009105 |
| 2019 | 0.018833 | 0.017456 | 0.007435 |
| 2020 | 0.015429 | 0.015221 | 0.005532 |
| 2021 | 0.012453 | 0.012039 | 0.004263 |
| 2022 | 0.016926 | 0.016528 | 0.008014 |
| 2023 | 0.014554 | 0.013957 | 0.006189 |
| 2024 | 0.012779 | 0.012140 | 0.006076 |

---

## dividends

| date    | Value    |
|---------|----------|
| 2015-11 | 0.000000 |
| 2015-12 | 5.347449 |
| 2016-01 | 0.000000 |
| 2016-02 | 0.000000 |
| 2016-03 | 4.438988 |
| ...     | ...      |
| 2024-04 | 0.000000 |
| 2024-05 | 0.000000 |
| 2024-06 | 9.361996 |
| 2024-07 | 0.000000 |
| 2024-08 | 0.000000 |

*Freq: M, Name: portfolio_3420.PF, Length: 106, dtype: float64*

---

## dividends_annual

| Year | VOO.US | SPY.US | QQQ.US |
|------|--------|--------|--------|
| 2015 | 1.0920 | 1.2115 | 0.3422 |
| 2016 | 4.1380 | 4.5390 | 1.2526 |
| 2017 | 4.3679 | 4.8021 | 1.3006 |
| 2018 | 4.7367 | 5.1004 | 1.4046 |
| 2019 | 5.5709 | 5.6183 | 1.5807 |
| 2020 | 5.3027 | 5.6910 | 1.7355 |
| 2021 | 5.4367 | 5.7182 | 1.6960 |
| 2022 | 5.9467 | 6.3207 | 2.1340 |
| 2023 | 6.3572 | 6.6339 | 2.5346 |
| 2024 | 3.3264 | 3.3539 | 1.3350 |

---

## drawdowns

| date    | Value     |
|---------|-----------|
| 2015-11 | 0.000000  |
| 2015-12 | -0.017060 |
| 2016-01 | -0.069540 |
| 2016-02 | -0.073505 |
| 2016-03 | -0.010413 |
| ...     | ...       |
| 2024-04 | -0.041121 |
| 2024-05 | 0.000000  |
| 2024-06 | 0.000000  |
| 2024-07 | 0.000000  |
| 2024-08 | 0.000000  |

*Freq: M, Name: portfolio_3420.PF, Length: 106, dtype: float64*

---

## eldest_asset

USD

---

## first_date

2015-11-01 00:00:00

---

## get_cagr

```python
<bound method Portfolio.get_cagr of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## get_cumulative_return

```python
<bound method Portfolio.get_cumulative_return of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## get_cvar_historic

```python
<bound method Portfolio.get_cvar_historic of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## get_rolling_cagr

```python
<bound method Portfolio.get_rolling_cagr of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## get_rolling_cumulative_return

```python
<bound method Portfolio.get_rolling_cumulative_return of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## get_sharpe_ratio

```python
<bound method Portfolio.get_sharpe_ratio of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## get_sortino_ratio

```python
<bound method Portfolio.get_sortino_ratio of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## get_var_historic

```python
<bound method Portfolio.get_var_historic of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## inflation

USD.INFL

---

## inflation_first_date

2015-11-01 00:00:00

---

## inflation_last_date

2024-08-01 00:00:00

---

## inflation_ts

| date    | Value    |
|---------|----------|
| 2015-11 | -0.0021  |
| 2015-12 | -0.0034  |
| 2016-01 | 0.0017   |
| 2016-02 | 0.0008   |
| 2016-03 | 0.0043   |
| ...     | ...      |
| 2024-04 | 0.0039   |
| 2024-05 | 0.0017   |
| 2024-06 | 0.0003   |
| 2024-07 | 0.0012   |
| 2024-08 | 0.0008   |

*Freq: M, Name: USD.INFL, Length: 106, dtype: float64*

---

## initial_amount

2000.0

---

## jarque_bera

| statistic         | p-value             |
|-------------------|---------------------|
| 3.781510810134506 | 0.15095773151917324 |

---

## kstest

```python
<bound method Portfolio.kstest of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## kurtosis

| date    | Value    |
|---------|----------|
| 2016-11 | 1.066831 |
| 2016-12 | 1.193685 |
| 2017-01 | 1.212599 |
| 2017-02 | 0.855925 |
| 2017-03 | 1.066627 |
| ...     | ...      |
| 2024-04 | 0.336662 |
| 2024-05 | 0.338377 |
| 2024-06 | 0.355339 |
| 2024-07 | 0.382239 |
| 2024-08 | 0.415570 |

*Freq: M, Name: portfolio_3420.PF, Length: 94, dtype: float64*

---

## kurtosis_rolling

```python
<bound method Portfolio.kurtosis_rolling of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## last_date

2024-08-01 00:00:00

---

## mean_return_annual

0.16368062593524102

---

## mean_return_monthly

0.01271245283018868

---

## monte_carlo_returns_ts

```python
<bound method Portfolio.monte_carlo_returns_ts of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## monte_carlo_wealth

```python
<bound method Portfolio.monte_carlo_wealth of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## name

portfolio_3420.PF

---

## names

| Ticker | Asset Name                     |
|--------|--------------------------------|
| VOO.US | Vanguard S&P 500 ETF            |
| SPY.US | SPDR S&P 500 ETF Trust          |
| QQQ.US | Invesco QQQ Trust               |

---

## newest_asset

VOO.US

---

## number_of_securities

| date    | VOO.US   | SPY.US  | QQQ.US |
|---------|----------|---------|--------|
| 2015-11 | 2.089942 | 1.915345| 1.757012|
| 2015-12 | 2.148295 | 1.968812| 1.800978|
| 2016-01 | 2.230770 | 2.044348| 1.870109|
| 2016-02 | 2.120664 | 1.943530| 1.777753|
| 2016-03 | 1.987547 | 1.821268| 1.662195|
| ...     | ...      | ...     | ...    |
| 2024-04 | 2.552435 | 2.332215| 1.967971|
| 2024-05 | 2.323614 | 2.123090| 1.791442|
| 2024-06 | 2.354571 | 2.150657| 1.811705|
| 2024-07 | 2.446278 | 2.234395| 1.882226|
| 2024-08 | 2.407375 | 2.199013| 1.852287|

*[106 rows x 3 columns]*

---

## percentile_distribution_cagr

```python
<bound method Portfolio.percentile_distribution_cagr of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## percentile_history_cagr

```python
<bound method Portfolio.percentile_history_cagr of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## percentile_inverse_cagr

```python
<bound method Portfolio.percentile_inverse_cagr of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## percentile_wealth

```python
<bound method Portfolio.percentile_wealth of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## percentile_wealth_history

```python
<bound method Portfolio.percentile_wealth_history of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## period_length

8.8

---

## pl

PeriodLength(years=8, months=10)

---

## plot_assets

```python
<bound method ListMaker.plot_assets of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## plot_forecast

```python
<bound method Portfolio.plot_forecast of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## plot_forecast_monte_carlo

```python
<bound method Portfolio.plot_forecast_monte_carlo of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## plot_hist_fit

```python
<bound method Portfolio.plot_hist_fit of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## plot_percentiles_fit

```python
<bound method Portfolio.plot_percentiles_fit of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## real_mean_return

0.12819374334634204

---

## rebalancing_period

none

---

## recovery_period

| date    | Value |
|---------|-------|
| 2016-05 | 5     |
| 2016-07 | 1     |
| 2016-11 | 1     |
| 2018-07 | 5     |
| 2019-04 | 6     |
| 2019-07 | 2     |
| 2019-10 | 2     |
| 2020-06 | 4     |
| 2020-11 | 2     |
| 2021-02 | 1     |
| 2021-10 | 1     |
| 2021-12 | 1     |
| 2023-12 | 23    |
| 2024-05 | 1     |

*Freq: M, Name: portfolio_3420.PF, dtype: int32*

---

## risk_annual

| date    | Value    |
|---------|----------|
| 2015-12 | 0.049101 |
| 2016-01 | 0.079441 |
| 2016-02 | 0.072693 |
| 2016-03 | 0.153209 |
| 2016-04 | 0.136242 |
| ...     | ...      |
| 2024-04 | 0.186932 |
| 2024-05 | 0.187525 |
| 2024-06 | 0.187595 |
| 2024-07 | 0.186544 |
| 2024-08 | 0.185811 |

*Freq: M, Name: portfolio_3420.PF, Length: 105, dtype: float64*

---

## risk_monthly

| date    | Value    |
|---------|----------|
| 2015-12 | 0.015188 |
| 2016-01 | 0.029222 |
| 2016-02 | 0.025457 |
| 2016-03 | 0.044203 |
| 2016-04 | 0.039553 |
| ...     | ...      |
| 2024-04 | 0.046996 |
| 2024-05 | 0.046941 |
| 2024-06 | 0.046810 |
| 2024-07 | 0.046592 |
| 2024-08 | 0.046375 |

*Freq: M, Name: portfolio_3420.PF, Length: 105, dtype: float64*

---

## ror

| date    | Value    |
|---------|----------|
| 2015-11 | 0.004420 |
| 2015-12 | -0.017060|
| 2016-01 | -0.053391|
| 2016-02 | -0.004261|
| 2016-03 | 0.068097 |
| ...     | ...      |
| 2024-04 | -0.041121|
| 2024-05 | 0.053349 |
| 2024-06 | 0.043223 |
| 2024-07 | 0.004117 |
| 2024-08 | 0.020307 |

*Freq: M, Name: portfolio_3420.PF, Length: 106, dtype: float64*

---

## semideviation_annual

0.13239371733631028

---

## semideviation_monthly

0.03821877417156698

---

## skewness

| date    | Value    |
|---------|----------|
| 2016-11 | 0.251125 |
| 2016-12 | 0.152288 |
| 2017-01 | 0.028754 |
| 2017-02 | -0.107934|
| 2017-03 | -0.074192|
| ...     | ...      |
| 2024-04 | -0.400958|
| 2024-05 | -0.417655|
| 2024-06 | -0.433519|
| 2024-07 | -0.429959|
| 2024-08 | -0.436459|

*Freq: M, Name: portfolio_3420.PF, Length: 94, dtype: float64*

---

## skewness_rolling

```python
<bound method Portfolio.skewness_rolling of symbol                       portfolio_3420.PF
assets                [VOO.US, SPY.US, QQQ.US]
weights                        [0.4, 0.4, 0.2]
rebalancing_period                        none
currency                                   USD
inflation                             USD.INFL
first_date                             2015-11
last_date                              2024-08
period_length               8 years, 10 months
dtype: object>
```

---

## symbol

portfolio_3420.PF

---

## symbols

- VOO.US
- SPY.US
- QQQ.US

---

## table

|   | asset name                | ticker | weights |
|---|---------------------------|--------|---------|
| 0 | Vanguard S&P 500 ETF      | VOO.US | 0.4     |
| 1 | SPDR S&P 500 ETF Trust    | SPY.US | 0.4     |
| 2 | Invesco QQQ Trust          | QQQ.US | 0.2     |

---

## tickers

- VOO
- SPY
- QQQ

---

## wealth_index

| date    | portfolio_3420.PF | USD.INFL   |
|---------|-------------------|------------|
| 2015-11 | 1000.000000       | 1000.000000|
| 2015-12 | 1004.420000       | 997.900000 |
| 2016-01 | 987.285070        | 994.507140 |
| 2016-02 | 934.572787        | 996.197802 |
| 2016-03 | 930.590548        | 996.994760 |
| ...     | ...               | ...        |
| 2024-04 | 3184.075959       | 1313.381286|
| 2024-05 | 3053.144365       | 1318.503473|
| 2024-06 | 3216.027977       | 1320.744929|
| 2024-07 | 3355.032807       | 1321.141153|
| 2024-08 | 3368.844839       | 1322.726522|

*[106 rows x 2 columns]*

---

## wealth_index_with_assets

| date    | portfolio_3420.PF | VOO.US    | SPY.US    | QQQ.US     | USD.INFL   |
|---------|-------------------|-----------|-----------|------------|------------|
| 2015-11 | 1000.000000       | 1000.000000 | 1000.000000 | 1000.000000 | 1000.000000|
| 2015-12 | 1004.420000       | 1004.300000 | 1003.700000 | 1006.100000 | 997.900000 |
| 2016-01 | 987.285070        | 986.825180 | 986.335990 | 990.103010 | 994.507140 |
| 2016-02 | 934.572787        | 938.372064 | 937.216458 | 921.686892 | 996.197802 |
| 2016-03 | 930.590548        | 936.401482 | 936.466685 | 907.216408 | 996.994760 |
| ...     | ...               | ...       | ...       | ...        | ...        |
| 2024-04 | 3184.075959       | 2941.293581 | 2924.310466 | 4189.171702 | 1313.381286|
| 2024-05 | 3053.144365       | 2823.347709 | 2806.460754 | 4006.104899 | 1318.503473|
| 2024-06 | 3216.027977       | 2965.362099 | 2948.467668 | 4252.480350 | 1320.744929|
| 2024-07 | 3355.032807       | 3071.225526 | 3052.548577 | 4527.615829 | 1321.141153|
| 2024-08 | 3368.844839       | 3106.851742 | 3089.484415 | 4451.551883 | 1322.726522|

*[106 rows x 5 columns]*

---

## weights

- 0.4
- 0.4
- 0.2

---

## weights_ts

| date    | VOO.US  | SPY.US  | QQQ.US |
|---------|---------|---------|--------|
| 2015-11 | 0.399952| 0.399713| 0.200335|
| 2015-12 | 0.399814| 0.399615| 0.200571|
| 2016-01 | 0.401626| 0.401131| 0.197242|
| 2016-02 | 0.402498| 0.402526| 0.194976|
| 2016-03 | 0.402725| 0.402225| 0.195050|
| ...     | ...     | ...     | ...    |
| 2024-04 | 0.369894| 0.367681| 0.262425|
| 2024-05 | 0.368823| 0.366722| 0.264455|
| 2024-06 | 0.366163| 0.363937| 0.269900|
| 2024-07 | 0.368892| 0.366830| 0.264278|
| 2024-08 | 0.370191| 0.367942| 0.261867|

*[106 rows x 3 columns]*

---