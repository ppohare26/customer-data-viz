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
https://github.com/ppohare26/customer-data-viz.git
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

<img width="1467" alt="Screenshot 2025-04-25 at 12 55 56 AM" src="https://github.com/user-attachments/assets/347bb76e-ca64-4816-8b4e-bec67104cdff" />

<ul>Use the file uploader on the sidebar to upload your CSV file.</ul>

<ul>Supported file types: .csv.</ul>

Data Cleaning Options:

<ul>On the sidebar, there are options to clean missing values (fill with mean for continuous and mode for categorical) and remove duplicate rows.</ul>

<ul>You can enable or disable these options as needed.</ul>

Tabs:

<img width="1464" alt="Screenshot 2025-04-25 at 12 58 00 AM" src="https://github.com/user-attachments/assets/9021c92b-30b4-4ec5-9be2-25b35be67ceb" />

<ul>Overview: View basic information about the dataset, such as the shape of the data, missing values, and types of columns.</ul>

<img width="1443" alt="Screenshot 2025-04-28 at 9 41 15 PM" src="https://github.com/user-attachments/assets/965dcd81-209e-4c91-aac8-160068dedefe" />

<ul>Visualizations: Select the type of visualization you want (bar chart, pie chart, or sales funnel). These charts provide insights into your dataset.</ul>

<img width="1452" alt="Screenshot 2025-04-28 at 9 42 28 PM" src="https://github.com/user-attachments/assets/b7c40cf3-6787-4420-bf3c-c2ec4b0d829d" />

<ul>Feature: Select a feature from the dataset and view its distribution using histograms or bar charts.</ul>

<img width="1449" alt="Screenshot 2025-04-28 at 9 42 43 PM" src="https://github.com/user-attachments/assets/c73c294b-8c04-40f5-9745-f85361baf890" />

<ul>Relationships: Explore the relationship between two continuous features with scatter plots.</ul>

Sales Funnel:

<ul>A funnel chart visually represents a process by showing how data changes as it moves through various stages. Below are two examples of the same showing how the first interaction and last activity's data changes in every stage.</ul>
<ul>You can visualize a Sales Funnel for any categorical feature to understand the distribution across different stages.</ul>
<img width="1465" alt="Screenshot 2025-04-25 at 12 58 31 AM" src="https://github.com/user-attachments/assets/93a935be-d91d-40b9-964f-dfafac28fdc6" />

<img width="1087" alt="Screenshot 2025-04-28 at 9 31 42 PM" src="https://github.com/user-attachments/assets/48e2c774-570f-48e8-b63d-14ae9f95b40c" />

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


