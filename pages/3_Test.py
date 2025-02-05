import streamlit as st
import os

def main():

    with st.expander("Show code"):
        current_file_name = os.path.abspath(__file__)
        
        with open(current_file_name, 'r') as f:
            code = f.read()
        
        st.code(code, language='python')

if __name__ == "__main__":
    main()
