import streamlit as st
import numpy as np
import pickle
model = ''
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
ch = list()

st.markdown("<h1 style='text-align: center;'>Market Segmentation</h1>",
            unsafe_allow_html=True)
nav = st.sidebar.radio("Navigation", ['Input Section'])

if nav == 'Input Section':

    st.subheader("Please Enter the given values")
    col1, col2 = st.columns(2)
    bal = col1.number_input(
        "BALANCE", format="%.4f")

    bal_freq = col2.number_input(
        "BALANCE FREQUENCY", format="%.4f")

    purchases = col1.number_input(
        "PURCHASES",  format="%.4f")

    one_off_pur = col2.number_input(
        "ONEOFF PURCHASES",  format="%.4f")

    install_pur = col1.number_input(
        "INSTALLMENTS_PURCHASES", format="%.4f")

    cash_advance = col2.number_input(
        "CASH ADVANCE",  format="%.4f")

    pur_freq = col1.number_input(
        "PURCHASES FREQUENCY", format="%.4f")

    one_pur_freq = col2.number_input(
        "ONEOFF PURCHASES FREQUENCY",  format="%.4f")

    pur_install_freq = col1.number_input(
        "PURCHASES INSTALLMENTS FREQUENCY",  format="%.4f")

    cash_advance_freq = col2.number_input(
        "CASH ADVANCE FREQUENCY", format="%.4f")

    cash_advance_trx = col1.number_input(
        "CASH ADVANCE TRX",  format="%.4f")

    pur_trx = col2.number_input(
        "PURCHASES TRX", format="%.4f")

    credit_limit = col1.number_input(
        "CREDIT LIMIT",  format="%.4f")

    pay = col2.number_input(
        "PAYMENTS",  format="%.4f")

    m_pay = col1.number_input(
        "MINIMUM PAYMENTS",  format="%.4f")

    prc = col2.number_input(
        "PRC FULL PAYMENT",  format="%.4f")

    tenure = col1.number_input(
        "TENURE", format="%.4f")

    if st.button('submit'):
        ch.append(bal)
        ch.append(bal_freq)
        ch.append(purchases)
        ch.append(one_off_pur)
        ch.append(install_pur)
        ch.append(cash_advance)
        ch.append(pur_freq)
        ch.append(one_pur_freq)
        ch.append(pur_install_freq)
        ch.append(cash_advance_freq)
        ch.append(cash_advance_trx)
        ch.append(pur_trx)
        ch.append(credit_limit)
        ch.append(pay)
        ch.append(m_pay)
        ch.append(prc)
        ch.append(tenure)
        y_pred = model.predict(np.array(ch).reshape(1, -1))
        st.info(f'Input:  {ch}')
        st.success(f'This belong to Cluster: {y_pred}')
