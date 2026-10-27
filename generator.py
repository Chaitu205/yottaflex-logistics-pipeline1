import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# 1. Deterministic Rule
np.random.seed(20261022)
random.seed(20261022)

print("🚀 Starting Synthetic Logistics Volume Generation (50k Shipments)...")


NUM_SHIPMENTS = 50000
NUM_FACILITIES = 100
NUM_CARRIERS = 10
START_DATE = datetime(2026, 1, 1)


facilities = [f"FAC-{i:03d}" for i in range(1, NUM_FACILITIES + 1)]
carriers = [f"CRR-{i:02d}" for i in range(1, NUM_CARRIERS + 1)]
service_levels = ["STANDARD", "EXPRESS", "NEXT_DAY"]

shipments_list = []
legs_list = []
events_list = []
anomalies_list = []


for i in range(1, NUM_SHIPMENTS + 1):
    shipment_id = f"SHP-2026-{i:06d}"
    carrier = random.choice(carriers)
    service_level = random.choice(service_levels)
    
   
    ship_time = START_DATE + timedelta(days=random.randint(0, 180), hours=random.randint(0, 23))
    route_id = f"ROT-{random.randint(1000, 9999)}"
    
    fac_1 = random.choice(facilities)
    fac_2 = random.choice([f for f in facilities if f != fac_1])
    
   
    leg_id = f"LEG-{shipment_id}-01"
    legs_list.append({
        "ShipmentLegID": leg_id, "ShipmentID": shipment_id, 
        "OriginFacility": fac_1, "DestinationFacility": fac_2, "RouteID": route_id
    })
    
    # Event 1: Pickup
    evt1_id = f"EVT-{shipment_id}-000001"
    events_list.append({
        "TrackingEventID": evt1_id, "ShipmentID": shipment_id, "EventTime": ship_time,
        "IngestionTime": ship_time + timedelta(minutes=random.randint(5, 30)),
        "Status": "PICKED_UP", "Location": fac_1
    })
    
    # Event 2: Delivery 
    delivery_time = ship_time + timedelta(days=random.randint(1, 5))
    evt2_id = f"EVT-{shipment_id}-000002"
    status_label = "DELIVERED"
    
    
    if random.random() < 0.05:
        anomaly_choice = random.choice(["transit_leak", "wrong_order"])
        if anomaly_choice == "transit_leak":
            status_label = "IN_TRANSIT"  # నిజానికి డెలివరీ అయినా ఇంకా ఇన్-ట్రాన్సిట్ అని తప్పుగా చూపించడం
            anomalies_list.append({"ShipmentID": shipment_id, "AnomalyType": "Delivered shipment still marked in transit"})
        elif anomaly_choice == "wrong_order":
            ship_time, delivery_time = delivery_time, ship_time  # టైమ్‌స్టాంప్స్ తారుమారు చేయడం (ఇంపాజిబుల్ రూట్ ఆర్డర్)
            anomalies_list.append({"ShipmentID": shipment_id, "AnomalyType": "Impossible route date order"})

    events_list.append({
        "TrackingEventID": evt2_id, "ShipmentID": shipment_id, "EventTime": delivery_time,
        "IngestionTime": delivery_time + timedelta(minutes=random.randint(5, 30)),
        "Status": status_label, "Location": fac_2
    })
    
    shipments_list.append({
        "ShipmentID": shipment_id, "CarrierID": carrier, "ServiceLevel": service_level,
        "OrderDate": ship_time - timedelta(days=1), "Status": status_label
    })

# 6. (Export to CSV - Step 9 Rule)
pd.DataFrame(shipments_list).to_csv("shipments.csv", index=False)
pd.DataFrame(legs_list).to_csv("shipment_legs.csv", index=False)
pd.DataFrame(events_list).to_csv("tracking_events.csv", index=False)
pd.DataFrame(anomalies_list).to_csv("ground_truth.csv", index=False)

print("✅ Data and Edge Cases Generated Successfully!")
print(f"Created shipments.csv, tracking_events.csv, and ground_truth.csv files.")
