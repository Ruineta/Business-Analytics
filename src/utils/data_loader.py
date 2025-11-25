"""
Utility functions for loading and preprocessing data.
"""
import pandas as pd
import numpy as np
from pathlib import Path
import os


def load_data(file_path, file_type=None):
    """
    Load data from various file formats.
    
    Parameters:
    -----------
    file_path : str or Path
        Path to the data file
    file_type : str, optional
        Type of file ('csv', 'excel', 'json', 'parquet')
        If None, will infer from file extension
    
    Returns:
    --------
    pd.DataFrame
        Loaded data as pandas DataFrame
    """
    file_path = Path(file_path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Infer file type from extension if not provided
    if file_type is None:
        ext = file_path.suffix.lower()
        if ext == '.csv':
            file_type = 'csv'
        elif ext in ['.xlsx', '.xls']:
            file_type = 'excel'
        elif ext == '.json':
            file_type = 'json'
        elif ext == '.parquet':
            file_type = 'parquet'
        else:
            raise ValueError(f"Unsupported file type: {ext}")
    
    # Load based on file type
    if file_type == 'csv':
        return pd.read_csv(file_path)
    elif file_type == 'excel':
        return pd.read_excel(file_path)
    elif file_type == 'json':
        return pd.read_json(file_path)
    elif file_type == 'parquet':
        return pd.read_parquet(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")


def get_project_root():
    """Get the project root directory."""
    return Path(__file__).parent.parent.parent


def get_data_path(file_name=None, subfolder='raw'):
    """
    Get path to data directory or specific data file.
    
    Parameters:
    -----------
    file_name : str, optional
        Name of the data file
    subfolder : str
        Subfolder in data directory ('raw' or 'processed')
    
    Returns:
    --------
    Path
        Path to data directory or file
    """
    root = get_project_root()
    data_path = root / 'data' / subfolder
    
    if file_name:
        return data_path / file_name
    return data_path


def save_processed_data(df, file_name, subfolder='processed'):
    """
    Save processed data to file.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to save
    file_name : str
        Name of the output file
    subfolder : str
        Subfolder in data directory ('processed')
    """
    output_path = get_data_path(file_name, subfolder)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    ext = output_path.suffix.lower()
    if ext == '.csv':
        df.to_csv(output_path, index=False)
    elif ext in ['.xlsx', '.xls']:
        df.to_excel(output_path, index=False)
    elif ext == '.parquet':
        df.to_parquet(output_path, index=False)
    else:
        # Default to CSV
        output_path = output_path.with_suffix('.csv')
        df.to_csv(output_path, index=False)
    
    print(f"Data saved to: {output_path}")

