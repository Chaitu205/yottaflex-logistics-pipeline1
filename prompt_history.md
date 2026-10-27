# 📝 YottaFlex AI Project - Prompt History & AI Transparency

As per Section 03 of the project guidelines, this document outlines the iterative prompts used with the AI collaborator to accelerate the logistics data pipeline creation.

## 1. Initial Structural Framework Prompt
* **Prompt Given:** "Act as a Senior Logistics Data Engineer. Write a Python script using pandas and dataclasses to generate synthetic data for 11 relational tables including Shipment, Carrier, Route, Facility, and TrackingEvents. Implement deterministic zero-padded ID logic like SHP-2026-000001, and utilize a fixed seed for complete mathematical reproducibility."

## 2. Edge Case & Operational Anomaly Injection Prompt
* **Prompt Given:** "Update the generator loop to inject deliberate operational failures into a 5% baseline sample. Include cases like delivered shipments still marked in transit and impossible route date ordering. Save all injected anomaly flags into a distinct ground_truth.csv log without leaking it into core input features."

## 3. Step 8 Validation Pipeline Prompt
* **Prompt Given:** "Write a validator script using pandas to scan the generated CSV files for Primary Key uniqueness, referential bounds, and dataset integrity checks, printing explicit pass/fail output statuses."
