"""
Report generation utilities for the Business Analytics project.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import json


def generate_summary_report(df, output_path=None):
    """
    Generate a comprehensive summary report of the analysis.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    output_path : str or Path, optional
        Path to save the report. If None, saves to outputs/reports/
    """
    if output_path is None:
        output_dir = Path(__file__).parent.parent.parent / 'outputs' / 'reports'
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = output_dir / f'summary_report_{timestamp}.txt'
    else:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
    
    report_lines = []
    report_lines.append("=" * 80)
    report_lines.append("EMPLOYEE ATTRITION ANALYSIS - SUMMARY REPORT")
    report_lines.append("=" * 80)
    report_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("")
    
    # Dataset Overview
    report_lines.append("DATASET OVERVIEW")
    report_lines.append("-" * 80)
    report_lines.append(f"Total Employees: {len(df):,}")
    report_lines.append(f"Total Features: {len(df.columns)}")
    report_lines.append("")
    
    # Attrition Overview
    if 'Attrition' in df.columns:
        attrition_counts = df['Attrition'].value_counts()
        attrition_pct = df['Attrition'].value_counts(normalize=True) * 100
        
        report_lines.append("ATTRITION OVERVIEW")
        report_lines.append("-" * 80)
        for val, count in attrition_counts.items():
            report_lines.append(f"  {val}: {count:,} ({attrition_pct[val]:.2f}%)")
        report_lines.append("")
    
    # Key Statistics
    report_lines.append("KEY STATISTICS")
    report_lines.append("-" * 80)
    
    key_metrics = ['Age', 'MonthlyIncome', 'YearsAtCompany', 'JobSatisfaction', 
                   'WorkLifeBalance', 'StressRating', 'PerformanceIndex']
    
    for metric in key_metrics:
        if metric in df.columns:
            if df[metric].dtype in [np.int64, np.float64]:
                report_lines.append(f"\n{metric}:")
                report_lines.append(f"  Mean: {df[metric].mean():.2f}")
                report_lines.append(f"  Median: {df[metric].median():.2f}")
                report_lines.append(f"  Std Dev: {df[metric].std():.2f}")
                report_lines.append(f"  Min: {df[metric].min():.2f}")
                report_lines.append(f"  Max: {df[metric].max():.2f}")
    
    # Department Distribution
    if 'Department' in df.columns:
        report_lines.append("\nDEPARTMENT DISTRIBUTION")
        report_lines.append("-" * 80)
        dept_counts = df['Department'].value_counts()
        for dept, count in dept_counts.items():
            pct = (count / len(df)) * 100
            report_lines.append(f"  {dept}: {count:,} ({pct:.2f}%)")
    
    # Job Role Distribution
    if 'JobRole' in df.columns:
        report_lines.append("\nTOP 10 JOB ROLES")
        report_lines.append("-" * 80)
        job_counts = df['JobRole'].value_counts().head(10)
        for job, count in job_counts.items():
            pct = (count / len(df)) * 100
            report_lines.append(f"  {job}: {count:,} ({pct:.2f}%)")
    
    # Attrition by Key Factors
    if 'Attrition' in df.columns:
        report_lines.append("\nATTRITION RATES BY KEY FACTORS")
        report_lines.append("-" * 80)
        
        factors = ['Department', 'Gender', 'MaritalStatus', 'OverTime', 'BusinessTravel']
        for factor in factors:
            if factor in df.columns:
                factor_attrition = df.groupby(factor)['Attrition'].apply(
                    lambda x: (x == 'Yes').sum() / len(x) * 100
                ).sort_values(ascending=False)
                
                report_lines.append(f"\n{factor}:")
                for val, rate in factor_attrition.items():
                    report_lines.append(f"  {val}: {rate:.2f}%")
    
    # Income Analysis
    if 'MonthlyIncome' in df.columns and 'Attrition' in df.columns:
        report_lines.append("\nINCOME ANALYSIS")
        report_lines.append("-" * 80)
        income_yes = df[df['Attrition'] == 'Yes']['MonthlyIncome'].mean()
        income_no = df[df['Attrition'] == 'No']['MonthlyIncome'].mean()
        report_lines.append(f"Average Monthly Income (Left): ${income_yes:,.2f}")
        report_lines.append(f"Average Monthly Income (Stayed): ${income_no:,.2f}")
        report_lines.append(f"Income Difference: ${income_no - income_yes:,.2f}")
    
    report_lines.append("\n" + "=" * 80)
    report_lines.append("END OF REPORT")
    report_lines.append("=" * 80)
    
    # Write report to file
    report_text = "\n".join(report_lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report_text)
    
    print(f"Summary report saved to: {output_path}")
    return output_path


def generate_insights_json(df, output_path=None):
    """
    Generate insights as JSON file.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    output_path : str or Path, optional
        Path to save the JSON file
    """
    if output_path is None:
        output_dir = Path(__file__).parent.parent.parent / 'outputs' / 'reports'
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = output_dir / f'insights_{timestamp}.json'
    else:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
    
    insights = {
        'generated_at': datetime.now().isoformat(),
        'dataset_info': {
            'total_employees': int(len(df)),
            'total_features': int(len(df.columns))
        }
    }
    
    if 'Attrition' in df.columns:
        insights['attrition'] = {
            'overall_rate': float((df['Attrition'] == 'Yes').sum() / len(df) * 100),
            'counts': df['Attrition'].value_counts().to_dict()
        }
    
    # Key metrics
    key_metrics = ['Age', 'MonthlyIncome', 'YearsAtCompany', 'JobSatisfaction', 
                   'WorkLifeBalance', 'StressRating']
    insights['key_metrics'] = {}
    for metric in key_metrics:
        if metric in df.columns:
            insights['key_metrics'][metric] = {
                'mean': float(df[metric].mean()),
                'median': float(df[metric].median()),
                'std': float(df[metric].std())
            }
    
    # Attrition by factors
    if 'Attrition' in df.columns:
        insights['attrition_by_factors'] = {}
        factors = ['Department', 'Gender', 'MaritalStatus', 'OverTime']
        for factor in factors:
            if factor in df.columns:
                factor_attrition = df.groupby(factor)['Attrition'].apply(
                    lambda x: (x == 'Yes').sum() / len(x) * 100
                ).to_dict()
                insights['attrition_by_factors'][factor] = factor_attrition
    
    # Save JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(insights, f, indent=2, ensure_ascii=False)
    
    print(f"Insights JSON saved to: {output_path}")
    return output_path

