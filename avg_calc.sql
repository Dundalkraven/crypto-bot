ITH daily_returns AS (
    SELECT 
        date,
        ticker,
        (close - open) / open AS daily_return
    FROM 
        binance-bot-442813.BIG_FIVE.BNB_KPI
),
rolling_stddev AS (
    SELECT
        ticker,
        date,
        daily_return,
        STDDEV_SAMP(daily_return) OVER (
            PARTITION BY ticker
            ORDER BY date
            ROWS BETWEEN 29 PRECEDING AND CURRENT ROW
        ) AS rolling_stddev_30
    FROM 
        daily_returns
)
SELECT *
FROM rolling_stddev
WHERE date >= '2024-01-01'
ORDER BY ticker, date;
