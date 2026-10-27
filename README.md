# yottaflex-logistics-pipeline1
# 🏥 YottaFlex AI - Synthetic Logistics Data Pipeline

This repository contains a production-ready data engineering solution to generate and validate large-scale synthetic operational datasets for a global logistics network.

## 📂 Repository Contents
* `generator.py` - The core deterministic script simulating 50,000 shipments and 300,000 sequential tracking events with a fixed seed (`20261022`).
* `validator.py` - Automated execution pipeline enforcing primary key constraints and structural integrity scans.
* `data_dictionary.md` - Complete schema definitions, formatting specs, and static bound rules for all 11 target entities.
* `prompt_history.md` - Transparent logging of interactive prompts utilized with the LLM collaborator.

## 🚀 Quick Start
To generate the datasets locally, clone this repository and run the scripts using the following terminal commands:
```bash
pip install pandas numpy
python generator.py
python validator.py
```
