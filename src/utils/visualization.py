"""
Utility functions for data visualization.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path


# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10


def save_figure(fig, filename, dpi=300):
    """
    Save figure to outputs/figures directory.
    
    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        Figure to save
    filename : str
        Name of the output file
    dpi : int
        Resolution (dots per inch)
    """
    output_dir = Path(__file__).parent.parent.parent / 'outputs' / 'figures'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / filename
    fig.savefig(output_path, dpi=dpi, bbox_inches='tight')
    print(f"Figure saved to: {output_path}")


def plot_distribution(data, column, title=None, bins=30):
    """
    Plot distribution of a numerical column.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input data
    column : str
        Column name to plot
    title : str, optional
        Plot title
    bins : int
        Number of bins for histogram
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Histogram
    axes[0].hist(data[column].dropna(), bins=bins, edgecolor='black', alpha=0.7)
    axes[0].set_xlabel(column)
    axes[0].set_ylabel('Frequency')
    axes[0].set_title(f'Distribution of {column}')
    axes[0].grid(True, alpha=0.3)
    
    # Box plot
    axes[1].boxplot(data[column].dropna())
    axes[1].set_ylabel(column)
    axes[1].set_title(f'Box Plot of {column}')
    axes[1].grid(True, alpha=0.3)
    
    if title:
        fig.suptitle(title, fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig


def plot_correlation_matrix(data, method='pearson', figsize=(10, 8)):
    """
    Plot correlation matrix heatmap.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input data
    method : str
        Correlation method ('pearson', 'kendall', 'spearman')
    figsize : tuple
        Figure size
    """
    corr = data.select_dtypes(include=[np.number]).corr(method=method)
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
    ax.set_title('Correlation Matrix', fontsize=14, fontweight='bold')
    plt.tight_layout()
    return fig


def plot_time_series(data, date_column, value_column, title=None):
    """
    Plot time series data.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input data
    date_column : str
        Name of date column
    value_column : str
        Name of value column to plot
    title : str, optional
        Plot title
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    
    data_sorted = data.sort_values(date_column)
    ax.plot(data_sorted[date_column], data_sorted[value_column], linewidth=2)
    ax.set_xlabel(date_column)
    ax.set_ylabel(value_column)
    ax.set_title(title or f'Time Series: {value_column}')
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


def plot_attrition_by_category(data, category_col, target_col='Attrition', figsize=(10, 6)):
    """
    Plot attrition rate by categorical variable.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input data
    category_col : str
        Categorical column name
    target_col : str
        Target column (default: 'Attrition')
    figsize : tuple
        Figure size
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Calculate attrition rate by category
    attrition_rate = data.groupby(category_col)[target_col].apply(
        lambda x: (x == 'Yes').sum() / len(x) * 100
    ).sort_values(ascending=False)
    
    # Plot
    bars = ax.bar(range(len(attrition_rate)), attrition_rate.values, 
                   color='#e74c3c', alpha=0.7, edgecolor='black')
    ax.set_xticks(range(len(attrition_rate)))
    ax.set_xticklabels(attrition_rate.index, rotation=45, ha='right')
    ax.set_ylabel('Attrition Rate (%)')
    ax.set_title(f'Attrition Rate by {category_col}', fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for i, (bar, val) in enumerate(zip(bars, attrition_rate.values)):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{val:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    return fig
