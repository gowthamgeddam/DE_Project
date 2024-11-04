import streamlit as st
def clear_session():
        st.session_state["logged_in"] = False
        st.session_state["role"] = None
        st.session_state["username"] = None