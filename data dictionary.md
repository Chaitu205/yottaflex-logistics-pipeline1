# 📊 YottaFlex AI Project - Data Dictionary

This document defines the schema, types, allowed values, and validation rules for all 11 core logistics entities required by the recruitment drive project.

---

## 1. Shipment Table
* **ShipmentID:** String (Required) | Format: `SHP-2026-XXXXXX` (e.g., SHP-2026-000001) | Primary Key. Must be strictly unique.
* **CarrierID:** String (Required) | Format: `CRR-XX` (e.g., CRR-01) | Foreign Key referencing Carrier table.
* **ServiceLevel:** String (Required) | Allowed Values: `STANDARD`, `EXPRESS`, `NEXT_DAY` | Enum validation constraint.
* **OrderDate:** Date (Required) | Format: YYYY-MM-DD | Must be at least 1 day before the pickup event time.
* **Status:** String (Required) | Allowed Values: `PICKED_UP`, `IN_TRANSIT`, `DELIVERED` | Current state lifecycle transition.

## 2. ShipmentLeg Table
* **ShipmentLegID:** String (Required) | Format: `LEG-<shipment-id>-XX` (e.g., LEG-SHP-2026-000001-01) | Primary Key.
* **ShipmentID:** String (Required) | Foreign Key referencing Shipment.
* **OriginFacility:** String (Required) | Format: `FAC-XXX` (e.g., FAC-001 to FAC-100) | Foreign Key.
* **DestinationFacility:** String (Required) | Format: `FAC-XXX` | Must not be equal to OriginFacility.
* **RouteID:** String (Required) | Format: `ROT-XXXX` | Identifies the physical path.

## 3. TrackingEvent Table 
* **TrackingEventID:** String (Required) | Format: `EVT-<shipment-id>-XXXXXX` | Primary Key.
* **ShipmentID:** String (Required) | Foreign Key referencing Shipment.
* **EventTime:** Timestamp (Required) | Format: YYYY-MM-DD HH:MM:SS | Operational timestamp.
* **IngestionTime:** Timestamp (Required) | Database record time. Must be greater than or equal to EventTime.
* **Status:** String (Required) | `PICKED_UP`, `IN_TRANSIT`, `DELIVERED` | Current state checkpoint.
* **Location:** String (Required) | `FAC-XXX` | Current facility node.

## 4. ETAEstimate Table 
* **ETAEstimateID:** String (Required) | Format: `ETA-<shipment-id>-<timestamp>` | Primary Key.
* **ShipmentID:** String (Required) | Foreign Key.
* **EstimatedDelivery:** Timestamp (Required) | Computed target arrival prediction.

## 5. WeatherEvent Table
* **WeatherEventID:** String (Required) | Format: `WTH-2026-XXXXXX` | Primary Key.
* **Location:** String (Required) | `FAC-XXX` | Affected node area.
* **Severity:** String (Required) | Allowed Values: `LIGHT`, `MODERATE`, `SEVERE` | Impact modifier for delay calculations.

## 6. Other Reference Tables
* **Carrier, Route, Facility, FacilityQueue, ServiceLevel, DelayReason:** Utilizing unique alphanumeric string keys preserving structural referential integrity.
