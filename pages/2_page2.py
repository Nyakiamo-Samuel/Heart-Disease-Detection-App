import streamlit as st

st.title("Summary of the Heart Disease Analytics & Predictive Intelligence System")

st.markdown("""
## Project Executive Summary: Heart Disease Analytics & Predictive Intelligence

### 1. Project Overview
The **Heart Disease Analytics & Predictive Intelligence System** is a sophisticated, end-to-end data science solution designed to bridge the gap between complex clinical data and actionable medical insights. The project encompasses the full data lifecycle—from rigorous exploratory data analysis (EDA) and preprocessing to the deployment of a high-performance machine learning model via an interactive web application. The primary objective is to provide clinicians and health researchers with a tool that can accurately identify risk factors and predict the presence of heart disease based on standardized physiological metrics.

### 2. Technical Architecture & Development Workflow
The project is structured into two distinct but interconnected phases: the analytical research phase and the deployment phase.

* **Analytical Phase (Jupyter Notebook):** Utilizing `Heart_disease.ipynb`, the development team performed extensive data cleaning and statistical modeling. This phase involved handling missing values, identifying outliers in clinical features like cholesterol and blood pressure, and evaluating various classification algorithms to find the most accurate predictor.
* **Deployment Phase (Streamlit Framework):** The model was operationalized using `Heart_app.py`, creating a responsive web dashboard. This allows non-technical users to interact with the machine learning model in real-time, entering patient data and receiving instant risk assessments.

### 3. Machine Learning Methodology
The core of the system is a supervised learning classifier, specifically a **Logistic Regression** or similar ensemble model (serialized as `logistic_heart_model.jbl`), chosen for its balance of interpretability and predictive power.

* **Feature Engineering:** The system processes 13 critical medical features, including:
    * **Demographics:** Age and Sex.
    * **Symptomology:** Chest pain type and Exercise-induced Angina.
    * **Clinical Measurements:** Resting Blood Pressure (BP), Serum Cholesterol, and Maximum Heart Rate (Max HR).
    * **EKG Metrics:** ST depression (Oldpeak), the slope of the peak exercise ST segment, and the number of major vessels colored by fluoroscopy.
* **Model Persistence:** By using `joblib` for model serialization, the application ensures high-speed inference, allowing the predictive intelligence model to run without the need for constant retraining.

### 4. Interactive Data Visualization & Dashboarding
The project emphasizes "Data Storytelling" through an advanced visualization suite built with `Plotly Express`. Key analytical components include:

* **Demographic Distribution:** Histograms analyzing the prevalence of heart disease across different age cohorts and genders.
* **Comparative Analytics:** Box and Violin plots that contrast clinical variables (like Max Heart Rate vs. Cholesterol) between healthy patients and those with detected heart disease.
* **Correlation Mapping:** Heatmaps and categorical plots that identify the strongest indicators of cardiac risk, such as the relationship between Thallium stress test results and heart disease presence.

### 5. Frontend Design & User Experience (UX)
The `Heart_app.py` script demonstrates a high level of front-end customization to ensure the tool is professional and user-friendly:
* **Custom Styling:** The application uses injected CSS to modify container aesthetics, including rounded borders and custom media sizing.
* **Immersive Media:** Integrated video elements and branded imagery (via `heart_image.jpg`) create a modern, clinical atmosphere.
* **Intuitive Controls:** A sidebar navigation system allows for seamless entry of medical parameters, while a "Risk Probability" metric provides a granular view of the model's confidence in its prediction.

### 6. Safety and Ethical Considerations
Recognizing the sensitivity of medical applications, the system includes a prominent **Medical Disclaimer**. It explicitly states that the tool is intended for analytical and predictive intelligence purposes and is not a replacement for professional clinical diagnosis. This ensures that the AI is used responsibly as a supplementary decision-support tool.

### 7. Future Scalability
The modular nature of the Python scripts and the use of modern deployment frameworks make this project highly scalable. Future iterations could include:
* **Integration of SHAP/LIME:** To provide "Explainable AI" (XAI) insights, showing patients which specific factor most influenced their risk score.
* **Cloud Integration:** Deployment to Streamlit Cloud or AWS for global accessibility.
* **Batch Processing:** Extending the UI to allow for the upload of entire CSV datasets for population-wide heart health screening.

---

### **Clinical Variable Definitions**

| Variable | Description & Options |
| :--- | :--- |
| **Age** | Represents the patient's age in years. Age is a primary risk factor for heart disease. |
| **Blood Pressure (BP)** | Resting blood pressure (in mm Hg) upon admission to the hospital. |
| **Cholesterol** | Serum cholesterol in mg/dl. High levels are associated with plaque buildup in arteries. |
| **Max Heart Rate** | The maximum heart rate achieved during a stress test. |
| **ST Depression** | ST depression induced by exercise relative to rest. It measures the stress on the heart muscle. |
| **Sex** | Biological sex of the patient (**Male** or **Female**). |
| **Exercise Angina** | **Yes / No**: Whether the patient experiences chest pain specifically during physical exertion. |

---

### **Categorical Explanations**

### **Chest Pain Type**
This classifies the nature of the pain the patient is experiencing.
* **Typical Angina:** Classic heart-related chest pain caused by reduced blood flow to the heart.
* **Atypical Angina:** Chest pain that doesn't fit the classic profile but is still heart-related.
* **Non-Anginal Pain:** Pain that is likely not related to the heart (e.g., esophageal or muscular).
* **Asymptomatic:** The patient feels no pain, despite potential underlying heart issues.

### **FBS over 120 (Fasting Blood Sugar)**
* **Greater than 120 mg/dl:** Often indicates a diabetic or pre-diabetic state.
* **Less than 120 mg/dl:** Considered within a normal or controlled range.

### **EKG Results (Electrocardiogram)**
* **Normal:** No significant electrical abnormalities in the heart rhythm.
* **ST-T Abnormality:** Indicates potential ischemia (lack of oxygen) or electrolyte imbalance.
* **Left Ventricular Hypertrophy:** Shows thickening of the heart's main pumping chamber wall.


### **Slope of ST**
This refers to the peak exercise ST segment on an EKG.
* **Upsloping:** Generally considered a normal heart response to exercise.
* **Flat:** May indicate a lack of oxygen to the heart during stress.
* **Downsloping:** A strong clinical indicator of coronary artery disease.

### **Number of Vessels Fluro (0–3)**
* The number of major vessels (0 to 3) colored by fluoroscopy. This visualizes blood flow; a **lower number** usually indicates better flow (fewer blockages).

### **Thallium (Stress Test Results)**
* **Normal:** Blood flow to the heart muscle is adequate during both rest and exercise.
* **Fixed Defect:** Indicates a part of the heart muscle has permanent damage (likely a previous heart attack).
* **Reversible Defect:** Indicates blood flow is restricted during exercise but returns to normal at rest (signs of a significant blockage).
                  
""")