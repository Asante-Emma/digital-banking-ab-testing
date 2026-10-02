"""Data loading and quality checks."""
from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS=["user_id","experiment_group","age","gender","income","employment_status","credit_score","loan_amount","loan_term_months","application_started","application_completed","application_time_minutes","application_date","device_type","previous_customer","loan_approved"]
BINARY_COLUMNS=["application_started","application_completed","previous_customer","loan_approved"]

def load_data(path):
    path=Path(path)
    if not path.exists(): raise FileNotFoundError(f"Dataset not found: {path}")
    df=pd.read_csv(path,parse_dates=["application_date"]); validate_schema(df); return df

def validate_schema(df):
    missing=[c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing: raise ValueError(f"Missing required columns: {missing}")
    if df.user_id.duplicated().any(): raise ValueError("user_id must be unique.")
    groups=set(df.experiment_group.dropna().unique())
    if not groups.issubset({"control","treatment"}): raise ValueError(f"Unexpected experiment groups: {groups}")

def quality_report(df):
    return {"rows":len(df),"columns":len(df.columns),"duplicate_user_ids":int(df.user_id.duplicated().sum()),"missing_values":int(df.isna().sum().sum()),"group_counts":df.experiment_group.value_counts().to_dict(),"invalid_binary_values":{c:sorted(set(df[c].dropna().unique())-{0,1}) for c in BINARY_COLUMNS},"started_not_one":int((df.application_started!=1).sum()),"completed_without_start":int(((df.application_completed==1)&(df.application_started!=1)).sum()),"approved_without_completion":int(((df.loan_approved==1)&(df.application_completed!=1)).sum())}

def validate_data(df):
    validate_schema(df)
    allowed_time_missing = df["application_time_minutes"].isna() & (df["application_completed"] == 0)
    unexpected_missing = df.isna() & ~pd.DataFrame({"application_time_minutes": allowed_time_missing}).reindex(columns=df.columns, fill_value=False)
    if unexpected_missing.any().any(): raise ValueError("Dataset contains unexpected missing values.")
    if df.loc[df["application_completed"] == 1, "application_time_minutes"].isna().any(): raise ValueError("Completed applications must have completion time.")
    for c in BINARY_COLUMNS:
        if not set(df[c].unique()).issubset({0,1}): raise ValueError(f"{c} contains values other than 0 and 1.")
    if ((df.application_completed==1)&(df.application_started!=1)).any(): raise ValueError("A completed application cannot exist without a start.")
    if (df.application_started!=1).any(): raise ValueError("All experiment participants should have started the application.")
    if ((df.loan_approved==1)&(df.application_completed!=1)).any(): raise ValueError("A loan cannot be approved without a completed application.")
    if (df.age<18).any(): raise ValueError("Age contains values below 18.")
    if not df.credit_score.between(300,850).all(): raise ValueError("Credit score must be between 300 and 850.")
    if (df.loan_amount<=0).any(): raise ValueError("Loan amount must be positive.")
