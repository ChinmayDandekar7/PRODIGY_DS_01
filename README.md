Task 1: Data Visualization - Bar Plot of Categorical Variables



Overview :

This task was part of my Data Science internship at Prodigy InfoTech, where I focused on visualizing categorical variables in a dataset using bar plots. The goal was to practice data visualization techniques and gain insights into the distribution of different categories within specific columns.



Objective :

The main objective of this task was to
Load and inspect the dataset to ensure it was ready for analysis.
Identify and handle missing values in categorical columns.
Visualize the distribution of categorical variables ('Sex', 'Embarked', 'Pclass') using bar plots to understand their frequency distribution.



Key Features of the Code:

Data Loading: The dataset was loaded into a Pandas DataFrame using pd.read_csv().
Data Inspection: Initial inspection was done to check for the existence of specified columns and handle missing values with dropna().
Visualization: Bar plots were created using the ggplot package from plotnine to represent the distribution of categorical columns in the dataset.
Plot Customization: Custom color palettes were used, and the plots were enhanced with labels, titles, and rotated x-axis labels for better readability.
Plot Display: The plot was saved to an in-memory buffer and displayed using Matplotlib, allowing seamless image handling without saving to disk.



Learning Outcomes :

Understanding how to inspect and clean categorical data by handling missing values.
Visualizing categorical columns using bar plots to observe the distribution of categories.
Gaining proficiency with Python libraries such as Pandas, Plotnine, Seaborn (for color palettes), and Matplotlib.
Learning to manage in-memory plotting and figure display using io for efficient visualization workflows.



Tools & Technologies :

Python (Version 3.x): The programming language used for the task.
Pandas: For data handling and preprocessing.
Plotnine: For creating bar plots and customizing them.
Matplotlib: For displaying the images created by Plotnine.
Seaborn: For generating color palettes based on the number of unique categories.



Sample Output :

The bar plots generated from the categorical columns ('Sex', 'Embarked', 'Pclass') provided a clear view of the distribution of these categories, helping identify patterns and trends in the data.
