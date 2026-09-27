# Virtual DataScience Internship - Week 1

## Data Acquisition, Cleaning and Exploratory Analysis

Week 1 of the Virtual Data Science with Python Apprentice Internship. This week
acquires a public dataset, checks and cleans it with documented decisions, and
explores it. The same dataset is used for the rest of the five-week project.

| Week | Repository |
|---|---|
| **1** | **Data acquisition, cleaning and EDA (this repository)** |
| 2 | [Virtual-DataScience-Internship-Week-2](https://github.com/Pharos-0/Virtual-DataScience-Internship-Week-2): visualization and storytelling |
| 3 | [Virtual-DataScience-Internship-Week-3](https://github.com/Pharos-0/Virtual-DataScience-Internship-Week-3): hypothesis testing |
| 4 | [Virtual-DataScience-Internship-Week-4](https://github.com/Pharos-0/Virtual-DataScience-Internship-Week-4): machine learning |
| 5 | [Virtual-DataScience-Internship-Week-5](https://github.com/Pharos-0/Virtual-DataScience-Internship-Week-5): final project |

## Dataset

**IBM Telco Customer Churn**: 7,043 customers x 21 columns, one row per customer of a
telecom provider that IBM describes as fictional. The target is `Churn` (Yes/No).

- Source: [IBM/telco-customer-churn-on-icp4d](https://github.com/IBM/telco-customer-churn-on-icp4d)
- Licence: Apache License 2.0. The raw file is redistributed unchanged, with the licence text, in `data/raw/`.
- Data dictionary and cleaning notes: [`data/README.md`](data/README.md)

## What was done

1. **Acquisition** (`src/01_data_acquisition.py`): download over HTTPS, SHA-256 check, licence saved with the data.
2. **Inspection** (`src/02_data_cleaning.py`): `head`, `tail`, `shape`, `columns`, `info`, `describe`,
   `describe(include="all")`, `dtypes`, unique values and `value_counts`.
3. **Missing values**: `isna()` found none, but `TotalCharges` held 11 blank strings. All belong to
   customers with `tenure = 0`, so they were set to 0 (no billing month completed). Before/after
   statistics are saved.
4. **Duplicates**: 0 duplicate rows and 0 duplicate customer IDs. The 22 rows with identical attributes
   are different customers, so they were kept.
5. **Data quality**: whitespace, label consistency, structural labels, impossible values, value ranges,
   billing consistency and IQR outliers. No rows were removed.
6. **Type corrections**: `TotalCharges` to float, `SeniorCitizen` to Yes/No, text columns to `category`,
   and a new `churn_flag`.
7. **EDA** (`src/03_eda.py`): descriptive statistics, distributions, churn rates by category and tenure
   band, Pearson/Spearman correlations and Cramer's V, with seven charts (including a tenure trend
   line and a tenure vs total-charges scatter plot).

## Key results

| Check | Result |
|---|---|
| Raw shape | 7,043 rows x 21 columns |
| Hidden missing values | 11 blank `TotalCharges` values (0.16%), all with `tenure = 0`, set to 0 |
| Duplicate rows / IDs | 0 / 0 (no rows removed) |
| Overall churn rate | 26.54% (1,869 of 7,043) |

- Churn was 42.7% on month-to-month contracts, against 11.3% (one year) and 2.8% (two years).
- Churn was 47.4% in the first 12 months of tenure and 6.6% after 61-72 months.
- Fibre optic customers (41.9%) and electronic-check payers (45.3%) had the highest churn in their groups.
- Tenure had the strongest correlation with churn (r = -0.35), and `Contract` the strongest categorical
  association (Cramer's V = 0.41).

These are descriptive associations, not causal effects. They are tested in Week 3.

## Repository structure

```
|-- README.md
|-- requirements.txt
|-- data/
|   |-- README.md                    # source, licence, data dictionary
|   |-- raw/                         # original CSV + Apache 2.0 licence
|   `-- processed/                   # cleaned dataset (7,043 x 22)
|-- notebooks/
|   |-- Week_1_Analysis.ipynb        # executed notebook (same code as src/)
|   `-- build_notebook.py            # rebuilds and executes the notebook
|-- src/
|   |-- config.py                    # paths, source URL, checksum, seed
|   |-- data_utils.py                # loads the cleaned data with dtypes
|   |-- plot_style.py                # shared chart style
|   |-- 01_data_acquisition.py
|   |-- 02_data_cleaning.py
|   `-- 03_eda.py
|-- outputs/
|   |-- figures/                     # fig1_1 ... fig1_7
|   |-- tables/                      # 13 CSV tables (missing values, dtypes, statistics, ...)
|   `-- results/                     # acquisition, cleaning and EDA summaries (JSON)
`-- screenshots/                     # 15 screenshots of the executed notebook
```

## How to reproduce

Tested with Python 3.11.9 (pandas 3.0.6, NumPy 2.4.6, Matplotlib 3.11.2, SciPy 1.17.1).

```bash
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python src/01_data_acquisition.py    # download (if missing) and verify the raw data
python src/02_data_cleaning.py       # inspection and cleaning -> data/processed/
python src/03_eda.py                 # EDA tables, figures and summary -> outputs/
python notebooks/build_notebook.py   # optional: rebuild and execute the notebook
```

Every step is deterministic, so re-running the scripts reproduces the files in `outputs/` exactly.

## Notebook and screenshots

The scripts are written in Jupytext "percent" format, so each `# %%` block becomes a notebook cell.
`notebooks/Week_1_Analysis.ipynb` is built from them and executed top to bottom, which means it
contains the same code as `src/`. The images in `screenshots/` are crops of that executed notebook,
rendered with nbconvert's JupyterLab template in headless Chrome.

## Limitations

- The data describes a fictional company (per IBM) at a single point in time, with no dates.
- `MonthlyCharges` is the current price only, so past price changes are not recorded.
- The findings are associations and do not establish cause and effect.

The written report for this week is submitted separately through the internship portal.
