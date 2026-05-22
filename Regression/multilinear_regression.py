import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
db=pd.read_csv("C:/AI_python/EDA_START2/Regression_dataset.csv")
print(db)

# Define multiple independent variables (X_multi) and the dependent variable (y)
X_multi = db[['Hours_Studied', 'Attendance (%)', 'Previous_Score']]
y = db['Exam_Score']

# Create and fit the multilinear regression model
multi_model = LinearRegression()
multi_model.fit(X_multi, y)

# Get the coefficients (m) and intercept (b)
multi_m = multi_model.coef_
multi_b = multi_model.intercept_

# Print the multilinear regression formula
print(f"Multilinear Regression Formula: y = {multi_b:.2f} + ", end="")
for i, feature in enumerate(X_multi.columns):
    print(f"{multi_m[i]:.2f}*{feature}", end=" ")
print("\n")

# Predict y values using the model for a sample student
# Let's say a student studied 5 hours, had 75% attendance, and a previous score of 65.
new_student_data = pd.DataFrame([{'Hours_Studied': 5, 'Attendance (%)': 75, 'Previous_Score': 65}])
predicted_score_multi = multi_model.predict(new_student_data)

print(f"For a student with {new_student_data['Hours_Studied'].iloc[0]} hours studied, ")
print(f"{new_student_data['Attendance (%)'].iloc[0]}% attendance, and ")
print(f"{new_student_data['Previous_Score'].iloc[0]} previous score,")
print(f"the predicted exam score is: {predicted_score_multi[0]:.2f}")