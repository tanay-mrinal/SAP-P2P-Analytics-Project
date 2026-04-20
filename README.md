# SAP Procure-to-Pay (P2P) Analytics Project
Procure-to-Pay (P2P) Cycle with Procurement Analytics (SAP MM Project)

## Overview

This project presents a structured simulation of the Procure-to-Pay (P2P) cycle within SAP Materials Management (MM), combined with procurement data analytics.

The objective is to demonstrate how SAP-driven procurement processes generate structured data and how that data can be analyzed to derive meaningful business insights.

---

## Case Study

A fictional organization, ABC Manufacturing Ltd, is used to model real-world procurement operations involving multiple vendors, materials, and monthly purchasing activities.

---

## SAP P2P Process Covered

The project follows the complete end-to-end procurement lifecycle:

* Purchase Requisition (ME51N)
* Purchase Order (ME21N)
* Goods Receipt (MIGO)
* Invoice Verification (MIRO)
* Vendor Payment (F-53)

Each step reflects standard SAP MM transaction flow and document linkage.

---

## Data Analytics Performed

The procurement dataset is analyzed to extract key business insights:

* Vendor-wise procurement analysis
* Monthly spending trends
* Cost comparison across vendors

### Key Insights:

* Identification of vendor dependency risk
* Opportunities for cost optimization
* Detection of demand fluctuation patterns

---

## Tools & Technologies

* SAP Concepts – MM Module (simulated environment)
* Microsoft Excel – Data modeling, formulas, and visualization
* Python (Pandas, Matplotlib) – Data processing and chart generation

---

## Project Structure

* report.pdf → Detailed project documentation
* p2p_data_final.xlsx → Procurement dataset
* analysis.py → Python-based data analysis
* python_chart.png → Generated visualization

---

## Python-Based Analysis

The Python script processes procurement data and performs vendor-wise aggregation to compute total spending.

```python
data.groupby("Vendor")["Total"].sum()
```

Additionally, a bar chart is generated programmatically to visualize vendor contribution.

---



*This project is a conceptual simulation due to limited access to a live SAP system. However, all process flows, transaction codes, and business logic are aligned with standard SAP MM practices.*

---
