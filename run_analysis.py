from pathlib import Path
from src.data_preparation import load_data,validate_data,quality_report
from src.experiment_analysis import experiment_result,group_summary,segment_conversion
from src.visualization import plot_conversion_rates,plot_segment_rates
ROOT=Path(__file__).resolve().parent; DATA=ROOT/"data"/"digital_banking_ab_testing_synthetic_dataset.csv"; OUT=ROOT/"reports"/"figures"

def main():
    df=load_data(DATA); print("=== DATA QUALITY ==="); [print(f"{k}: {v}") for k,v in quality_report(df).items()]; validate_data(df); print("\nData validation: PASSED")
    print("\n=== GROUP SUMMARY ==="); print(group_summary(df).to_string(index=False)); r=experiment_result(df)
    print("\n=== PRIMARY A/B TEST ==="); print(f"Control conversion rate:   {r['control_rate']:.2%}"); print(f"Treatment conversion rate: {r['treatment_rate']:.2%}"); print(f"Absolute lift:             {r['absolute_lift']:.2%}"); print(f"Relative lift:             {r['relative_lift']:.2%}"); print(f"Z-statistic:               {r['z_statistic']:.4f}"); print(f"P-value:                   {r['p_value']:.6g}"); print(f"95% CI treatment-control:  [{r['difference_ci'][0]:.2%}, {r['difference_ci'][1]:.2%}]"); print(f"Significant at alpha=0.05: {r['significant_at_alpha_0_05']}")
    print("\n=== SEGMENT CHECK: DEVICE ==="); print(segment_conversion(df,"device_type").to_string(index=False)); plot_conversion_rates(df,OUT/"conversion_rates.png"); plot_segment_rates(df,"device_type",OUT/"conversion_by_device.png"); print(f"\nCharts saved to: {OUT}")
if __name__=="__main__": main()
