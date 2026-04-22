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




