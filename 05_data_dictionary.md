# ER Dataset – Data Dictionary & Field Reference

## Dataset Overview

This mock dataset contains detailed information on patient visits to the **ABC Emergency Room (ER)** across multiple dates and times. Each record represents a **distinct ER visit**. The data covers the period **October 2022 – August 2024**.

- The same patient may appear multiple times (repeat visits use the same `patient_id`).
- The dataset is intended to be complete but may contain anomalies due to its mock nature.

---

## Field Definitions

### Date_and_Time
- **Type**: Datetime
- **Description**: The exact date and time when the patient arrived at the ER.
- **Format**: YYYY-MM-DD HH:MM:SS

---

### Hour_of_day
- **Type**: Integer (0–23)
- **Description**: The specific hour during which the patient arrived, in 24-hour format.
- **Example**: 14 = 2:00 PM

---

### patient_id
- **Type**: String / Unique Identifier
- **Description**: A unique identifier for each patient. The same patient_id may appear in multiple rows if the patient visited the ER more than once.

---

### patient_gender
- **Type**: Categorical
- **Values**: Male, Female
- **Description**: The gender of the patient.

---

### patient_age
- **Type**: Integer
- **Description**: The age of the patient at the time of the ER visit.
- **Dashboard Age Buckets**: 1–10, 11–20, 21–30, 31–40, 41–50, 51–60, 61–70, 71–80

---

### patient_first_initial
- **Type**: String (single character)
- **Description**: The first initial of the patient's first name.

---

### patient_last_name
- **Type**: String
- **Description**: The patient's last name.

---

### patient_race
- **Type**: Categorical
- **Values**:
  - White
  - African American
  - Asian
  - Two or More Races
  - Pacific Islander
  - Native American/Alaska Native
  - Declined to Identify
- **Description**: The racial background of the patient as self-reported or recorded.

---

### department_referral
- **Type**: Categorical
- **Values**:
  - General Practice
  - Orthopedics
  - Gastroenterology
  - Cardiology
  - Physiotherapy
  - Neurology
  - Renal
- **Description**: The department within the hospital to which the patient was referred during their ER visit.

---

### month
- **Type**: String / Date
- **Description**: The month of the patient's visit.
- **Format**: MMM YYYY (e.g., "Oct 2022")

---

### patient_waittime
- **Type**: Float / Integer
- **Unit**: Minutes
- **Description**: The duration in minutes the patient waited before being attended to by medical personnel.
- **KPI Target**: ≤ 30 minutes
- **Dashboard Average**: 37.71 minutes
- **Key Finding**: 61.52% of visits exceed the 30-minute target

---

### patient_admitted_flag
- **Type**: Boolean
- **Values**: True / False
- **Description**: Indicates whether the patient was admitted to the hospital following their ER visit.
- **Dashboard Admission Rate**: 42.19%
- **Insight**: Admitted patients report significantly higher satisfaction (+1.17 pts) than non-admitted patients.

---

### patient_satisfaction_score
- **Type**: Numeric
- **Scale**: 1–10
- **Description**: A numerical score reflecting the patient's satisfaction with their ER experience.
- **Dashboard Average**: 6.0 / 10

---

## Business Rules and Derived Metrics

| Metric | Definition |
|---|---|
| Visit Delay Flag | patient_waittime > 30 minutes |
| % Visits Exceeding Target | (count of visits where waittime > 30) / total visits × 100 |
| Admission Rate | (count where patient_admitted_flag = True) / total visits × 100 |
| Weekend Flag | Whether the visit occurred on a Saturday or Sunday |
| Age Bucket | patient_age grouped into 10-year bands (1–10, 11–20, ... 71–80) |
| Time of Day | Morning: 6AM–12PM, Afternoon: 12PM–6PM, Evening: 6PM–10PM, Night: 10PM–6AM |

---

## Monthly Trend Summary

The dashboard tracks metrics monthly from October 2022 to August 2024. Peak delay months were January–March 2023 (78%+ delayed visits). Recent 2024 months show improvement in delay rates (50–58%) but remain well above the 30% target.
