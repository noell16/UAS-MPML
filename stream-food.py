import streamlit as st


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
            Satisfaction = food_model.predict([[age, feedback, monthly_income, marital_status]])

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
