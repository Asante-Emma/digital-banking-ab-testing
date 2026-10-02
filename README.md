# Digital Banking A/B Testing: Optimizing Loan Application Conversion

## Project overview
An end-to-end A/B testing project evaluating whether a redesigned digital loan application changes application completion. **The dataset is synthetic** and is for learning/portfolio demonstration.

## Business problem
A digital bank is experiencing drop-off during online loan applications. The product team proposes a simplified flow and wants quantitative evidence about whether completion changes.

## Experiment
- Control (A): existing application experience
- Treatment (B): simplified application experience
- Primary metric: application completion rate
- Secondary metrics: completion time and loan approval rate
- Exploratory segments: device, employment status, customer status, etc.

## Dataset
20,000 synthetic participants with customer attributes, experiment assignment, application outcomes and downstream approval. Key fields include `user_id`, `experiment_group`, `credit_score`, `loan_amount`, `application_completed`, `application_time_minutes`, `device_type`, `previous_customer`, and `loan_approved`.

## Project structure
```text
digital-banking-ab-testing/
├── data/
│   └── digital_banking_ab_testing_synthetic_dataset.csv
├── notebooks/
│   └── 01_ab_testing_analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── data_preparation.py
│   ├── experiment_analysis.py
│   └── visualization.py
├── tests/
│   ├── test_data_preparation.py
│   └── test_experiment_analysis.py
├── reports/
│   └── ab_testing_report.md
├── run_analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Windows activation: `.venv\Scripts\activate`.

## Run tests
```bash
pytest -q
```
Tests cover schema validation, invalid experiment groups, invalid application states, conversion calculations, lift, the two-proportion z-test, confidence intervals, and an end-to-end result calculation.

## Run analysis
```bash
python run_analysis.py
```
This loads and validates the dataset, prints group summaries, calculates conversion rates/lift, runs the primary two-proportion z-test, reports confidence intervals, performs device-level exploratory analysis, and creates charts under `reports/figures/`.

## Hypotheses
Null: `H0: p_treatment = p_control`

Alternative: `H1: p_treatment != p_control`

The primary analysis uses a two-sided test at `alpha = 0.05`.

## Core calculations
Absolute lift = treatment conversion rate - control conversion rate.

Relative lift = (treatment - control) / control.

A 95% confidence interval is calculated for the treatment-minus-control difference.

## How to interpret the result
Do not stop at the p-value. Consider statistical significance, effect size, confidence interval, secondary metrics, experiment validity, and whether the effect is practically meaningful to the business.

## Segment analysis
Device and other segments can be explored after the primary test. Segment results are exploratory and multiple comparisons can increase false-positive risk.

## Learning objectives
A/B test design, control/treatment concepts, hypotheses, p-values, confidence intervals, two-proportion z-tests, absolute/relative lift, statistical vs practical significance, data validation, segment analysis, visualization, pytest, and business communication.

## Portfolio note
Because this experiment is synthetic, its numerical results must not be presented as evidence from a real bank or real customers. The portfolio value is demonstrating a rigorous A/B testing workflow.
