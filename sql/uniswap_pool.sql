WITH mint_data AS (
    SELECT 
        DATE_TRUNC('day', evt_block_time) AS date,
        contract_address AS pool_address,
        SUM(amount) AS liquidity_added
    FROM uniswap_v3_multichain.uniswapv3pool_evt_mint
    GROUP BY 1, 2
),
burn_data AS (
    SELECT 
        DATE_TRUNC('day', evt_block_time) AS date,
        contract_address AS pool_address,
        SUM(amount) AS liquidity_removed
    FROM uniswap_v3_multichain.uniswapv3pool_evt_burn
    GROUP BY 1, 2
),
swap_data AS (
    SELECT 
        DATE_TRUNC('day', evt_block_time) AS date,
        contract_address AS pool_address,
        SUM(ABS(amount0) + ABS(amount1)) AS total_trading_volume 
    FROM uniswap_v3_multichain.uniswapv3pool_evt_swap
    GROUP BY 1, 2
)
SELECT 
    m.date,
    m.pool_address,
    COALESCE(m.liquidity_added, 0) AS total_liquidity_added,
    COALESCE(b.liquidity_removed, 0) AS total_liquidity_removed,
    COALESCE(s.total_trading_volume, 0) AS total_trading_volume
FROM mint_data m
LEFT JOIN burn_data b ON m.pool_address = b.pool_address AND m.date = b.date
LEFT JOIN swap_data s ON m.pool_address = s.pool_address AND m.date = s.date
ORDER BY date DESC
LIMIT 30;
