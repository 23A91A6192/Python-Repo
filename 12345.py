import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("employee_productivity_dataset_extended.xlsx")

# Display basic info
print("Dataset Overview:\n", df.head())

# Drop missing values and duplicates
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Top 5 employees by performance rating
top_employees = df.nlargest(5, 'PerformanceRating')[['Name', 'Department', 'PerformanceRating']]
print("\nTop 5 Performing Employees:\n", top_employees)

# Bar chart – Top performers
plt.figure(figsize=(8, 4))
plt.bar(top_employees['Name'], top_employees['PerformanceRating'], color='skyblue')
plt.title('Top 5 Performing Employees')
plt.xlabel('Employee Name')
plt.ylabel('Performance Rating')
plt.xticks(rotation=30)
plt.show()

# Department-wise average salary
dept_salary = df.groupby('Department')['Salary'].mean().sort_values(ascending=False)
print("\nAverage Salary by Department:\n", dept_salary)




plt.figure(figsize=(8, 4))
dept_salary.plot(kind='bar', color='lightgreen')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.show()

# Project-wise performance trend
proj_perf = df.groupby('CurrentProject')['PerformanceRating'].mean()
plt.figure(figsize=(7, 4))
plt.plot(proj_perf.index, proj_perf.values, marker='o', color='orange')
plt.title('Average Performance Rating by Project')
plt.xlabel('Current Project')
plt.ylabel('Average Rating')
plt.show()

# Education Level Distribution
edu_dist = df['EducationLevel'].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(edu_dist, labels=edu_dist.index, autopct='%1.1f%%', startangle=140)
plt.title('Employee Distribution by Education Level')
plt.show()

