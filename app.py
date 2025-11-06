import streamlit as st
from src.extraction import load_data
import src.answer as asw

st.set_page_config(layout='wide')

def creat_aswer_section(df):
    st.title("Main questions answer")
    st.header("First round")

    st.subheader("How many bikes are being sold by their owners and how many bikes are being sold by distributors?")
    st.subheader("How many bikes are being sold are bikes from unique owner?")
    st.subheader("Are high kilometers bikes more expensive than bikes with lower kilometer?")
    return None

def main():
    df = load_data()

    creat_aswer_section(df)

    st.dataframe (df)

if __name__ =='__main__':
    main()   
# Adicionando comentario
