# Rule-Based Classification - Gezinomi Case Study

## Business Problem
Gezinomi aims to create level-based sales definitions using existing sales data and estimate the average revenue potential of new customers based on these segments.

**Example:** Estimating the average revenue from a customer who wants to stay at an all-inclusive hotel in Antalya during a busy season.

## Dataset
| File | Description |
|---|---|
| `miuul_gezinomi.xlsx` | Gezinomi sales data including city, concept, season and price information |

## Tasks
| Task | Description |
|---|---|
| Task 1 | Load dataset and explore general information (unique values, frequencies, revenue by city/concept) |
| Task 2 | Convert SaleCheckInDayDiff to categorical EB_Score variable |
| Task 3 | Analyze average price and frequency by City-Concept-EB_Score / Season / CInDay breakdown |
| Task 4 | Sort City-Concept-Season breakdown by price and save as agg_df |
| Task 5 | Convert index names to column variables |
| Task 6 | Create level-based sales definitions (CITY_CONCEPT_SEASON format) |
| Task 7 | Divide personas into segments (A, B, C, D) based on price |
| Task 8 | Predict revenue for a new customer profile |

## Topics Covered
- GroupBy and aggregation
- pd.cut for custom binning
- Level-based persona creation
- Customer segmentation with pd.qcut
- Rule-based classification

## Tools & Libraries
- Python 3.x
- pandas
- openpyxl (for reading .xlsx files)
