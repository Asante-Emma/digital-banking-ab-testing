# A/B Testing Report

## Business Problem

A digital bank wants to evaluate whether a redesigned online loan application experience improves the rate at which customers complete their loan applications.

The bank is considering a **simplified loan application experience** designed to make the application process easier and faster for customers.

The objective of the A/B test is to determine whether the redesigned experience produces a measurable difference in application completion compared with the existing experience.

---

## Experiment Design

The experiment compares two groups:

* **Control:** Customers using the existing online loan application experience.
* **Treatment:** Customers using the redesigned, simplified loan application experience.

Participants are randomly assigned to either the Control or Treatment group.

### Primary Metric

The primary metric is the **application completion rate**.

$$
\text{Completion Rate}
=
\frac{\text{Completed Applications}}
{\text{Application Starters}}
$$

Because all participants in this synthetic experiment started the application, the completion rate is calculated as the proportion of participants who completed their application.

### Secondary Metrics

The experiment also considers:

* **Application completion time:** Average time required to complete the application.
* **Loan approval rate:** Proportion of participants whose loan applications were approved.

These secondary metrics provide additional context about the potential impact of the redesigned experience.

---

## Statistical Hypotheses

The primary hypothesis tests whether the application completion rate differs between the Control and Treatment groups.

### Null Hypothesis ($H_0$)

There is no difference in application completion rates between the Control and Treatment groups.

$$
H_0: p_T = p_C
$$

where:

* $p_T$ = Treatment completion rate
* $p_C$ = Control completion rate

### Alternative Hypothesis ($H_1$)

There is a difference in application completion rates between the two groups.

$$
H_1: p_T \neq p_C
$$

A significance level of:

$$
\alpha = 0.05
$$

was used.

---

## Statistical Method

A **two-proportion z-test** was used because the primary outcome, `application_completed`, is a binary variable with two possible outcomes:

* `1` = application completed
* `0` = application not completed

The test evaluates whether the observed difference in completion rates between the Control and Treatment groups is sufficiently large relative to sampling variability to provide evidence against the null hypothesis.

A 95% confidence interval was also calculated for the difference between the Treatment and Control completion rates.

---

## Data Quality and Experiment Validation

The experiment dataset contains **20,000 observations** across **16 variables**.

The data quality checks produced the following results:

| Check                                    | Result |
| ---------------------------------------- | -----: |
| Total observations                       | 20,000 |
| Total columns                            |     16 |
| Duplicate user IDs                       |      0 |
| Control participants                     | 10,046 |
| Treatment participants                   |  9,954 |
| Invalid binary values                    |      0 |
| Applications started incorrectly         |      0 |
| Completed applications without starting  |      0 |
| Approved applications without completion |      0 |

The data validation checks passed successfully.

The missing-value count was **16,824**. These missing values are associated with `application_time_minutes` for participants who did not complete their applications. Therefore, the missing completion-time values are expected rather than automatically treated as data-quality errors.

---

## Results

### Primary A/B Test

| Metric                  |  Control | Treatment |
| ----------------------- | -------: | --------: |
| Participants            |   10,046 |     9,954 |
| Completed applications  |    1,446 |     1,730 |
| Completion rate         |   14.39% |    17.38% |
| Average completion time | 7.66 min |  6.93 min |
| Approved applications   |      530 |       626 |
| Approval rate           |    5.28% |     6.29% |

### Treatment Effect

The observed difference in completion rates was:

**Absolute lift: 2.99 percentage points**

$$
17.38\% - 14.39\% = 2.99\%
$$

The relative lift was:

**20.75%**

$$
\frac{17.38\%-14.39\%}{14.39\%}
\times 100
\approx 20.75\%
$$

### Statistical Test

| Statistic                             |         Result |
| ------------------------------------- | -------------: |
| Z-statistic                           |         5.7772 |
| P-value                               | 7.59475 × 10⁻⁹ |
| Significance level ($\alpha$)         |           0.05 |
| 95% CI for Treatment − Control        | [1.97%, 4.00%] |
| Statistically significant at α = 0.05 |            Yes |

---

## Segment Analysis: Device Type

The experiment was also examined across device types.

