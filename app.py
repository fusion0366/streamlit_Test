# -*- coding:utf-8 -*-
import streamlit as st # streamlit 모듈 import
from utils import html_temp
from utils import dec_temp
from eda_app import run_eda_app
from ml_app import run_ml_app

def main(): # 메인 페이지 함수 생성
    st.subheader("Lee's ML Project") # 페이지 SubHeader 생성
    st.markdown(html_temp, unsafe_allow_html=True)

    menu = ['HOME', 'EDA', 'ML', 'About'] # 메뉴에 들어갈 목록 작성
    choice = st.sidebar.selectbox("Menu", menu) # 사이드 바에 SelectBox 생성

    if choice == 'HOME': # HOME 페이지
        st.subheader('HOME')
        st.markdown(dec_temp, unsafe_allow_html=True)
    elif choice == 'EDA': # EDA 페이지
        run_eda_app()
    elif choice == 'ML': # ML 페이지
        run_ml_app()
    else: # ABOUT 페이지
        st.subheader('About')

if __name__ == "__main__": # 메인 페이지 실행
    main()