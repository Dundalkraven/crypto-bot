CREATE OR REPLACE TABLE `binance-bot-442813.Daily_data.coin_kpis` AS
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
    MIN(m.Low) AS lowest

FROM
    `binance-bot-442813.Daily_data.All_Metrics` m -- Metrics table
JOIN
    `binance-bot-442813.Daily_data.Coins_List_Binance_15` c -- Coin information table
ON
    m.Ticker_Name = c.Coin_Ticker -- Join on the Ticker_Name and Coin_Ticker
GROUP BY
    c.Coin_Id, c.Coin_Name, c.Coin_Ticker, c.Primary_Category;