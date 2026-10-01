import pandas as pd


def repeat_customer_rate(
    orders: pd.DataFrame,
    customers: pd.DataFrame,
    delivered_only: bool = True,
) -> float:
    """Percentage of real customers (customer_unique_id) with more than one order."""
    df = orders.merge(
        customers[["customer_id", "customer_unique_id"]],
        on="customer_id",
    )

    if delivered_only:
        df = df[df["order_status"] == "delivered"]

    orders_per_customer = df.groupby("customer_unique_id")["order_id"].nunique()
    return (orders_per_customer > 1).mean() * 100