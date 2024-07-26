import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#Data
food = pd.read_csv('onlinefoods.csv')

# Remove unnecessary columns
food_cleaned = food.drop(columns=['Unnamed: 12'])

# Define features and target variable
X = food_encoded.drop(columns=['Output_No', 'Output_Yes'])
y = food_encoded['Output_Yes']

# Inisialisasi model Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Latih model
model.fit(X_train, y_train)


# Input data
Age = st.text_input('Age', key="A1")
Feedback = st.text_input('Feedback', key="A2")
Monthly_Income = st.text_input('Monthly Income', key="A3")
Marital_Status = st.text_input('Marital Status', key="A4")

Kepuasan = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Convert input to appropriate data types
        age = float(Age) if Age else None
        feedback = Feedback
        monthly_income = float(Monthly_Income) if Monthly_Income else None
        marital_status = Marital_Status

        if age is None or monthly_income is None:
            st.error("Pastikan semua input diisi dengan angka yang valid.")
        else:
            # Melakukan prediksi
            Satisfaction = model.predict([[age, feedback, monthly_income, marital_status]])

            # Menentukan kategori harga berdasarkan prediksi
            if Satisfaction[0] == 1:
                Kepuasan = 'Yes'
            elif Satisfaction[0] == 2:
                Kepuasan = 'No'
            else:
                Kepuasan = 'NotFound'
            
            st.success(Kepuasan)

    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