| Device | Group     | Users | Completed | Completion Rate |
| ------ | --------- | ----: | --------: | --------------: |
| Mobile | Control   | 6,254 |       896 |          14.33% |
| Mobile | Treatment | 6,119 |     1,057 |          17.27% |
| Tablet | Control   |   603 |        76 |          12.60% |
| Tablet | Treatment |   601 |        85 |          14.14% |
| Web    | Control   | 3,189 |       474 |          14.86% |
| Web    | Treatment | 3,234 |       588 |          18.18% |

The Treatment group has a higher observed completion rate across all three device categories in this synthetic experiment.

However, these segment-level differences should be interpreted as exploratory unless separate statistical tests and appropriate multiple-comparison controls are performed.

---

## Interpretation

The Treatment group had a higher application completion rate than the Control group:

* Control: **14.39%**
* Treatment: **17.38%**
* Absolute difference: **2.99 percentage points**
* Relative lift: **20.75%**

The two-proportion z-test produced a p-value of approximately **7.59 × 10⁻⁹**, which is substantially below the predefined significance level of 0.05. The 95% confidence interval for the Treatment-minus-Control difference ranged from **1.97 to 4.00 percentage points**.

Therefore, within this synthetic experiment, the observed difference is **statistically significant at the 5% significance level**.

### Statistical Significance vs. Practical Significance

Statistical significance addresses the question:

> **Is the observed difference unlikely to be explained by random sampling variation under the null hypothesis?**

Practical or business significance asks a different question:

> **Is the size of the observed improvement large enough to matter to the business?**

The observed relative lift of **20.75%** and absolute increase of approximately **2.99 percentage points** provide an effect size that can be considered alongside implementation costs, expected application volume, customer experience, operational capacity, and other business considerations.

Statistical significance alone does not establish that an implementation is economically worthwhile.

---

## Secondary Metrics

The Treatment group also showed a lower average completion time:

* Control: **7.66 minutes**
* Treatment: **6.93 minutes**

This represents an observed reduction of approximately **0.73 minutes**, or about **44 seconds**, in this synthetic dataset.

The Treatment group also had a higher observed loan approval rate:

* Control: **5.28%**
* Treatment: **6.29%**

However, loan approval is affected by factors beyond the application interface, such as applicant characteristics and creditworthiness. Therefore, the approval-rate difference should not automatically be attributed to the redesigned application experience without further analysis.

---

## Limitations

### 1. Synthetic Dataset

The dataset is **synthetic** and was created for learning and portfolio demonstration.

The results should therefore **not be interpreted as evidence about actual digital banking customers or real-world loan applications**.

### 2. Simulated Experiment

The Control and Treatment groups were generated as part of a simulated A/B-testing environment. A real production experiment would require actual users, a controlled randomization process, experiment instrumentation, and appropriate monitoring.

### 3. External Validity

Because the data is synthetic, the observed effect may not generalize to a real banking population.

### 4. Secondary Metrics

Completion time and loan approval provide useful additional context, but they require further investigation before drawing causal conclusions about the redesigned experience.

### 5. Segment Analysis

The device-level analysis is exploratory. Additional statistical testing would be required to determine whether differences within individual segments are statistically reliable.

---

## Conclusion

This project demonstrates an end-to-end A/B testing workflow for evaluating a redesigned digital banking loan application.

The analysis covers:

1. Data quality validation
2. Control and Treatment group comparison
3. Primary conversion metric calculation
4. Absolute and relative lift
5. Two-proportion z-test
6. P-value interpretation
7. Confidence intervals
8. Secondary metric analysis
9. Device-level segmentation
10. Distinction between statistical and practical significance

Within the **synthetic dataset**, the Treatment group recorded a higher application completion rate than the Control group, with an observed absolute difference of **2.99 percentage points** and a relative lift of **20.75%**. The difference was statistically significant at the 5% significance level.

The project is intended primarily to demonstrate the methodology and reasoning involved in designing, validating, analyzing, and interpreting an A/B test.

---

## Project Note

**Dataset:** Synthetic digital banking A/B testing dataset

**Primary outcome:** Loan application completion

**Statistical test:** Two-proportion z-test

**Significance level:** α = 0.05

**Confidence level:** 95%

**Purpose:** Data Science / A/B Testing learning and portfolio demonstration

