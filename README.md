# Business Analytics Project

A comprehensive data analytics project for business insights and decision-making.

## 📁 Project Structure

```
Business-Analytics/
├── data/
│   ├── raw/              # Original, unprocessed data files
│   │   └── data.csv      # Employee dataset
│   └── processed/        # Cleaned and processed data files
│       └── cleaned_data.csv
├── notebooks/            # Jupyter notebooks for analysis
│   ├── 01_data_exploration.ipynb      # Initial data exploration and cleaning
│   ├── 02_visualizations.ipynb        # Comprehensive visualizations
│   ├── 03_statistical_analysis.ipynb  # Statistical tests and analysis
│   └── 04_generate_report.ipynb       # Report generation
├── src/
│   └── utils/           # Utility functions and helper modules
│       ├── __init__.py
│       ├── data_loader.py          # Data loading utilities
│       ├── visualization.py        # Visualization functions
│       └── report_generator.py     # Report generation utilities
├── outputs/
│   ├── figures/         # Generated visualizations and charts
│   └── reports/         # Analysis reports and presentations
├── docs/                # Documentation and reference materials
├── requirements.txt     # Python dependencies
├── setup.py            # Package setup file
└── README.md           # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd Business-Analytics
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Dataset is already included:**
   - The dataset (`data.csv`) is located in `data/raw/`
   - If you need additional documentation, download from: https://drive.google.com/drive/folders/1YY5fToNo_gsnFTAN6rlqxs0lrnYZ5_oW
   - Place any additional files in the `docs/` folder

## 📊 Usage

### Running the Analysis Notebooks

1. **Start Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```
   Or use JupyterLab:
   ```bash
   jupyter lab
   ```

2. **Run notebooks in order:**
   
   **Notebook 1: Data Exploration** (`01_data_exploration.ipynb`)
   - Load and inspect the dataset
   - Perform initial data exploration
   - Data cleaning and preprocessing
   - Generate cleaned dataset
   
   **Notebook 2: Visualizations** (`02_visualizations.ipynb`)
   - Comprehensive visualizations of attrition patterns
   - Demographic analysis
   - Job-related factors analysis
   - Satisfaction and work-life balance metrics
   - Income and compensation analysis
   - Stress and performance metrics
   
   **Notebook 3: Statistical Analysis** (`03_statistical_analysis.ipynb`)
   - Chi-square tests for categorical variables
   - T-tests for numerical variables
   - Correlation analysis
   - Identification of significant factors
   
   **Notebook 4: Report Generation** (`04_generate_report.ipynb`)
   - Generate summary reports
   - Export insights as JSON

### Using Utility Functions

The project includes utility functions for common tasks:

```python
from src.utils import load_data, get_data_path, plot_distribution

# Load data
data_path = get_data_path('your_file.csv', subfolder='raw')
df = load_data(data_path)

# Create visualizations
fig = plot_distribution(df, 'column_name')
```

## 📝 Project Workflow

1. **Data Collection**: Dataset is already in `data/raw/data.csv`
2. **Data Exploration**: Run `notebooks/01_data_exploration.ipynb` to explore and clean the data
3. **Visualization**: Run `notebooks/02_visualizations.ipynb` to create comprehensive visualizations
4. **Statistical Analysis**: Run `notebooks/03_statistical_analysis.ipynb` for hypothesis testing
5. **Report Generation**: Run `notebooks/04_generate_report.ipynb` to generate final reports
6. **Review Outputs**: Check `outputs/figures/` for visualizations and `outputs/reports/` for reports

## 🛠️ Customization

### Adding New Analysis Notebooks

Create new notebooks in the `notebooks/` directory following the naming convention:
- `02_analysis_name.ipynb`
- `03_another_analysis.ipynb`

### Extending Utility Functions

Add new utility functions to `src/utils/` and import them in `src/utils/__init__.py`

## 📚 Key Features

### Dataset Information
- **Dataset**: Employee Attrition Data
- **Records**: 1,470 employees
- **Features**: 44 variables including demographics, job details, satisfaction scores, and performance metrics
- **Target Variable**: Attrition (Yes/No)

### Analysis Capabilities
- **Data Loading**: Support for CSV, Excel, JSON, and Parquet files
- **Visualization**: Comprehensive plotting functions for HR analytics
- **Statistical Analysis**: Chi-square tests, t-tests, correlation analysis
- **Data Processing**: Utilities for data cleaning and transformation
- **Report Generation**: Automated report and insights generation
- **Project Organization**: Clean structure for managing data science projects

### Key Insights Areas
- Attrition patterns and rates
- Demographic factors affecting attrition
- Job-related factors (role, department, travel, overtime)
- Satisfaction metrics (job, environment, relationship, work-life balance)
- Income and compensation analysis
- Stress and performance metrics

## 📖 Documentation

Refer to the following documents in the `docs/` folder:
- `Company I Dataset Overview.docx` - Dataset description and schema
- `final_assignment_tutorial.pdf` - Assignment instructions and requirements
- `README.docx` - Additional project documentation

## 🤝 Contributing

1. Follow the project structure
2. Document your code
3. Use meaningful variable and function names
4. Save outputs to appropriate directories

## 📄 License

[Add your license information here]

## 🆘 Troubleshooting

### Common Issues

1. **Import errors**: Make sure you've installed all requirements and activated your virtual environment
2. **File not found**: Verify that data files are in the correct `data/raw/` directory
3. **Jupyter not found**: Install Jupyter using `pip install jupyter`

### Getting Help

- Check the documentation in the `docs/` folder
- Review the tutorial PDF for assignment-specific guidance
- Refer to sample slides for presentation ideas

---

## 🎯 Project Objectives

This project analyzes employee attrition data to:
1. Identify key factors contributing to employee turnover
2. Understand demographic and job-related patterns
3. Analyze satisfaction and work-life balance impacts
4. Examine compensation and performance relationships
5. Provide actionable insights for HR decision-making

## 📈 Expected Outputs

After running all notebooks, you will have:
- Cleaned and processed dataset in `data/processed/`
- Multiple visualization figures in `outputs/figures/`
- Statistical analysis results
- Summary reports in `outputs/reports/`
- Insights JSON file with key metrics

## 🔍 Quick Start Example

```python
from src.utils import load_data, get_data_path, generate_summary_report

# Load data
data_path = get_data_path('data.csv', subfolder='raw')
df = load_data(data_path)

# Generate report
generate_summary_report(df)
```

---

**Note**: The dataset is already included in the project. If you need additional documentation from Google Drive, download and place files in the `docs/` folder.
