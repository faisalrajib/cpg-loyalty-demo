import pandas as pd
import numpy as np
from pathlib import Path
Path("data/raw").mkdir(parents=True, exist_ok=True)
np.random.seed(42)
n = 500
df = pd.DataFrame({
"customer_id": np.random.randint(1, 120, n),
"transaction_id": range(10000, 10000 + n),
"product_id": np.random.randint(100, 300, n),
"amount": np.round(np.random.uniform(2.5, 45.0, n), 2),
"date": pd.date_range("2025-01-01", periods=n).date
})
df.to_csv("data/raw/transactions_2025.csv", index=False)
print(f"Generated {len(df)} synthetic transactions")
