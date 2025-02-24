WITH
    mint_data AS (
        SELECT
            DATE_TRUNC('day', evt_block_time) AS date,
            contract_address AS pool_address,
            SUM(amount) AS liquidity_added,
            COUNT(*) AS mint_events
        FROM
            uniswap_v3_multichain.uniswapv3pool_evt_mint
        WHERE
            contract_address = 0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640 -- WETH/USDC资金池
            AND evt_block_time >= CURRENT_DATE - INTERVAL '360' day  -- 过去360天
        GROUP BY
            1,
            2
    ),
    burn_data AS (
        SELECT
            DATE_TRUNC('day', evt_block_time) AS date,
            contract_address AS pool_address,
            SUM(amount) AS liquidity_removed,
            COUNT(*) AS burn_events
        FROM
            uniswap_v3_multichain.uniswapv3pool_evt_burn
        WHERE
            contract_address = 0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640 -- WETH/USDC资金池
            AND evt_block_time >= CURRENT_DATE - INTERVAL '360' day  -- 过去360天
        GROUP BY
            1,
            2
    ),
    swap_data AS (
        SELECT
            DATE_TRUNC('day', evt_block_time) AS date,
            contract_address AS pool_address,
            SUM(ABS(amount0) + ABS(amount1)) AS total_trading_volume,
            COUNT(*) AS swap_events
        FROM
            uniswap_v3_multichain.uniswapv3pool_evt_swap
        WHERE
            contract_address = 0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640 -- WETH/USDC资金池
            AND evt_block_time >= CURRENT_DATE - INTERVAL '360' day -- 过去360天
        GROUP BY
            1,
            2
    )
SELECT
    COALESCE(m.date, b.date, s.date) AS date,
    COALESCE(m.pool_address, b.pool_address, s.pool_address) AS pool_address,
    COALESCE(m.liquidity_added, 0) AS total_liquidity_added,
    COALESCE(b.liquidity_removed, 0) AS total_liquidity_removed,
    COALESCE(s.total_trading_volume, 0) AS total_trading_volume,
    COALESCE(m.mint_events, 0) AS mint_events,
    COALESCE(b.burn_events, 0) AS burn_events,
    COALESCE(s.swap_events, 0) AS swap_events,
    CAST(COALESCE(m.liquidity_added, 0) AS INT256) - CAST(COALESCE(b.liquidity_removed, 0) AS INT256) AS net_liquidity_change
FROM
    mint_data m
    FULL OUTER JOIN burn_data b ON m.pool_address = b.pool_address
    AND m.date = b.date
    FULL OUTER JOIN swap_data s ON COALESCE(m.pool_address, b.pool_address) = s.pool_address
    AND COALESCE(m.date, b.date) = s.date
ORDER BY
    date DESC;