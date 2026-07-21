# Rule-Based Classification - Persona Case Study

## Business Problem
Creating level-based customer personas using country, source, sex and age data, and estimating the average revenue potential of new customers based on these segments.

**Example:** How much revenue can a 33-year-old Turkish female Android user generate?

## Dataset
| File | Description |
|---|---|
| `persona.csv` | Customer data including country, source, sex, age and price information |

## Tasks
| Task | Description |
|---|---|
| Task 1 | Load dataset and explore general information |
| Task 2 | Find average price by country, source, sex and age breakdown |
| Task 3 | Sort by price in descending order and save as agg_df |
| Task 4 | Convert index names to column variables |
| Task 5 | Create age categories (0_18, 19_23, 24_30, 31_40, 41+) |
| Task 6 | Create level-based customer definitions (COUNTRY-SOURCE-SEX-AGE_CAT format) |
| Task 7 | Divide personas into segments (A, B, C, D) based on price |
| Task 8 | Predict segment and revenue for a new customer profile |

## Topics Covered
- GroupBy and aggregation
- pd.cut for custom age binning
- Level-based persona creation
- Customer segmentation with pd.qcut
- Rule-based classification

## Tools & Libraries
- Python 3.x
- pandas
