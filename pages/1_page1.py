import pandas as pd
import streamlit as st 
import plotly.express as px

st.title("Dashboard Analysis")

st.write("""
         Here we have the dashboard analysis of the heart disease dataset. 
         We will explore various visualizations and insights from the data to understand the factors 
         contributing to heart disease.
         """)

# Load the dataset
heart_train_df=pd.read_csv('train.csv')
heart_train_df.drop(columns=['id'], inplace=True)   

heart_train_df['Sex'] = heart_train_df['Sex'].map({0: 'Female', 1: 'Male'})
heart_train_df['Chest pain type'] = heart_train_df['Chest pain type'].map({1: 'Typical Anginia', 2: 'Atypical Anginia', 3: 'Non-Anginal pain', 4: 'Assymptomatic'})
heart_train_df['FBS over 120'] = heart_train_df['FBS over 120'].map({0: 'Less than 120 mgdL', 1: 'Greater than 120 mgdL'})
heart_train_df['EKG results'] = heart_train_df['EKG results'].map({0: 'Normal', 1: 'ST-T wave abnormality', 2: 'Left ventricular hypertrophy'})
heart_train_df['Exercise angina'] = heart_train_df['Exercise angina'].map({0: 'No', 1: 'Yes'})
heart_train_df['Number of vessels fluro'] = heart_train_df['Number of vessels fluro'].map({0: '0', 1: '1', 2: '2', 3: '3'})       
heart_train_df['Thallium'] = heart_train_df['Thallium'].map({3: 'Normal', 6: 'Fixed Defect', 7: 'Reversible Defect'})
# Categorising the slope of ST segment
def slope_of_st_mapping(value):
    if value == 0 or value < 1:
        return 'Upsloping'
    elif value == 1:
        return 'Flat'
    elif value > 1:
        return 'Downsloping'
    else:
        return 'Unknown'
heart_train_df['Slope of ST'] = heart_train_df['Slope of ST'].apply(slope_of_st_mapping)

col1, col2, col3 = st.columns(3)

# Visualizations
fig_1=px.histogram(heart_train_df, x='Age', color='Heart Disease', title='Distribution of Age by Heart Disease Status')
col1.plotly_chart(fig_1, use_container_width=True)

fig2=px.histogram(heart_train_df, x='Sex', color='Heart Disease', title='Distribution of Sex by Heart Disease Status')
col2.plotly_chart(fig2, use_container_width=True)

fig3=px.histogram(heart_train_df, x='BP', color='Heart Disease', title='Distribution of Blood Pressure by Heart Disease Status')
col3.plotly_chart(fig3, use_container_width=True)   

fig4=px.box(heart_train_df, color='Heart Disease', y='Cholesterol', x='Sex', title='Cholesterol Levels by Heart Disease Status')
col1.plotly_chart(fig4, use_container_width=True)

fig5=px.box(heart_train_df, color='Heart Disease', y='Max HR', x='Sex', title='Maximum Heart Rate by Heart Disease Status')
col2.plotly_chart(fig5, use_container_width=True)

fig6=px.box(heart_train_df, color='Heart Disease', y='ST depression', x='Sex', title='ST Depression by Heart Disease Status')
col3.plotly_chart(fig6, use_container_width=True)

fig7=px.violin(heart_train_df, color='Heart Disease', y='Age', x='Sex', title='Age Distribution by Heart Disease Status')
col1.plotly_chart(fig7, use_container_width=True)

fig8=px.pie(heart_train_df, names='Chest pain type', color='Heart Disease', title='Chest Pain Type Distribution by Heart Disease Status')
col2.plotly_chart(fig8, use_container_width=True)

fig9=px.pie(heart_train_df, names='Exercise angina', color='Heart Disease', title='Exercise Induced Angina Distribution by Heart Disease Status')
col3.plotly_chart(fig9, use_container_width=True)

fig10=px.density_heatmap(heart_train_df, x='Age', y='Cholesterol', facet_row='Heart Disease', facet_col='Sex', text_auto=True, title='Age vs Cholesterol Density by Heart Disease Status')
st.plotly_chart(fig10, use_container_width=True)

fig11=px.density_heatmap(heart_train_df, x='Age', y='Max HR', facet_row='Heart Disease', facet_col='Sex', text_auto=True, title='Age vs Max Heart Rate Density by Heart Disease Status')
st.plotly_chart(fig11, use_container_width=True)

fig12=px.density_heatmap(heart_train_df, x='Age', y='ST depression', facet_row='Heart Disease', facet_col='Sex', text_auto=True, title='Age vs ST Depression Density by Heart Disease Status')
st.plotly_chart(fig12, use_container_width=True)

fig13=px.density_heatmap(heart_train_df, x='Cholesterol', y='Max HR', facet_row='Heart Disease', facet_col='Sex', text_auto=True, title='Cholesterol vs Max Heart Rate Density by Heart Disease Status')
st.plotly_chart(fig13, use_container_width=True)




