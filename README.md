# 🚚 Carrier-Performance-SLA-Risk-Intelligence-System

> **Predictive B2B Supply Chain Intelligence for Proactive Carrier & SLA Management**

---

## 📌 Overview

Enterprises spend millions annually on logistics while relying on **reactive performance indicators** such as average delivery time and monthly carrier scorecards. These indicators fail to provide **early warnings** when a carrier or route is silently degrading.

The **Carrier Performance & SLA Risk Intelligence Platform** is a data-driven solution that transforms shipment-level logistics data into **predictive, explainable, and actionable intelligence**.

This project simulates a **real B2B enterprise use case**, designed to mirror how analytics and machine learning are applied in large manufacturing, retail, and distribution organizations.

---

## 🏢 Business Context

**Client (Simulated):** Apex Manufacturing Ltd.
**Industry:** Manufacturing / Retail Distribution
**Annual Logistics Spend:** $50M–$200M
**Operational Regions:** APAC, EMEA, AMER

### Key Business Question

> **Which carrier is most likely to breach SLA in upcoming shipments, on which routes, and why?**

---

## 🎯 Project Objectives

### Primary Objective

* Predict **SLA breach risk** *before* shipment execution.

### Secondary Objectives

* Improve carrier selection decisions
* Reduce SLA penalties and operational firefighting
* Support procurement contract negotiations
* Balance cost vs reliability trade-offs
* Improve customer fulfillment performance

---

## 🧠 Solution Summary

The platform:

* Ingests shipment-level data from a simulated TMS
* Engineers carrier, route, and mode risk signals
* Trains ML models to predict SLA breach probability
* Provides explainable insights for business users
* Supports decision-making via dashboards and APIs

---

## 📊 Dataset Overview

| Metric          | Value                 |
| --------------- | --------------------- |
| Total Rows      | **200,000 shipments** |
| Carriers        | 7                     |
| Transport Modes | Road, Sea, Air, Rail  |
| Regions         | APAC, EMEA, AMER      |
| Granularity     | 1 row = 1 shipment    |

The dataset is **synthetic but enterprise-realistic**, structured to resemble real ERP/TMS exports.

---

## 📁 Repository Structure

```
carrier-sla-risk-intelligence/
│
├── data/
│   ├── raw/
│   │   └── b2b_carrier_sla_risk_intelligence_100k.csv
│   ├── processed/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_explainability.ipynb
│
├── src/
│   ├── data_pipeline/
│   │   ├── ingestion.py
│   │   ├── validation.py
│   │   └── preprocessing.py
│   │
│   ├── features/
│   │   └── feature_engineering.py
│   │
│   ├── models/
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── evaluate.py
│   │
│   └── api/
│       └── app.py
│
├── docs/
│   ├── architecture.md
│   ├── dataset_metadata.md
│   ├── business_context.md
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📘 Dataset & Metadata

### Core Columns

| Column                | Description                |
| --------------------- | -------------------------- |
| shipment_id           | Unique shipment identifier |
| vendor                | Logistics carrier          |
| shipping_mode         | Road / Sea / Air / Rail    |
| origin_country        | Shipment origin            |
| destination_country   | Shipment destination       |
| region                | Operational region         |
| planned_delivery_days | SLA commitment             |
| actual_delivery_days  | Actual delivery            |
| delivery_delay_days   | SLA deviation              |
| shipping_cost_usd     | Shipment cost              |
| sla_breach_flag       | ML target variable         |

---

## 🤖 Machine Learning Design

### ML Problem

Binary classification:

```text
sla_breach_flag ∈ {0,1}
```

### Models Used

* Logistic Regression (baseline)
* Random Forest
* Gradient Boosting

### Key Features

* Carrier rolling SLA breach rate
* Route delay volatility
* Mode-specific risk profiles
* Cost vs reliability indicators
* Priority & fragile shipment flags

---

## 🔍 Explainability & Trust

Enterprise adoption requires **transparent AI**.

This project includes:

* Feature importance analysis
* SHAP value explanations
* Business-friendly risk drivers
* Audit-ready predictions

---

## 🔌 API Interfaces (Conceptual)

### Predict Shipment SLA Risk

```http
POST /api/shipments/predict
```

**Response**

```json
{
  "sla_risk_score": 0.31,
  "risk_level": "Medium",
  "top_drivers": [
    "Carrier historical delays",
    "Route volatility"
  ]
}
```

---

## 📈 Business Outputs

* Carrier Risk Scorecards
* Route-Mode SLA Heatmaps
* Cost vs Reliability Dashboards
* Procurement Decision Insights

---

## 🧪 How to Run the Project

```bash
# Clone repository
git clone https://github.com/Technocolabs100/Carrier-Performance-SLA-Risk-Intelligence-System.git
cd carrier-sla-risk-intelligence

# Install dependencies
pip install -r requirements.txt

# Run notebooks or scripts
jupyter notebook
```

---

## 🏆 Why This Project Matters

* Realistic B2B logistics problem
* Predictive, not descriptive analytics
* Explainable machine learning
* Scalable enterprise design
* Suitable for consulting, product, and analytics roles

---

## 📌 Intended Audience

* Supply Chain Analytics Teams
* Data Scientists & ML Engineers
* Enterprise Architects
* Interns & Early-Career Professionals
* Consulting & Product Teams

---

## 🚀 Future Enhancements

* Time-series SLA forecasting
* External disruption signals (weather, ports)
* Multi-carrier optimization
* Real-time scoring APIs
* Integration with ERP/TMS systems

---

## 📄 License

This project is provided for **educational and demonstration purposes** and simulates real-world enterprise use cases.

---

### ⭐ Final Note

This repository demonstrates how **data, machine learning, and business context** come together to solve a **real B2B supply chain problem** — exactly how it happens in industry.

---
