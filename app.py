# Importing Libraries
import streamlit as st
import io
import plotly.figure_factory as ff
from streamlit_option_menu import option_menu
from PIL import Image
from Alzheimer import alzheimer_prediction
from Pneumonia import pneumonia_prediction
from Diabetes import diabetes_prediction
from HeartDisease import heart_prediction
from Kidney import kidney_prediction
from Malaria import malaria_prediction


# Function to style streamlit page
def streamlit_style():
    st.markdown("""
    <style>
    
        /*Side bar*/
        .st-emotion-cache-dvne4q{
            padding:2rem 1rem;
            background: #2a454b;
            padding-bottom: 1rem;

        }

        /*Main image*/
        .st-emotion-cache-bm2z3a {
            background-image: linear-gradient(15deg, #13547a 0%, #80d0c7 100%);
            background-image: linear-gradient(to top, #505285 0%, #585e92 12%, #65689f 25%, #7474b0 37%, #7e7ebb 50%, #8389c7 62%, #9795d4 75%, #a2a1dc 87%, #b5aee4 100%);            # background: linear-gradient(to right, #4da0b0, #d39d38);
            # background-image: linear-gradient(to right, #243949 0%, #517fa4 100%);
            # background-image: linear-gradient(120deg, #e0c3fc 0%, #8ec5fc 100%);
            # background-image: linear-gradient(to top, #30cfd0 0%, #330867 100%);
            # background-image: linear-gradient(-225deg, #473B7B 0%, #3584A7 51%, #30D2BE 100%);
            # background: linear-gradient(90deg, hsla(208, 33%, 21%, 1) 0%, hsla(211, 36%, 46%, 1) 100%)
        }

        /*Main page*/
        .st-emotion-cache-13ln4jf {
            padding: 0rem 1rem 1rem 1rem;
            max-width: 80rem;
        }

        /*header*/
        .st-emotion-cache-1avcm0n{
            display:none
        }

        /*info block*/
        .st-bf {
            background-color: hsla(201, 50%, 15%, 1);
        }
        .st-bh {
            background-color: #0a3431;
        }
        
        # .st-bj{ 
            # background-color: rgba(255, 108, 108, 1);}

    </style>
    """, unsafe_allow_html=True)
streamlit_style()




