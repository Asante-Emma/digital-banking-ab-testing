"""Visualization helpers."""
from pathlib import Path
import matplotlib.pyplot as plt

def plot_conversion_rates(df,output_path):
    s=df.groupby("experiment_group").application_completed.mean().reindex(["control","treatment"]); fig,ax=plt.subplots(figsize=(7,5)); ax.bar(s.index,s.values); ax.set_title("Loan Application Completion Rate"); ax.set_ylabel("Completion rate"); ax.set_ylim(0,max(s.values)*1.25); ax.yaxis.set_major_formatter(lambda x,pos:f"{x:.0%}"); fig.tight_layout(); Path(output_path).parent.mkdir(parents=True,exist_ok=True); fig.savefig(output_path,dpi=150); plt.close(fig)

def plot_segment_rates(df,segment,output_path):
    s=df.groupby([segment,"experiment_group"]).application_completed.mean().unstack().reindex(columns=["control","treatment"]); ax=s.plot(kind="bar",figsize=(9,5)); ax.set_title(f"Completion Rate by {segment}"); ax.set_ylabel("Completion rate"); ax.set_xlabel(segment); ax.yaxis.set_major_formatter(lambda x,pos:f"{x:.0%}"); fig=ax.get_figure(); fig.tight_layout(); Path(output_path).parent.mkdir(parents=True,exist_ok=True); fig.savefig(output_path,dpi=150); plt.close(fig)
