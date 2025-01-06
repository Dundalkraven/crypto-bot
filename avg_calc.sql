WITH subquery AS (
  SELECT 
    *, 
    MAX(High) OVER (PARTITION BY Ticker_Name) AS Time_to_peak_price,
    
  FROM 
    `binance-bot-442813.fresh_and_clean.fresh_with_ticker`
)
SELECT
  *
FROM 
  subquery
WHERE 
  Time_to_peak_price = High; -- Filter rows where High equals Time_to_peak_price