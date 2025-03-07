# Predictive Maintenance Dashboard for Industrial Equipment

This project demonstrates the development of a **Predictive Maintenance Dashboard** using **Amazon QuickSight**, **Python**, and **AWS**. The dashboard provides real-time insights into equipment health, failure predictions, and maintenance recommendations.

## Key Features
- **Interactive Visualizations**:
  - Gauge Chart: Overall machine health (failure rate).
  - Bar Chart: Failure modes by product type (L, M, H).
  - Line Chart: Sensor trends over time (air temperature, process temperature, tool wear).
  - Heatmap: Failure predictions by product type.
  - Table: Maintenance recommendations.
- **Machine Learning Model**:
  - Developed a **Random Forest model** to predict equipment failures.
  - Achieved **99.05% testing accuracy** with high precision (0.96) and recall (0.72) for failure cases.
- **Data Pipeline**:
  - Preprocessed sensor data using **Python** (pandas, scikit-learn).
  - Manually uploaded the dataset to **AWS S3** for integration with QuickSight.

## Tools and Technologies
- **Python**: Data preprocessing, feature engineering, and model training.
- **Amazon QuickSight**: Interactive dashboard with real-time visualizations.
- **AWS S3**: Data storage and integration with QuickSight.
- **Scikit-learn**: Machine learning model development.

## Dashboard Link
[View the Live Dashboard on AWS QuickSight](https://us-east-1.quicksight.aws.amazon.com/sn/dashboards/4274f5ba-a65d-49d2-9c3c-058647ec1dbc/views/b16733f3-e07d-466e-b018-7723ddbcef27?directory_alias=srujan-quicksight)

## Repository Contents
- **Code**: Python scripts for data preprocessing and model training.
- **Dataset**: Cleaned dataset used for the dashboard (`predictions.csv`).
- **Documentation**: README file with project details and setup instructions.

## How to Use
1. Clone the repository.
2. Install the required Python libraries (`pandas`, `scikit-learn`, etc.).
3. Run the preprocessing and model training scripts.
4. Upload the dataset to AWS S3 and connect it to QuickSight.
5. Build the dashboard using the provided visualizations.

## Contributions
Feel free to contribute to this project by opening issues or submitting pull requests. Feedback and suggestions are always welcome!
