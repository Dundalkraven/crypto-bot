CREATE OR REPLACE TABLE `binance-bot-442813.Daily_data.coin_metrics` AS
SELECT
    c.Coin_Id,
    c.Coin_Name,
    c.Coin_Ticker,
    c.Primary_Category,
    
    -- Calculate First listing date as the minimum date
    MIN(m.Date) AS First_listing_date,
    
    -- Calculate First opening as the opening price on the first day
    MIN(m.Open) AS First_opening,
    
    -- Calculate Last closing as the maximum date and closing price
    MAX(m.Date) AS Last_closing,
    
    -- Calculate highest price
    MAX(m.High) AS highest,
    
    -- Calculate lowest price
    MIN(m.Low) AS lowest,

    -- Calculate Cumulative Return: Percentage change from the first opening to the last closing
    100 * (MAX(m.Close) - MIN(m.Open)) / MIN(m.Open) AS Cumulative_Return,

    -- Calculate Average Daily Return: Average of daily returns (percentage change from open to close)
    AVG(100 * (m.Close - m.Open) / m.Open) AS Average_Daily_Return,

    -- Calculate Average Daily Volatility: Average of daily volatility (difference between high and low)
    AVG(100 * (m.High - m.Low) / m.Open) AS Average_Daily_Volatility

FROM
    `binance-bot-442813.Daily_data.All_Metrics` m -- Metrics table containing price data
JOIN
    `binance-bot-442813.Daily_data.Coins_List_Binance_15` c -- Coin details table
ON
    m.Ticker_Name = c.Coin_Ticker -- Join based on Ticker_Name from All_Metrics and Coin_Ticker from Coins_List_Binance_15
WHERE
    m.Ticker_Name IN ('XAI', 'DYM', 'OMNI', 'PYTH', 'RON', 'JUP', 'ALT', 'AI', 'PIXEL', 'AXL', 'REZ', 'NOT', 'ZK', 'ZRO', 'BANANA') -- Example coin tickers
GROUP BY
    c.Coin_Id, c.Coin_Name, c.Coin_Ticker, c.Primary_Category;