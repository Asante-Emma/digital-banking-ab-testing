"""Statistical analysis functions."""
import numpy as np
import pandas as pd
from scipy.stats import norm

def group_summary(df):
    return df.groupby("experiment_group").agg(users=("user_id","count"),completed=("application_completed","sum"),completion_rate=("application_completed","mean"),approved=("loan_approved","sum"),approval_rate=("loan_approved","mean"),avg_completion_time=("application_time_minutes","mean")).reset_index()

def conversion_rate(df,group):
    x=df.loc[df.experiment_group==group,"application_completed"]
    if len(x)==0: raise ValueError(f"No observations found for group: {group}")
    return float(x.mean())

def absolute_lift(control_rate,treatment_rate): return treatment_rate-control_rate

def relative_lift(control_rate,treatment_rate):
    if control_rate==0: raise ValueError("Control rate cannot be zero.")
    return (treatment_rate-control_rate)/control_rate

def two_proportion_z_test(control_successes,control_total,treatment_successes,treatment_total):
    if min(control_total,treatment_total)<=0: raise ValueError("Group sizes must be positive.")
    pc=control_successes/control_total; pt=treatment_successes/treatment_total; pooled=(control_successes+treatment_successes)/(control_total+treatment_total)
    se=np.sqrt(pooled*(1-pooled)*(1/control_total+1/treatment_total))
    if se==0: return 0.0,1.0
    z=(pt-pc)/se; return float(z),float(2*norm.sf(abs(z)))

def conversion_rate_confidence_interval(successes,total,confidence=.95):
    if total<=0: raise ValueError("Total must be positive.")
    p=successes/total; z=norm.ppf(1-(1-confidence)/2); se=np.sqrt(p*(1-p)/total); m=z*se
    return max(0,p-m),min(1,p+m)

def difference_confidence_interval(control_successes,control_total,treatment_successes,treatment_total,confidence=.95):
    pc=control_successes/control_total; pt=treatment_successes/treatment_total; z=norm.ppf(1-(1-confidence)/2)
    se=np.sqrt(pc*(1-pc)/control_total+pt*(1-pt)/treatment_total); d=pt-pc; m=z*se
    return d-m,d+m

def experiment_result(df,confidence=.95):
    c=df[df.experiment_group=="control"]; t=df[df.experiment_group=="treatment"]
    ct,tt=len(c),len(t); cs,ts=int(c.application_completed.sum()),int(t.application_completed.sum()); cr, tr=cs/ct,ts/tt
    z,p=two_proportion_z_test(cs,ct,ts,tt); diff=tr-cr
    return {"control_users":ct,"treatment_users":tt,"control_completed":cs,"treatment_completed":ts,"control_rate":cr,"treatment_rate":tr,"absolute_lift":diff,"relative_lift":relative_lift(cr,tr),"z_statistic":z,"p_value":p,"control_ci":conversion_rate_confidence_interval(cs,ct,confidence),"treatment_ci":conversion_rate_confidence_interval(ts,tt,confidence),"difference_ci":difference_confidence_interval(cs,ct,ts,tt,confidence),"significant_at_alpha_0_05":p<.05}

def segment_conversion(df,segment):
    return df.groupby([segment,"experiment_group"]).agg(users=("user_id","count"),completed=("application_completed","sum"),conversion_rate=("application_completed","mean")).reset_index()
