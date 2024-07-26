import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#Data
food = pd.read_csv('onlinefoods.csv')

# Remove unnecessary columns
food_cleaned = food.drop(columns=['Unnamed: 12'])

# Perform one-hot encoding on categorical variables
food_encoded = pd.get_dummies(food_cleaned, columns=[
    'Gender', 'Marital Status', 'Occupation', 'Monthly Income',
    'Educational Qualifications', 'Feedback', 'Output'
])

# Define features and target variable
X = food_encoded.drop(columns=['Output_No', 'Output_Yes'])
y = food_encoded['Output_Yes']

# Misalnya, data X dan target y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inisialisasi model Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Latih model
model.fit(X_train, y_train)

# Judul web
st.title('Prediksi Kepuasan Pelanggan')

# Input data
Age = st.text_input('Age')
Feedback = st.text_input('Feedback')
Monthly_Income = st.text_input('Monthly Income')
Marital_Status = st.text_input('Marital Status')

Kepuasan = ''

import streamlit as st

# Fungsi untuk melakukan konversi dan validasi input
def convert_and_validate_input(Age, Feedback, Monthly_Income, Marital_Status):
    try:
        age = float(Age) if Age else None
        monthly_income = float(Monthly_Income) if Monthly_Income else None
        feedback = int(Feedback) if Feedback else None
        marital_status = int(Marital_Status) if Marital_Status else None

        if age is None or feedback is None or monthly_income is None or marital_status is None:
            st.error("Pastikan semua input diisi dengan angka yang valid.")
            return None
        else:
            return age, feedback, monthly_income, marital_status

    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
        return None

# Fungsi utama untuk melakukan prediksi
def main():
    st.title("Prediksi Kepuasan")

    # Input dari pengguna
    Age = st.text_input("Usia")
    Feedback = st.text_input("Feedback (1 atau 2)")
    Monthly_Income = st.text_input("Pendapatan Bulanan")
    Marital_Status = st.text_input("Status Pernikahan (1 atau 2)")

    if st.button("Prediksi"):
        try:
            # Konversi dan validasi input
            input_data = convert_and_validate_input(Age, Feedback, Monthly_Income, Marital_Status)

            if input_data:
                age, feedback, monthly_income, marital_status = input_data

                # Melakukan prediksi
                Satisfaction = model.predict([[age, feedback, monthly_income, marital_status]])

                # Menentukan kategori kepuasan berdasarkan prediksi
                if Satisfaction[0] == 1:
                    Kepuasan = 'Yes'
                elif Satisfaction[0] == 2:
                    Kepuasan = 'No'
                else:
                    Kepuasan = 'NotFound'
                
                st.success(f"Kepuasan: {Kepuasan}")

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

# Jalankan aplikasi
if __name__ == "__main__":
    main()
import streamlit as st

# Fungsi untuk melakukan konversi dan validasi input
def convert_and_validate_input(Age, Feedback, Monthly_Income, Marital_Status):
    try:
        age = float(Age) if Age else None
        monthly_income = float(Monthly_Income) if Monthly_Income else None
        feedback = int(Feedback) if Feedback else None
        marital_status = int(Marital_Status) if Marital_Status else None

        if age is None or feedback is None or monthly_income is None or marital_status is None:
            st.error("Pastikan semua input diisi dengan angka yang valid.")
            return None
        else:
            return age, feedback, monthly_income, marital_status

    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
        return None

# Fungsi utama untuk melakukan prediksi
def main():
    st.title("Prediksi Kepuasan")

    # Input dari pengguna
    Age = st.text_input("Usia")
    Feedback = st.text_input("Feedback (1 atau 2)")
    Monthly_Income = st.text_input("Pendapatan Bulanan")
    Marital_Status = st.text_input("Status Pernikahan (1 atau 2)")

    if st.button("Prediksi"):
        try:
            # Konversi dan validasi input
            input_data = convert_and_validate_input(Age, Feedback, Monthly_Income, Marital_Status)

            if input_data:
                age, feedback, monthly_income, marital_status = input_data

                # Melakukan prediksi
                Satisfaction = model.predict([[age, feedback, monthly_income, marital_status]])

                # Menentukan kategori kepuasan berdasarkan prediksi
                if Satisfaction[0] == 1:
                    Kepuasan = 'Yes'
                elif Satisfaction[0] == 2:
                    Kepuasan = 'No'
                else:
                    Kepuasan = 'NotFound'
                
                st.success(f"Kepuasan: {Kepuasan}")

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

# Jalankan aplikasi
if __name__ == "__main__":
    main()
