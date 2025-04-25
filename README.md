# customer-data-viz

# 📊 Data Explorer Dashboard

This interactive data exploration and visualization dashboard allows you to upload a CSV file, clean the data, and visualize various insights with customizable charts. You can perform data wrangling, handle missing values, remove duplicates, and explore relationships between features through visualizations like histograms, bar charts, pie charts, and sales funnel charts.

## Features:
1. **Upload Dataset**: Users can upload a CSV file for analysis.
2. **Data Cleaning**:
   - Handle missing values by filling them with mean (for continuous columns) or mode (for categorical columns).
   - Remove duplicate rows.
3. **Interactive Visualizations**:
   - **Overview**: Quick summary of the dataset including the number of rows, columns, continuous and categorical columns, and missing values.
   - **Visual Explorations**: Users can select the type of visualization to generate:
     - Bar Chart
     - Pie Chart
     - Sales Funnel
   - **Feature Analysis**: Select a feature to analyze and visualize its distribution (using histograms or bar charts).
   - **Relationships**: Explore relationships between two continuous features via scatter plots.

## Installation

To run the dashboard locally, follow these steps:

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/data-explorer-dashboard.git
```
### 2. Navigate to the project folder:
```bash
cd data-explorer-dashboard
```
### 3. Install the dependencies:
```bash
pip install -r requirements.txt
```
### 4. Run the Streamlit app:
```bash
streamlit run app.py
```

## Usage
Upload CSV File:

<ul>Use the file uploader on the sidebar to upload your CSV file.</ul>

<ul>Supported file types: .csv.</ul>

Data Cleaning Options:

<ul>On the sidebar, there are options to clean missing values (fill with mean for continuous and mode for categorical) and remove duplicate rows.</ul>

<ul>You can enable or disable these options as needed.</ul>

Tabs:

<ul>Overview: View basic information about the dataset, such as the shape of the data, missing values, and types of columns.</ul>

<ul>Visualizations: Select the type of visualization you want (bar chart, pie chart, or sales funnel). These charts provide insights into your dataset.</ul>

<ul>Feature: Select a feature from the dataset and view its distribution using histograms or bar charts.</ul>

<ul>Relationships: Explore the relationship between two continuous features with scatter plots.</ul>

Sales Funnel:

<ul>You can visualize a Sales Funnel for any categorical feature to understand the distribution across different stages.</ul>

## Requirements
The following libraries are required to run this project:

<li>Streamlit: For building the dashboard UI.</li>

<li>Plotly: For creating interactive charts.</li>

<li>Pandas: For data manipulation.</li>

<li>Seaborn: For advanced statistical plotting (optional).</li>

<li>Matplotlib: For basic plotting (optional).</li>

<li>Missingno: For visualizing missing data.</li>

### To install all dependencies, use the following command:
```bash
pip install -r requirements.txt
```

## File Structure
```bash
data-explorer-dashboard/
│
├── app.py              # Main app script with Streamlit UI.
├── data_cleaning.py    # Code for data wrangling and cleaning.
├── visualizations.py   # Code for visualizations like bar charts, pie charts, etc.
├── requirements.txt    # List of required Python libraries.
└── README.md           # Project documentation.
```

## Code Structure
<li> app.py: Main entry point for the Streamlit app. This script initializes the dashboard layout, handles user inputs, and integrates with the data processing functions.</li>

<li>data_cleaning.py: Contains functions for cleaning the dataset, such as handling missing values and removing duplicates.</li>

<li>visualizations.py: Contains the logic for creating various visualizations (e.g., bar charts, pie charts, sales funnels, scatter plots).</li>

## Customization
<li>Modify Visualizations: You can adjust the types of visualizations or add new ones depending on your needs. The app is flexible and can be extended with new chart types (e.g., line charts, heatmaps).</li>

<li>Adjust Data Wrangling: If needed, you can customize how missing values are handled or implement additional data cleaning steps.</li>
