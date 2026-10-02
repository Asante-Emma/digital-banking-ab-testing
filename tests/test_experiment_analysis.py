import pandas as pd
import pytest
from src.experiment_analysis import conversion_rate,absolute_lift,relative_lift,two_proportion_z_test,conversion_rate_confidence_interval,difference_confidence_interval,experiment_result

def test_conversion_rate():
    df=pd.DataFrame({"experiment_group":["control","control","treatment","treatment"],"application_completed":[0,1,1,1]}); assert conversion_rate(df,"control")==.5; assert conversion_rate(df,"treatment")==1

def test_lift(): assert absolute_lift(.10,.12)==pytest.approx(.02); assert relative_lift(.10,.12)==pytest.approx(.20)

def test_z_test():
    z,p=two_proportion_z_test(100,1000,180,1000); assert z>0; assert p<.001

def test_ci():
    lo,hi=conversion_rate_confidence_interval(100,1000); assert lo<.10<hi; lo,hi=difference_confidence_interval(100,1000,180,1000); assert lo<.06<hi

def test_experiment_result():
    df=pd.DataFrame({"user_id":[f"U{i}" for i in range(200)],"experiment_group":["control"]*100+["treatment"]*100,"application_completed":[0]*90+[1]*10+[0]*80+[1]*20}); r=experiment_result(df); assert r["control_rate"]==pytest.approx(.10); assert r["treatment_rate"]==pytest.approx(.20); assert r["absolute_lift"]==pytest.approx(.10); assert r["relative_lift"]==pytest.approx(1.0); assert r["p_value"]<.05; assert r["significant_at_alpha_0_05"] is True
