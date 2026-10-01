## Step 2: Data profiling

- customer_id is per order; customer_unique_id identifies the real customer (96,096 people).
- geolocation has 261,831 duplicate rows and many points per zip, so reduce to one row per zip before joining.
- payments can have multiple rows per order, so aggregate (sum) before joining.
- reviews: only ~41% have comment text; some review_ids and order_ids repeat.
- orders: missing delivery dates are mostly undelivered orders (verified with order_status).

## Step 2 (continued): First business finding

- customer_id is per order; customer_unique_id is the real customer.
- Always check row count after a join (orders 99,441 -> merged 99,441, so the join is safe).
- 97% of customers are one-time buyers. Repeat rate is 3.00% (delivered orders only).
- Business definition matters: cancelled/unavailable orders are not real purchases.
- Moved proven notebook logic into olist/analysis/retention.py.