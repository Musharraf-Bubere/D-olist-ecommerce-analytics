import pandas as pd

from olist.config import RAW_DIR

# Friendly name -> actual file name
TABLE_FILES = {
    "customers": "olist_customers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}

# Columns that should be read as dates, per table
DATE_COLUMNS = {
    "orders": [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ],
    "order_items": ["shipping_limit_date"],
    "reviews": ["review_creation_date", "review_answer_timestamp"],
}


def load_table(name: str) -> pd.DataFrame:
    """Load one raw table by its friendly name."""
    if name not in TABLE_FILES:
        raise KeyError(f"Unknown table '{name}'. Choose from: {list(TABLE_FILES)}")

    path = RAW_DIR / TABLE_FILES[name]
    return pd.read_csv(path, parse_dates=DATE_COLUMNS.get(name, []))


def load_all() -> dict[str, pd.DataFrame]:
    """Load all 9 raw tables into a dictionary of DataFrames."""
    return {name: load_table(name) for name in TABLE_FILES}