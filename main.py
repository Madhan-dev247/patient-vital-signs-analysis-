import pandas as pd

# Load patient data
df = pd.read_csv("data/patient-vitals.csv")


# Function to identify abnormal vital signs
def identify_abnormal_vitals(row):
    abnormal = []

    if row["Heart_Rate"] < 60 or row["Heart_Rate"] > 100:
        abnormal.append("Heart Rate")

    if row["SpO2"] < 95:
        abnormal.append("SpO2")

    if row["Temperature"] < 36.5 or row["Temperature"] > 37.5:
        abnormal.append("Temperature")

    if row["Systolic_BP"] < 90 or row["Systolic_BP"] > 140:
        abnormal.append("Systolic BP")

    if row["Diastolic_BP"] < 60 or row["Diastolic_BP"] > 90:
        abnormal.append("Diastolic BP")

    return ", ".join(abnormal) if abnormal else "None"


# Identify abnormal vital signs
df["Abnormal_Vitals"] = df.apply(identify_abnormal_vitals, axis=1)

# Assign risk status
df["Risk_Status"] = df["Abnormal_Vitals"].apply(
    lambda x: "Normal" if x == "None" else "Needs Attention"
)


# Create output folder
import os
os.makedirs("output", exist_ok=True)


# Save detailed analysis
df.to_csv("output/patient_vitals_final_analysis.csv", index=False)


# Create summary
summary = pd.DataFrame({
    "Metric": [
        "Total Patients",
        "Normal Patients",
        "Needs Attention",
        "Average Heart Rate (bpm)",
        "Average SpO2 (%)",
        "Average Temperature (°C)",
        "Average Systolic BP (mmHg)",
        "Average Diastolic BP (mmHg)"
    ],
    "Value": [
        len(df),
        (df["Risk_Status"] == "Normal").sum(),
        (df["Risk_Status"] == "Needs Attention").sum(),
        round(df["Heart_Rate"].mean(), 2),
        round(df["SpO2"].mean(), 2),
        round(df["Temperature"].mean(), 2),
        round(df["Systolic_BP"].mean(), 2),
        round(df["Diastolic_BP"].mean(), 2)
    ]
})

summary.to_csv("output/patient_vitals_summary.csv", index=False)


# Display results
print("=" * 45)
print("PATIENT VITAL SIGNS ANALYSIS")
print("=" * 45)

print(f"Total patients analyzed: {len(df)}")
print(f"Normal patients: {(df['Risk_Status'] == 'Normal').sum()}")
print(f"Patients needing attention: {(df['Risk_Status'] == 'Needs Attention').sum()}")

print("\nPatients Requiring Attention:")

attention_patients = df[df["Risk_Status"] == "Needs Attention"]

for patient in attention_patients["Patient_ID"]:
    print("-", patient)

print("\nAnalysis completed successfully!")
