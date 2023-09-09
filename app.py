import streamlit as st
from predict import show_pred_page
from explore import show_explore_page

page = st.sidebar.selectbox("Explore or Predict", ('Explore', 'Predict'))

if page == 'Predict':
    show_pred_page()
else:
    show_explore_page()