import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black;text-align:center">Health Insurance Cost Prediction Using ML</h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Load the model
    model = joblib.load('model_insurance')

    # Input fields
    p1 = st.slider('Enter your Age', 18, 100)
    
    s1 = st.selectbox('Sex', ('Male', 'Female'))
    p2 = 1 if s1 == 'Male' else 0  # Convert to numeric format
    
    p3 = st.number_input('Enter Your BMI Value')
    
    p4 = st.slider('Enter Number of Children', 0, 4)
    
    s2 = st.selectbox('Smoker', ('Yes', 'No'))
    p5 = 1 if s2 == 'Yes' else 0  # Convert to numeric format
    
    p6 = st.slider('Enter Your Region', 1, 4)
    
    pred = None  # Initialize pred before use

    if st.button('Predict'):
        pred = model.predict([[p1, p2, p3, p4, p5, p6]])
        st.success('Your Insurance Cost is ${}'.format(round(pred[0], 2)))  # Moved inside the button block

if __name__ == '__main__':
    main()
