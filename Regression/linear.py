import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
db=pd.read_csv("C:/AI_python/EDA_START2/Regression_dataset.csv")
print(db)

# Define X and y
X = db[['Hours_Studied']]
y = db['Exam_Score']

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)
# Get the slope (m) and intercept (b)
m = model.coef_[0]
b = model.intercept_

# Print the linear regression formula
print(f"Linear Regression Formula: y = {m:.2f}x + {b:.2f}")

# Predict y values using the model
y_pred = model.predict(X)

# Plot the actual data points
plt.scatter(X, y, color='blue', label='Actual Data')

# Plot the regression line
plt.plot(X, y_pred, color='red', label=f'Regression Line: y = {m:.2f}x + {b:.2f}')

# Add titles and labels for clarity
plt.title('Linear Regression of Exam Score vs. Hours Studied (y=mx+b)')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()