def main():
    st.markdown("""<h4><center>About OmniHealth</center></h4>""", unsafe_allow_html=True)
    st.write("""**OmniHealth** is an advanced healthcare platform that leverages machine learning and deep learning techniques to predict various diseases. Our state-of-the-art models analyze medical data to provide accurate predictions, helping patients and healthcare professionals make informed decisions about their health.""")

    st.subheader("About Diseases, Symptoms, Cure, Prevention & Model Acuuracies")
    disease_data = {
        "Malaria": {
            "Symptoms": "- Fever & Chills\n- Headache\n- Muscle pain\n- Nausea\n- Vomiting",
            "Cure": "- Antimalarial medication\n- Adequate rest\n- Hydration\n- Proper nutrition\n- Avoiding mosquito bites",
            "logo":"logos\malaria_logo.jpeg",
            "train_acc":"Training Accuracy : **94.03%**",
            "test_acc":"Testing Accuracy : **94.37%**",
            "Prevention":"""- Use of insecticide-treated bed nets\n- Indoor residual spraying with insecticides \n- Taking antimalarial medications when traveling to endemic areas"""
        },
        "Kidney": {
            "Symptoms": "- Fatigue\n- Swelling in the ankles, feet, or hands\n- Shortness of breath\n- Nausea\n- Confusion",
            "Cure": "- Dialysis\n- Kidney transplant\n- Medications to manage symptoms\n- Lifestyle changes (e.g., diet, exercise)",
            "logo":"logos\kidney_logo.jpeg",
            "train_acc":"Training Accuracy : **97.50%**",
            "test_acc":"Testing Accuracy : **98.34%**",
            "Prevention": "- Maintain a healthy lifestyle \n- Manage health conditions such as diabetes and high blood pressure \n- Avoid excessive use of pain medications \n- Regular screening for kidney function",
        },
        "Alzheimer": {
            "Symptoms": "- Memory loss\n- Disorientation\n- Mood swings\n- Confusion\n- Difficulty speaking, walking, or swallowing",
            "Cure": "- No cure, but management of symptoms\n- Medications to slow progression\n- Supportive care\n- Therapy and cognitive training",
            "logo":r"logos\alzheimer_logo.jpeg",
            "train_acc":"Training Accuracy : **88.40%**",
            "test_acc":"Testing Accuracy : **88.62%**",
            "Prevention":  "- Regular Physical Exercise \n- Healthy Diet \n- Mental Stimulation \n- Social Engagement \n- Management of Cardiovascular Risk Factors (e.g., diabetes, obesity)",
        },
        "Heart Diseases": {
            "Symptoms": "- Chest pain\n- Shortness of breath\n- Palpitations\n- Fatigue\n- Dizziness\n- Fainting",
            "Cure": "- Medications (e.g., blood thinners, beta-blockers)\n- Lifestyle changes (e.g., diet, exercise)\n- Surgery (e.g., bypass surgery, valve repair)",
            "logo":"logos\heart_logo.jpeg",
            "train_acc":"Training Accuracy : **99.99%**",
            "test_acc":"Testing Accuracy : **99.99%**",
            "Prevention": "- Maintain a healthy lifestyle, i.e regular exercise & balanced diet \n- Avoid smoking \n- Manage stress \n- Control conditions like high blood pressure, high cholesterol, and diabetes",
                    
        },
        "Diabetes": {
            "Symptoms": "- Frequent urination\n- Increased thirst\n- Unexplained weight loss\n- Fatigue\n- Blurred vision",
            "Cure": "- Medications (e.g., insulin, oral medications)\n- Lifestyle changes (e.g., diet, exercise)\n- Monitoring blood sugar levels",
            "logo":"logos\diabetes_logo.jpeg",
            "train_acc":"Training Accuracy : **99.99%**",
            "test_acc":"Testing Accuracy : **90.25%**",
            "Prevention": "- Maintain a healthy weight \n- Eat a balanced diet \n- Engage in regular physical activity \n- Avoid Smoking & Alcohol consumption \n- Manage stress",
        },

        "Pneumonia" :{
            "Symptoms": "- Cough\n- Fever\n- Shortness of breath\n- Chest pain\n- Fatigue",
            "Causes": "- Bacterial infection (e.g., Streptococcus pneumoniae)\n- Viral infection (e.g., Influenza virus)\n- Fungal infection (e.g., Pneumocystis jirovecii)",
            "Cure": "- Antibiotics (for bacterial pneumonia)\n- Antiviral medications (for viral pneumonia)\n- Antifungal medications (for fungal pneumonia)\n- Oxygen therapy\n- Fluids & Rest",
            "Prevention": "- Vaccination (e.g., pneumococcal vaccine, flu vaccine)\n- Hand hygiene\n- Avoiding Smoking \n- Good respiratory hygiene (e.g., covering mouth when coughing or sneezing)",
            "logo": "logos/pneumonia_logo.jpeg",
            "train_acc":"Training Accuracy : **93.11%**",
            "test_acc":"Testing Accuracy : **90.22%**",
        }
    }


    for disease, info in disease_data.items():
        dis, tr, te = st.columns([2,3,3])
        with dis: 
            st.markdown(f"<h3>{disease}</h3>", unsafe_allow_html=True)
        # with tr:
        #     st.info(info['train_acc'])
        # with te:
        #     st.info(info['test_acc'])
        
        
        col0, col1, col2, col3 = st.columns([2, 2, 2, 2])
        with col0:
            st.image(info['logo'], use_column_width=True)
        with col1:
            st.info(f"**Symptoms:**\n{info['Symptoms']}")
        with col2:
            st.success(f"**Cure:**\n{info['Cure']}")
        with col3:
            st.success(f"**Prevention:** \n{info['Prevention']}")
            
        st.header("")
            




