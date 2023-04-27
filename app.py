import streamlit as st

from database import query_db
from plot import plot_wells

def app():
    
    st.title("This is a wells app")

    st.markdown("Input the **minimum well depth** as well as the **minimum well gradient** below. _Thank you for using the app!_")
    
    depth = st.number_input("Min depth:", 0, 10000, value=5000, step=200)
    gradient = st.number_input("Min gradient:", 0.0, 0.1, value=0.01, step=0.005)
    
    data = query_db(depth, gradient)
    st.write(plot_wells(data))

if __name__ == '__main__':
    app()