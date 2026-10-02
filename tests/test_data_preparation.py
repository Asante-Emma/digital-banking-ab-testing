import pandas as pd
import pytest
from src.data_preparation import validate_data,validate_schema
def valid_df():
    return pd.DataFrame({"user_id":["U1","U2"],"experiment_group":["control","treatment"],"age":[30,40],"gender":["Female","Male"],"income":[40000,50000],"employment_status":["Employed","Self-employed"],"credit_score":[680,720],"loan_amount":[5000,8000],"loan_term_months":[24,36],"application_started":[1,1],"application_completed":[0,1],"application_time_minutes":[0.0,5.0],"application_date":pd.to_datetime(["2026-08-01","2026-08-02"]),"device_type":["Mobile","Web"],"previous_customer":[0,1],"loan_approved":[0,1]})
def test_schema_passes(): validate_schema(valid_df())
def test_completed_without_start_fails():
    df=valid_df(); df.loc[0,"application_completed"]=1; df.loc[0,"application_started"]=0
    with pytest.raises(ValueError,match="completed application"): validate_data(df)
def test_invalid_group_fails():
    df=valid_df(); df.loc[0,"experiment_group"]="other"
    with pytest.raises(ValueError,match="Unexpected experiment group"): validate_schema(df)