def diseases_prediction():

    disease_data = {
        "Malaria": {
            "Symptoms": "- Fever\n- Chills\n- Headache\n- Muscle pain\n- Nausea\n- Vomiting",
            "Cure": "- Antimalarial medication\n- Adequate rest\n- Hydration\n- Proper nutrition\n- Avoiding mosquito bites",
            "logo":"logos\malaria_logo.jpeg"
        },
        "Kidney": {
            "Symptoms": "- Fatigue\n- Swelling in the ankles, feet, or hands\n- Shortness of breath\n- Nausea\n- Confusion",
            "Cure": "- Dialysis\n- Kidney transplant\n- Medications to manage symptoms\n- Lifestyle changes (e.g., diet, exercise)",
            "logo":"logos\kidney_logo.jpeg"
        },
        "Alzheimer": {
            "Symptoms": "- Memory loss\n- Disorientation\n- Mood swings\n- Confusion\n- Difficulty speaking, walking, or swallowing",
            "Cure": "- No cure, but management of symptoms\n- Medications to slow progression\n- Supportive care\n- Therapy and cognitive training",
            "logo":r"logos\alzheimer_logo.jpeg"
        },
        "Heart Diseases": {
            "Symptoms": "- Chest pain\n- Shortness of breath\n- Palpitations\n- Fatigue\n- Dizziness\n- Fainting",
            "Cure": "- Medications (e.g., blood thinners, beta-blockers)\n- Lifestyle changes (e.g., diet, exercise)\n- Surgery (e.g., bypass surgery, valve repair)",
            "logo":"logos\heart_logo.jpeg"
        },
        "Diabetes": {
            "Symptoms": "- Frequent urination\n- Increased thirst\n- Unexplained weight loss\n- Fatigue\n- Blurred vision",
            "Cure": "- Medications (e.g., insulin, oral medications)\n- Lifestyle changes (e.g., diet, exercise)\n- Monitoring blood sugar levels",
            "logo":"logos\diabetes_logo.jpeg"
        },
        "Pneumonia" :{
            "Symptoms": "- Cough\n- Fever\n- Shortness of breath\n- Chest pain\n- Fatigue",
            "Causes": "- Bacterial infection (e.g., Streptococcus pneumoniae)\n- Viral infection (e.g., Influenza virus)\n- Fungal infection (e.g., Pneumocystis jirovecii)",
            "Treatment": "- Antibiotics (for bacterial pneumonia)\n- Antiviral medications (for viral pneumonia)\n- Antifungal medications (for fungal pneumonia)\n- Oxygen therapy\n- Fluids\n- Rest",
            "Prevention": "- Vaccination (e.g., pneumococcal vaccine, flu vaccine)\n- Hand hygiene\n- Avoiding smoking and exposure to smoke\n- Good respiratory hygiene (e.g., covering mouth when coughing or sneezing)",
            "Logo": "logos/pneumonia_logo.jpeg"
        }
    }

    Disease_opt = st.selectbox("Select Disease", list(disease_data.keys())[::-1])

    if Disease_opt == "Malaria":

        info =  disease_data['Malaria']
            
        st.markdown("""<h3><center>Malaria</center><h3>""",unsafe_allow_html=True)
        st.write("""Malaria is a mosquito-borne disease caused by the Plasmodium parasite.Malaria is a mosquito-borne disease infecting millions each year. 
                    It causes flu-like symptoms like fever, chills, and fatigue. 
                    Left untreated, it can lead to severe illness and even death. 
                    Prevention with mosquito nets and medication is crucial. """)

        poster, about = st.columns([2,5])
        with poster:      
            st.image("poster/Malaria.jpeg", use_column_width=True)
        with about:

            st.info("""**Transmission:** \nMalaria is transmitted through the bite of infected female Anopheles mosquitoes.""")

            st.success("""**Peventions:**
                \n- Use of insecticide-treated bed nets
                \n- Indoor residual spraying with insecticides
                \n- Taking antimalarial medications when traveling to endemic areas""")

            st.error("""**Challenges:** 
            \nChallenges in malaria control and elimination include drug-resistant parasites, insecticide-resistant mosquitoes, and limited access to healthcare.""")


        # from Malaria import malaria_prediction

        # File uploader for image input
        uploaded_file = st.file_uploader("Upload Cell image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='JPEG')
            
            btn = st.button("Predict") 
            if btn:
                result = malaria_prediction.predict(img_bytes)
                predicted_class = "Malaria"if result <= 0.5 else 'Normal'
                
                
                st.markdown("""<h4><center>Prediction</center><h4>""",unsafe_allow_html=True)

                col1, col2 = st.columns([2,4])
                with col1:
                    st.image(uploaded_file, caption='Cell', use_column_width=True)

                with col2:
                    if predicted_class == "Malaria":
                        st.error("Person is Diagnosed With Malaria")
                        st.success(f"**Cure:**\n{info['Cure']}")

                    else:
                        st.success("Person is Malaria Negative")
        else:
            st.write("")

    if Disease_opt == "Alzheimer":
        # Disease data
        disease_data = {
            "Alzheimer's Disease": {
                "Description": "Alzheimer's disease is a progressive neurodegenerative disorder that affects memory, thinking skills, and behavior. It is the most common cause of dementia in older adults and typically worsens over time.",
                "Transmission": "Alzheimer's disease is not infectious and cannot be transmitted from person to person.",
                "Prevention":  "- Regular Physical Exercise \n- Healthy Diet \n- Mental Stimulation \n- Social Engagement \n- Management of Cardiovascular Risk Factors (e.g., diabetes, high blood pressure, obesity)",
                "Challenges": "Challenges in managing Alzheimer's disease include early detection, accurate diagnosis, access to healthcare services, caregiver support, and development of effective treatments.",
                "Cure": "- No cure, but management of symptoms\n- Medications to slow progression\n- Supportive care\n- Therapy and cognitive training",
            
            }
        }

        # Display information about Alzheimer's Disease
        info = disease_data["Alzheimer's Disease"]
        st.markdown("<h3><center>Alzheimer</center></h3>", unsafe_allow_html=True)
        st.write(info["Description"])

        # Display images and additional information
        poster, about = st.columns([2, 5])
        with poster:
            st.image("poster\Alzheimer.jpeg", use_column_width=True)
        with about:
            st.info(f"**Transmission:** {info['Transmission']}")
            st.success(f"**Prevention:** {info['Prevention']}")
            st.error(f"**Challenges:** {info['Challenges']}")

        # from Alzheimer import alzheimer_prediction
        
        # File uploader for image input
        uploaded_file = st.file_uploader("Upload Brain Image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='JPEG')
            
            btn = st.button("Predict") 
            if btn:
                predicted_class  = alzheimer_prediction.prediction(img_bytes)
                
                st.markdown("""<h4><center>Prediction</center><h4>""",unsafe_allow_html=True)
                col1, col2 = st.columns([2, 4])
                with col1:
                    st.image(uploaded_file, caption='Brain Image', use_column_width=True)

                with col2:
                    if predicted_class == "No Impairment":
                        st.success("Person doesn't have any stage of Alzheimer")
                    else:
                        st.error(f"Person is Diagnosed with {predicted_class}")
                        st.info(f"**Cure**: \n{info["Cure"]}")

    if Disease_opt == "Kidney":

        # Disease data
        disease_data = {
            "Kidney Disease": {
                "Description": "Kidney disease, also known as renal disease, occurs when the kidneys are damaged and cannot filter blood as effectively as they should. It can lead to waste buildup in the body and other health problems.",
                "Transmission": "Kidney disease is not infectious and cannot be transmitted from person to person.",
                "Prevention": "- Maintain a healthy lifestyle \n- Manage underlying health conditions such as diabetes and high blood pressure \n- Avoid excessive use of pain medications \n- Regular screening for kidney function",
                "Challenges": "Challenges in managing kidney disease include early detection, access to healthcare services, affordability of treatment, and lifestyle modifications.",
                "Cure": "- Dialysis\n- Kidney transplant\n- Medications to manage symptoms\n- Lifestyle changes (e.g., diet, exercise)",
            }
        }

        # Display information about Kidney Disease
        info = disease_data["Kidney Disease"]
        st.markdown("<h3><center>Kidney Disease</center></h3>", unsafe_allow_html=True)
        st.write(info["Description"])

        poster, about = st.columns([2, 6])
        with poster:
            st.image("poster\Kidney.jpeg",)
        with about:
            # Display additional information
            st.info(f"**Transmission:** \n{info['Transmission']}")

            st.success(f"**Prevention:** \n{info['Prevention']}")

            st.error(f"**Challenges:** \n{info['Challenges']}")
 
        # Input form for kidney disease prediction
        st.markdown("<h3><center>Kidney Disease Prediction</center></h3>", unsafe_allow_html=True)

        # from Kidney import kidney_prediction

        c1, c2 = st.columns(2)

        with c1:
            blood_pressure = st.number_input("Blood Pressure", min_value=50, max_value=200, value=60, step=1)
            albumin = st.number_input("Albumin", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
            blood_urea = st.number_input("Blood Urea", min_value=0, max_value=500, value=27, step=1)
            serum_creatinine = st.number_input("Serum Creatinine", min_value=0.0, max_value=20.0, value=0.5, step=0.1)
            sodium = st.number_input("Sodium", min_value=100, max_value=200, value=142, step=1)

        with c2:
            haemoglobin = st.number_input("Haemoglobin", min_value=0, max_value=20, value=15, step=1)
            packed_cell_volume = st.number_input("Packed Cell Volume", min_value=0, max_value=100, value=40, step=1)
            red_blood_cell_count = st.number_input("Red Blood Cell Count", min_value=0, max_value=10, value=5, step=1)
            hypertension = st.selectbox("Hypertension", options=["Yes", "No"], index=1)
            diabetes_mellitus = st.selectbox("Diabetes Mellitus", options=["Yes", "No"], index=1)


        # Convert categorical variables to numerical values
        hypertension = 1 if hypertension == "Yes" else 0
        diabetes_mellitus = 1 if diabetes_mellitus == "Yes" else 0

        # Predict button
        if st.button("Predict"):
            # Preprocess input data
            input_data = [blood_pressure, albumin, blood_urea, serum_creatinine, sodium, haemoglobin, packed_cell_volume, red_blood_cell_count, hypertension, diabetes_mellitus]

            # Perform prediction
            prediction = kidney_prediction.prediction(input_data)
            
            # Display prediction result
            if prediction == 1:
                st.error("Person is Diagnosed With Kidney Disease")
                st.info(f"**Cure**: \n{info["Cure"]}")
            else:
                st.success("Person is Kidney Disease Negative")

    if Disease_opt == "Heart Diseases":

        # Disease data
        disease_data = {
            "Heart Disease": {
                "Description": "Heart disease, also known as cardiovascular disease, refers to a range of conditions that affect the heart and blood vessels. These conditions include coronary artery disease, heart rhythm problems (arrhythmias), heart defects, and others.",
                "Transmission": "Heart disease is not infectious and cannot be transmitted from person to person.",
                "Prevention": "- Maintain a healthy lifestyle, such as regular exercise, a balanced diet \n- Avoid smoking \n- Manage stress \n- Control conditions like high blood pressure, high cholesterol, and diabetes",
                "Cure": "- Medications (e.g., blood thinners, beta-blockers)\n- Lifestyle changes (e.g., diet, exercise)\n- Surgery (e.g., bypass surgery, valve repair)",
                "Challenges": "Challenges in managing heart disease include early detection, access to healthcare services, adherence to treatment plans, lifestyle modifications, and addressing risk factors."
            }
        }

        # Display information about Heart Disease
        info = disease_data["Heart Disease"]
        st.markdown("<h3><center>Heart Disease</center></h3>", unsafe_allow_html=True)
        st.write(info["Description"])

        poster, about = st.columns([2, 5])
        with poster:
            st.image("poster/Heart.jpeg", use_column_width='auto')
        with about:
            # Display additional information
            st.info(f"**Transmission:** \n{info['Transmission']}")
            st.success(f"**Prevention:** \n{info['Prevention']}")
            st.error(f"**Challenges:** \n{info['Challenges']}")

        # Input form for heart disease prediction
        st.markdown("<h3><center>Heart Disease Prediction</center></h3>", unsafe_allow_html=True)

        # from HeartDisease import heart_prediction

        c1, c2 = st.columns(2)
        with c1:
            a, s = st.columns(2)
            with a:
                age = st.slider("Age", min_value=1, max_value=110, value=51, step=1)
            with s:
                sex = st.radio("Sex", options=["Male", "Female"], index=1)
            cp = st.selectbox("Chest Pain Type", options=["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"], index=3)
            trestbps = st.slider("Resting Blood Pressure", min_value=80, max_value=300, value=125, step=1)
            chol = st.slider("Cholesterol Level", min_value=100, max_value=600, value=213, step=1)

        with c2:
            thalach = st.slider("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=125, step=1)
            exang = st.radio("Exercise Induced Angina", options=["Yes", "No"], index=1)
            slope = st.selectbox("Slope of ST Segment", options=["Upsloping", "Flat", "Downsloping"], index=2)
            thal = st.selectbox("Thalassemia Type", options=["Normal", "Fixed Defect", "Reversible Defect"], index=2)

        # Convert categorical variables to numerical values
        sex = 1 if sex == "Male" else 0
        exang = 1 if exang == "Yes" else 0

        # Map categorical variables to numerical values
        cp_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}
        slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
        thal_mapping = {"Normal": 0, "Fixed Defect": 1, "Reversible Defect": 2}

        # Predict button
        if st.button("Predict"):
            # Preprocess input data
            input_data = [age, sex, cp_mapping[cp], trestbps, chol, thalach, exang, slope_mapping[slope], thal_mapping[thal]]

            # Perform prediction
            prediction = heart_prediction.prediction(input_data)

            # Display prediction result
            if prediction == 1:
                st.error("Person is Diagnosed With Heart Disease")
                st.info(f"**Cure**: \n{info["Cure"]}")
            else:
                st.success("Person Has Not Any Heart Disease")

    if Disease_opt == "Diabetes":

        # Disease data
        disease_data = {
            "Diabetes": {
                "Description": "Diabetes is a chronic condition that affects how your body turns food into energy. There are two main types of diabetes: type 1 and type 2. Type 1 diabetes is an autoimmune disease where the body attacks and destroys insulin-producing cells. Type 2 diabetes occurs when the body doesn't produce enough insulin or becomes resistant to insulin.",
                "Transmission": "Diabetes is not infectious and cannot be transmitted from person to person.",
                "Prevention": "- Maintain a healthy weight \n- Eat a balanced diet \n- Engage in regular physical activity \n- Avoid smoking & Limit alcohol consumption \n- Manage stress",
                "Cure": "- Medications (e.g., insulin, oral medications)\n- Lifestyle changes (e.g., diet, exercise)\n- Blood sugar monitoring",
                "Challenges": "Challenges in managing diabetes include blood sugar control, complications such as heart disease, stroke, kidney failure, vision loss, and amputation, access to healthcare services, adherence to treatment plans, and addressing risk factors."
            }
        }

        # Display information about Diabetes
        info = disease_data["Diabetes"]
        st.markdown("<h3><center>Diabetes</center></h3>", unsafe_allow_html=True)
        st.write(info["Description"])

        poster, about = st.columns([2, 4])
        with poster:
            st.image("poster/Diabetes.jpg", use_column_width='auto')
        with about:
            # Display additional information
            st.info(f"**Transmission:** \n{info['Transmission']}")
            st.success(f"**Prevention:** \n{info['Prevention']}")
            st.error(f"**Challenges:** \n{info['Challenges']}")

        # Input form for diabetes prediction
        st.markdown("<h3><center>Diabetes Prediction</center></h3>", unsafe_allow_html=True)

        # from Diabetes import diabetes_prediction

        c1, c2 = st.columns(2)

        with c1:
            pregnancies = st.number_input("Pregnancies", min_value=0, max_value=17, value=4, step=1)
            glucose = st.number_input("Glucose Level", min_value=0, max_value=200, value=117, step=1)
            skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=12, step=1)
            insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=170, step=1)

        with c2:
            bmi = st.number_input("Body Mass Index (BMI)", min_value=0, max_value=60, value=30, step=1)
            diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.38, step=0.1)
            age = st.number_input("Age", min_value=21, max_value=90, value=30, step=1)

        # Predict button
        if st.button("Predict"):
            # Preprocess input data
            input_data = [pregnancies, glucose, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]

            # Perform prediction
            prediction = diabetes_prediction.prediction(input_data)

            # Display prediction result
            if prediction == 1:
                st.error("Person is Diagnosed With Diabetes")
                st.info(f"**Cure**: \n{info['Cure']}")
            else:
                st.success("Person Has Not Diabetes")

    if Disease_opt == "Pneumonia":
        # Disease data
        disease_data = {
            "Pneumonia": {
                "Description": "Pneumonia is an infection that inflames air sacs in one or both lungs. The air sacs may fill with fluid or pus (purulent material), causing cough with phlegm or pus, fever, chills, and difficulty breathing.",
                "Transmission": "Pneumonia can be caused by a variety of infectious agents, including bacteria, viruses, and fungi. It can spread through respiratory droplets from coughs or sneezes of an infected person.",
                "Prevention": "\n- Vaccination (e.g., pneumococcal vaccine, flu vaccine) \n- Hand hygiene\n- Avoiding smoking and exposure to smoke\n- Good respiratory hygiene (e.g., covering mouth when coughing or sneezing)",
                "Treatment": "- Antibiotics (for bacterial pneumonia)\n- Antiviral medications (for viral pneumonia)\n- Antifungal medications (for fungal pneumonia)\n- Oxygen therapy\n- Fluids\n- Rest",
                "Cure": "Prompt and appropriate treatment can cure most cases of pneumonia. However, severe cases may require hospitalization and intensive care.",
                "Challenges": "Challenges in managing pneumonia include differentiating between bacterial, viral, and fungal pneumonia to determine appropriate treatment. Additionally, increasing antibiotic resistance poses a significant challenge. Access to healthcare services, especially in rural or low-resource areas, can also be problematic. Complications such as respiratory failure, sepsis, and lung abscesses in severe cases further complicate treatment."
            }
        }

        # Display information about Pneumonia
        info = disease_data["Pneumonia"]
        st.markdown("<h3><center>Pneumonia</center></h3>", unsafe_allow_html=True)
        st.write(info["Description"])

        # Display images and additional information
        poster, about = st.columns([3, 6])
        with poster:
            st.image("poster/pnuemonia.jpeg", use_column_width=True)
        with about:
            st.info(f"**Transmission:** {info['Transmission']}")
            st.success(f"**Prevention:** {info['Prevention']}")
            st.warning(f"**Challenges:** {info['Challenges']}")

        # from Pneumonia import pneumonia_prediction  # Assuming you have a module for pneumonia prediction
        
        # File uploader for image input
        uploaded_file = st.file_uploader("Upload Chest X-ray Image", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            img = Image.open(uploaded_file)
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='JPEG')
            
            btn = st.button("Predict") 
            if btn:
                result = pneumonia_prediction.prediction(img_bytes)
                predicted_class = "Pneumonia" if result > 0.5 else "Normal"
                
                st.markdown("""<h4><center>Prediction</center><h4>""", unsafe_allow_html=True)
                col1, col2 = st.columns([2, 4])
                with col1:
                    st.image(uploaded_file, caption='Chest X-ray Image', use_column_width=True)

                with col2:
                    if predicted_class == "Normal":
                        st.success("The chest X-ray does not show signs of pneumonia.")
                    else:
                        st.error("The chest X-ray suggests the presence of pneumonia.")
                        st.info(f"**Cure**: \n{info['Treatment']}")


def streamlit_menu():

    # st.sidebar.markdown("<h2><center>OmniHealth</center></h2>",unsafe_allow_html=True)
    st.markdown("<h2><center>𝔒𝔪𝔫𝔦<span style='color: red;'>ℌ𝔢𝔞𝔩𝔱𝔥</span> : Smart Health Disease Predictor</span></center></h2>",unsafe_allow_html=True)
    
    selected_option = option_menu(
        None,
        ["Home","Diseases Prediction", "Baymax"],
        icons = ['house', 'gear', 'robot'],
        default_index=0,
        orientation='horizontal',


        styles={
            "container": {"padding": "0", "background-color": "#051937"},
            "icon": {"color": "white", "font-size": "20px"}, 
            "nav-link": {"font-size": "15px", "text-align": "center", "margin":"2px", "--hover-color": "#1f7ea1"},
            "nav-link-selected": {"background-color": "#1f7ea1"},
        }
    )

    return selected_option



if __name__=="__main__":
    try:
        selected = streamlit_menu()
        if selected=="Home": 
            main()
        if selected=="Diseases Prediction":
            diseases_prediction()
        if selected=="Baymax":
            from chatbot import chat
            chat()
            pass

    except Exception as e:
        st.error(f"Error has occured - {e}")