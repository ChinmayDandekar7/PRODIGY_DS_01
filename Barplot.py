import pandas as pd
from plotnine import (
    ggplot, aes, geom_bar, theme_minimal, labs, theme, element_text, 
    scale_fill_manual, geom_text
)
import io
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\hp\OneDrive\Desktop\new projewct prodigy_01\test.csv')

def plot_categorical(df, column_name):
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame")
    
    # Drop missing values
    df = df.dropna(subset=[column_name])
    
    # Create a bar plot
    bar_plot = (ggplot(df, aes(x=column_name, fill=column_name)) +
                geom_bar(show_legend=False) +
                geom_text(aes(label='..count..'), stat='count', va='bottom', format_string='{:.0f}') +
                scale_fill_manual(values=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']) +
                theme_minimal() +
                labs(
                    title=f'Bar Plot of {column_name}', 
                    x=column_name, 
                    y='Count',
                    subtitle=f'Distribution of {column_name}',
                    caption='Source: Your Dataset'
                ) +
                theme(
                    figure_size=(10, 6),
                    axis_text_x=element_text(rotation=0, hjust=1, size=12, color='#333333'),
                    axis_text_y=element_text(size=12, color='#333333'),
                    plot_title=element_text(size=16, face='bold', color='#333333'),
                    plot_subtitle=element_text(size=12, color='#555555'),
                    plot_caption=element_text(size=10, color='#555555')
                ))
    
    # Save the plot to a buffer
    bar_plot_buffer = io.BytesIO()
    bar_plot.save(bar_plot_buffer, format='png')
    bar_plot_buffer.seek(0)
    
    # Display the plot using Matplotlib
    plt.imshow(plt.imread(bar_plot_buffer))
    plt.axis('off')  # Hide axes
    plt.show()

# Plot each categorical variable separately
categorical_columns = ['Sex', 'Embarked', 'Pclass']  # Replace with your dataset's categorical columns
for col in categorical_columns:
    plot_categorical(df, col)
