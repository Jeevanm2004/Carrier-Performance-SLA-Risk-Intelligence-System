## Step 1: Business Understanding

This project focuses on predicting SLA (Service Level Agreement) breaches in a B2B logistics environment.

An SLA breach occurs when a shipment is delivered later than the contractually agreed planned delivery time. Such breaches lead to penalty costs, reduced customer trust, and operational inefficiencies.

The business objective is to proactively identify shipments that are at risk of breaching SLAs so that corrective actions (carrier change, route optimization, or escalation) can be taken before execution.

---

## Step 2: Initial Data Loading & Familiarization

The dataset represents shipment-level records extracted from a simulated Transportation Management System (TMS).

- Each row corresponds to a single shipment.
- The data includes carrier details, shipment characteristics, cost metrics, planned vs actual delivery timelines, and geographic attributes.
- Initial exploration focused on understanding dataset size, column structure, data types, and overall completeness before any transformations.

## Step 3: Initial Data Assessment

### Dataset Overview
- Total number of rows: ~200,000 shipment records.
- Total number of columns: Multiple shipment-related attributes.
- Each row represents a single shipment executed by a logistics carrier under an SLA.

### Data Types
- Numeric columns include delivery days, shipping cost, weight, and volume related fields.
- Categorical columns include carrier, shipping mode, region, origin country, and destination country.
- Date or time-related columns appear to be stored as text and may require type conversion.

### Missing Values
- Some columns contain missing values.
- Missing data appears mainly in operational or descriptive fields and will require business-justified handling during cleaning.

### Data Quality Observations
- Some zero or extreme values may exist in delivery and cost-related fields.
- Wide ranges are observed in cost, weight, and delivery duration metrics.
- Certain columns may require data type corrections, especially date-related fields.

### Duplicate Records
- A shipment-level identifier appears to be present.
- Duplicate records may exist and will be evaluated and handled during the data cleaning phase.

## Step 4: Data Cleaning
- Missing values handled using median for numeric fields and 'Unknown' for categorical fields.
- Date-related columns converted to datetime format where applicable.
- Exact duplicate records removed.
- Invalid negative or zero operational values filtered.
- Cleaned dataset saved for further processing.

## Step 5: Target Variable Creation
- Created binary target variable `sla_breach_flag`.
- A value of 1 indicates actual delivery days exceeded planned delivery days (SLA breach).
- A value of 0 indicates the shipment met the SLA.
- The target definition aligns directly with business SLA contracts.
- Class distribution was reviewed to understand breach frequency.

## Step 6: Categorical Encoding
- Selected business-relevant categorical variables for encoding.
- Applied one-hot encoding to carrier, shipping mode, region, origin, and destination fields.
- High-cardinality identifiers were excluded to prevent dimensional explosion.
- Encoded dataset saved for downstream modeling.

## Step 7: Final Data Validation
- Verified no negative values in critical numeric business fields.
- Confirmed SLA breach flag contains valid binary values (0 and 1).
- Final dataset validated for consistency and business readiness.
- Dataset approved for downstream analytics and modeling.
