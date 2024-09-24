# README: Seoul Bike Prediction Model

## Overview
This project aims to predict the number of bikes rented per hour in Seoul using various weather-related features. The model is built using **Stochastic Gradient Descent (SGD)** regression, and the dataset is preprocessed and standardized to improve model accuracy.

## Libraries Used
Ensure the following libraries are available in your environment (all of which are pre-installed in Google Colab):
- **Pandas**: Data manipulation and preprocessing.
- **NumPy**: Numerical operations and handling arrays.
- **Scikit-learn**: Machine learning tools (used for model training, scaling, and evaluation).
- **Seaborn**: Data visualization (used for plotting correlation heatmap and pair plots).
- **Matplotlib**: General plotting library for visualizations.

### Installation (if running locally):
If you are running this code outside Google Colab, you will need to install the following libraries:
```bash
pip install pandas numpy scikit-learn seaborn matplotlib
```

## How to Build and Run the Code on Google Colab

### Upload the Notebook:
1. Go to [Google Colab](https://colab.research.google.com/).
2. Click on **File > Upload Notebook**.
3. Upload the `4375_asgmt1.ipynb` file.

### Set Up the Environment:
- All required libraries are already installed in Google Colab. No further setup is needed for libraries.
- Ensure you have an internet connection to download the dataset from the GitHub URL.

### Running the Notebook:
1. Open the notebook in Google Colab.
2. Run the cells sequentially by pressing the "Play" button to the left of each cell, or press `Shift + Enter` to execute each cell.
3. The dataset will be loaded via this code block:
   ```python
   url = 'https://github.com/pedigonatalie/Seoul-Bike-Data/raw/main/SeoulBikeData.csv'
   data = pd.read_csv(url, encoding='latin1')
   ```
## Model Training:
- The model will be trained using the SGDRegressor with optimal hyperparameters found using GridSearchCV.
- The training and test results (Mean Squared Error, R-squared values, etc.) will be displayed after the model is evaluated.
## Final Output:
- Residuals are plotted, and evaluation metrics are printed. You can see how well the model performed on both the training and testing datasets.
## Troubleshooting:
- If you encounter any issues with running the notebook on Google Colab, ensure that the dataset URL is correct and that you have run all cells in the correct order.
- The code relies on an internet connection to fetch the dataset, so make sure you are connected online.
