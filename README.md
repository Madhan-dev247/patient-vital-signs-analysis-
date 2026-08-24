# Patient Vital Signs Analysis

## 🩺 Biomedical Patient Data Analysis Using Python

A Python-based biomedical data analysis project for analyzing patient vital signs and identifying patients who may require further attention.

The project analyzes important physiological parameters such as heart rate, SpO₂, temperature, systolic blood pressure, and diastolic blood pressure.

---

## 📌 Project Overview

Patient vital signs provide important information about a person's physiological condition.

This project uses Python and data analysis techniques to:

- Analyze patient vital signs
- Compare measurements with predefined reference ranges
- Identify abnormal vital signs
- Classify patients based on risk status
- Calculate average vital-sign values
- Study relationships between different vital signs
- Generate graphical visualizations
- Produce summary reports

---

## 🎯 Objectives

1. Analyze patient vital-sign data using Python.
2. Identify patients with abnormal physiological measurements.
3. Classify patients into **Normal** and **Needs Attention** categories.
4. Visualize vital-sign measurements using graphs.
5. Study correlations between different physiological parameters.
6. Generate processed data and summary reports for further analysis.

---

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- GitHub

---

## 📊 Dataset

The dataset contains information for **10 patients**.

### Parameters

| Parameter | Description |
|---|---|
| Patient ID | Unique patient identifier |
| Age | Patient age |
| Gender | Patient gender |
| Heart Rate | Heart rate in beats per minute |
| SpO₂ | Blood oxygen saturation percentage |
| Temperature | Body temperature in °C |
| Systolic BP | Systolic blood pressure in mmHg |
| Diastolic BP | Diastolic blood pressure in mmHg |

The original dataset is available in:

`data/patient-vitals.csv`

---

## 🔬 Methodology

The project follows these major steps:

### 1. Data Loading

The patient dataset is loaded using Pandas.

### 2. Data Inspection

The dataset is examined using:

- `head()`
- `info()`
- Statistical summaries
- Data validation

### 3. Vital-Sign Analysis

The following parameters are analyzed:

- Heart Rate
- SpO₂
- Temperature
- Systolic Blood Pressure
- Diastolic Blood Pressure

### 4. Risk Classification

Patients are classified based on predefined reference ranges.

Patients with abnormal measurements are marked as:

**Needs Attention**

while patients within the defined ranges are classified as:

**Normal**

### 5. Visualization

Graphs are generated to compare patient measurements with reference values.

### 6. Correlation Analysis

A correlation matrix and heatmap are used to study relationships between the different vital signs.

### 7. Report Generation

Processed patient data and summary statistics are exported as CSV files.

---

## 📈 Visualizations

The project includes visual analysis of:

- Patient heart rate
- SpO₂ levels
- Body temperature
- Blood pressure
- Risk-status distribution
- Correlation between vital signs

---

## 📋 Results

A total of **10 patients** were analyzed.

| Result | Value |
|---|---:|
| Total Patients | 10 |
| Normal Patients | 8 |
| Needs Attention | 2 |
| Average Heart Rate | 84.50 bpm |
| Average SpO₂ | 96.30% |
| Average Temperature | 37.19 °C |
| Average Systolic BP | 131.80 mmHg |
| Average Diastolic BP | 85.60 mmHg |

### Patients Requiring Attention

The analysis identified:

- **P005**
- **P007**

These patients showed multiple vital-sign values outside the predefined reference ranges and were therefore classified as **Needs Attention**.

> This project is intended for educational and data-analysis purposes and does not provide medical diagnosis.

---

## 📁 Project Structure

```text
patient-vital-signs-analysis/
│
├── data/
│   └── patient-vitals.csv
│
├── notebooks/
│   └── patient_vitals_analysis.ipynb
│
├── output/
│   ├── patient_vitals_final_analysis.csv
│   └── patient_vitals_summary.csv
│
├── README.md
└── requirements.txt
