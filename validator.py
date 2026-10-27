import pandas as pd

print("🔍 Running Step 8 Validation Engine...")

try:
    df_shipments = pd.read_csv("shipments.csv")
    print("✅ Successfully loaded data files for cross-check analysis.")
except FileNotFoundError:
    print("❌ Error: Run generator.py first to create datasets!")
    exit()

# Primary Key Uniqueness Test
if df_shipments["ShipmentID"].is_unique:
    print("✅ Primary Key Validation Passed: All Shipment IDs are completely unique.")
else:
    print("❌ Validation Failure: Duplicate master entities detected!")

print("🏁 Validation Pipeline Execution Complete.")
