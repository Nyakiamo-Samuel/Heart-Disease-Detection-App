# Creating the app
import pandas as pd
import numpy as np
import pickle
import streamlit as st
import plotly.express as px
from PIL import Image
import joblib
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(page_title='Heart Disease Predictor App',
    page_icon='❤️',
    layout='wide',
    initial_sidebar_state='expanded')

# Insert image on the top of the app
image_1 = Image.open('heart_image.jpg')
st.image(image_1, caption='Heart Image', use_container_width=True)
st.divider()  

# Load pre-trained model
with open('logistic_heart_model.jbl', 'rb') as file:
    app_model = joblib.load(file)

st.title("Heart Disease Prediction App Dashboard")
st.write("## About the App")
st.write("""
         This app predicts the likelihood of heart disease based on user input parameters. 
         """)

st.divider() # Adds a clean horizontal line


# Columns for layout
col1, col2, col3 = st.columns([1, 2, 1])

col1.write('''
         For any assistance or inquiries, turn over to page 2 of the app where you can find more information about heart health, 
         risk factors, and preventive measures. Stay informed and take care of your heart!
         ''')

# 1. Inject CSS to hide the controls and set a custom width
col2.markdown(
    """
    <style>
    /* Target the video element specifically */
    video {
        width: 500px !important; /* Adjust this value to resize */
        height: auto;
        border-radius: 10px;
    }
    
    /* Hide the control bar */
    video::-webkit-media-controls {
        display: none !important;
    }
    video::-webkit-media-controls-enclosure {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. Display the video
col2.video('heart_beat.mp4', start_time=0, loop=True, autoplay=True, muted=True)
# Add caption below the video
col2.caption("""
            Visual representation of a healthy heartbeat. 
             This video is intended to provide a calming and reassuring visual while users interact with the heart disease prediction app.
             It serves as a reminder of the importance of heart health and encourages users to take proactive steps
             """
             )

col3.write("""
            The model is trained on a dataset of heart disease patients and uses various clinical features to make predictions.
            """)

# Add a divider to separate sections
st.divider()

# Columns for layout
col1, col2 = st.columns(2)

with col1:
    # User input form
    st.subheader('Input Parameters')
    # Feature selection on  
    def get_user_input():
        Age=st.selectbox('Age', options=range(25, 81), index=5, key='unique_age_selectbox')
        Blood_Pressure=st.selectbox('BP', options=range(90, 211), index=30, key='unique_bp_selectbox')
        Cholesterol=st.selectbox('Cholesterol', options=range(120, 571), index=80, key='unique_cholesterol_selectbox')
        Max_Heart_Rate=st.selectbox('Max HR', options=range(70, 221), index=110, key='unique_max_hr_selectbox')
        ST_Depression=st.slider('ST Depression', min_value=0.0, max_value=6.5, value=0.0, step=0.1,
                                    key='unique_st_depression_selectbox')
        Sex=st.radio('Sex', ['Female', 'Male'], key='unique_gender_radio')
        Chest_pain_type=st.selectbox('Chest pain type', ['Typical Anginia', 'Atypical Anginia', 'Non-Anginal pain', 'Assymptomatic'], 
        key='unique_chest_pain_type_selectbox')
        FBS_over_120=st.selectbox('FBS over 120', ['Less than 120 mgdL', 'Greater than 120 mgdL'], key='unique_fbs_selectbox')
        EKG_results=st.selectbox('EKG results', ['Normal', 'ST-T abnormality', 'Left ventricular hypertrophy'], key='unique_ekg_selectbox')
        Ecercise_induced_Angina=st.selectbox('Exercise angina', ['No', 'Yes'], key='unique_exercise_angina_selectbox')
        Slope_of_ST=st.selectbox('Slope of ST', ['Upsloping', 'Flat', 'Downsloping'], key='unique_slope_selectbox')
        Number_of_vessels_fluro = st.selectbox('Number of vessels fluro', ['0', '1', '2', '3'], key='unique_vessels_selectbox')
        Thallium=st.selectbox('Thallium', ['Normal', 'Fixed Defect', 'Reversible Defect'], key='unique_thallium_selectbox')
        
        user_data={
            'Age': Age,
            'Sex': Sex,
            'BP': Blood_Pressure, 
            'Cholesterol': Cholesterol, 
            'Max HR': Max_Heart_Rate, 
            'ST depression': ST_Depression,
            'Chest pain type': Chest_pain_type,
            'FBS over 120': FBS_over_120,
            'EKG results': EKG_results, 
            'Exercise angina': Ecercise_induced_Angina, 
            'Slope of ST': Slope_of_ST, 
            'Number of vessels fluro': Number_of_vessels_fluro,
            'Thallium': Thallium 
    }
        
        return pd.DataFrame([user_data])
    
    user_data = get_user_input()


with col2:
    st.subheader('Feature Importance')
    # sort feature importance by absolute value
    feature_importance_df = pd.read_csv('logistic_feature_importance.csv')
    
    # Create interactive plotly bar chart
    fig = px.bar(feature_importance_df, x='Coefficient', y='Feature', orientation='h', 
                 #title='Feature Importance', 
                 labels={'Coefficient': 'Coefficient Value', 'Feature': 'Feature'})
    fig.update_layout(
        xaxis_title='Coefficient Value', 
        yaxis_title='Feature', 
        template='plotly_white',
        height=1100
        )
    st.plotly_chart(fig, use_container_width=True)    

# Feature list for model input
features= ['Age', 'Sex', 'Chest pain type', 'BP', 'Cholesterol', 'FBS over 120', 'EKG results', 
            'Max HR', 'Exercise angina', 'ST depression', 'Slope of ST', 'Number of vessels fluro', 'Thallium']
               
# Transforming the inputs to the required format
def prepare_input(data, feature_list=features):
    # Create a dictionary with all features initialized to 0
    input_data={feature: data.get(feature, 0) for feature in feature_list}
    # Convert the dictionary to a DataFrame
    input_array=np.array([list(input_data.values())])
    return pd.DataFrame(input_array.reshape(1, -1), columns=features)


#with col2:
 #   # Predict button
  #  st.subheader('Heart Disease Prediction') 
   # # Load pre-trained model
    #with open('logistic_heart_model.pkl', 'rb') as file:
     #   app_model = joblib.load(file)
      #  
    #if st.button('Predict Heart Health', use_container_width=True, type="primary"):
     #   with st.spinner('Running predictive intelligence model...'):
      #      # Prepare the input data and make prediction
       #     input_df = prepare_input(user_data, features)
        #    prediction = app_model.predict(input_df)
          #  # Display the prediction result
         #   st.subheader('Prediction of Heart Disease')
           # if prediction[0] == 0:
           #     st.write("No heart disease detected.")
          #  else:
            #    st.write("Heart disease detected.")

    #st.write("Model expects:", app_model.feature_names_in_)
    #st.write("You provided:", input_df.columns.tolist())

st.divider() # Adds a clean horizontal line

# Columns for layout
col1, col2, col3 = st.columns(3)

# Place the prediction button and results in the center column
with col2:
    # Predict button
    st.header('Heart Disease Prediction')
    if st.button('Analyze Heart Health', use_container_width=True, type="primary"):
        with st.spinner('Running predictive intelligence model...'):
            # Prepare and predict
            input_df = prepare_input(user_data, features)
            prediction = app_model.predict(input_df)
            
            # Use a container for the results to group them visually
            with st.container(border=True):
                st.subheader('Result Analysis')
                
                if prediction[0] == 0:
                    st.success("### LOW RISK \nNo significant heart disease indicators detected.")
                else:
                    st.error("### HIGH RISK \nHeart disease indicators detected. Please consult a professional.")
                
                # Optional: Add a probability metric if your model supports it
                proba = app_model.predict_proba(input_df)[0][1]
                st.metric(label="Risk Probability", value=f"{round(proba*100, 2)}%")

        # Hide technical debug info in an expander
        with st.expander("View Pipeline Debug Info"):
            st.write("**Model Expected Features:**", list(app_model.feature_names_in_))
            st.write("**Processed Input Columns:**", input_df.columns.tolist())

# streamlit run Heart_app.py