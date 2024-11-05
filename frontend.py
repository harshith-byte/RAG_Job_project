import streamlit as st
from integrate_ollama import get_response
import pandas as pd
import json

import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


set_background('image.png')
st.title("VantageHire")
st.text("Finding jobs from a vantage point of clarity")
query = st.text_input("Enter the title or Job description :")
if query:
#     df = json.dumps(get_response(query))
    df = get_response(query)
#     st.write(df)
    ROWS_PER_PAGE = 10

    # Track the current page using Streamlit's session state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 0

    # Calculate total pages
    total_pages = (len(df) - 1) // ROWS_PER_PAGE + 1

    # Get data for the current page
    start_row = st.session_state.current_page * ROWS_PER_PAGE
    end_row = start_row + ROWS_PER_PAGE
    page_data = df.iloc[start_row:end_row]

    # Display current page data
#     for row in df:
#         with st.expander(f"Title : {row['title']}"):
#             st.write(f"occupation : {row['occupation']}")
#             st.write(f"Employer Description : {row['employer_description']}")
#             st.write(f"Description : {row['description']}")
#             st.write(f"Date : {row['insertion_date']}")

    st.write(page_data)
    # Pagination controls
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous") and st.session_state.current_page > 0:
            st.session_state.current_page -= 1

    with col2:
        if st.button("Next") and st.session_state.current_page < total_pages - 1:
            st.session_state.current_page += 1

    st.write(f"Page {st.session_state.current_page + 1} of {total_pages}")