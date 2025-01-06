  # crypto-bot
-------------------------------------------------------------------------------------------------------      

|_ _|_ __ | |_ ___| | (_) __ _  ___ _ __ | |_  |_   _| __ __ _  __| (_)_ __   __ _  | __ )  ___ | |_
 | || '_ \| __/ _ \ | | |/ _` |/ _ \ '_ \| __|   | || '__/ _` |/ _` | | '_ \ / _` | |  _ \ / _ \| __|
 | || | | | ||  __/ | | | (_| |  __/ | | | |_    | || | | (_| | (_| | | | | | (_| | | |_) | (_) | |_ 
|___|_| |_|\__\___|_|_|_|\__, |\___|_| |_|\__|   |_||_|  \__,_|\__,_|_|_| |_|\__, | |____/ \___/ \__|
                         |___/                                               |___/                   
-------------------------------------------------------------------------------------------------------
❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️❇️

https://lookerstudio.google.com/u/0/reporting/816631cc-5030-401d-bb52-101c237396a1/page/UcDXE/edit    

Development of a trading bot algorithm

Problem Statement:

In the cryptocurrency market, there is a recurring challenge where some coins are not listed immediately after their Initial Public Offering (IPO). This delay creates uncertainty among investors and traders, as the impact of listing on coin prices remains unclear. This lack of timely and actionable information prevents the crypto community from making informed buy/sell decisions, leading to missed opportunities or poor investment choices.

The project is aimed at developing AND testing an intelligent trading bot for  cryptocurrencies listing on Binance  using state-of-the-art machine learning (ML) algorithms and sentiment analysis on python. The project provides the following major functionalities:

Defining derived features using custom (Python) functions including technical signals
Analyzing historic data and training machine learning models 
Analyzing the predicted scores and choosing best signal parameters once a coin is listed on Binance


Hypothesis

Hypothesis 1: Prices tend to rise immediately after listing.

Hypothesis 2: High volatility occurs right after the listing.

Hypothesis 3: Do prices decline in the long term?

Hypothesis 4: Is there an opportunity for arbitrage to develop risk-efficient and profitable trading strategies?

Sources:
https://www.binance.com/en/support/announcement/new-cryptocurrency-listing?c=48
https://www.kucoin.com/announcement/new-listings/page/93
🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄🀄
Project Workflow:

![workflow](https://github.com/user-attachments/assets/026a7e32-46f0-4f05-a17d-5b95871a6c1f)


Steps:
collection /analysis / exploration

Extract historical data for newly listed coins.

Perform exploratory data analysis (EDA) on price movements.

Identify significant trends and anomalies.

Implementation:

For the bot service to work, a number of ML models must be created and tested .. All scripts run in batch mode by loading some input data in Colab and storing some output files. The scripts are located in the scripts module. Binance data was extracted using API, then loaded in Python for configuration and analysis

These are the files:

python -m scripts.download_binance -c config.json
python -m scripts.binance_api
python -m scripts.clean
python -m scripts.labels -c config.json
python -m scripts.BQ
python -m scripts.binominaltest
python -m scripts.merge
python -m scripts.falling


Download the latest historic data: python -m scripts.download_binance -c config.json

It uses Binance API but you can use any other data source or download data manually using other scripts
Merge several historic datasets into one dataset: python -m scripts.merge -c config.json

This script solves two problems: 1) there could be other sources like depth data or futures 2) a data source may have gaps so we need to produce a regular time raster in the output file

Generate Charts

This script is intended for visulaizing coins, calculating API and analysis:
Script: python -m scripts.visuals


![model_comparison](https://github.com/user-attachments/assets/f1decd05-652e-4392-a5df-449ce31d154c)


![calcs_volatility](https://github.com/user-attachments/assets/1b70f7bb-8320-449a-854c-39733e8d23f5)


![big_5_chart](https://github.com/user-attachments/assets/a777c0ad-78fd-4197-8f8a-73c0438b04ff)


![big_5_bg](https://github.com/user-attachments/assets/8a8e7815-37e3-434d-ad5a-38bcbd17fba3)


![big_5_chart3](https://github.com/user-attachments/assets/136a24bd-081f-49de-b3b8-7fec7f07c259)


![big_5_chart4](https://github.com/user-attachments/assets/08571bd0-f190-4c11-ac97-2d9435d2100c)



