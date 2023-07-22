import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('C:/Users/Vimah/Desktop/MY PROJECTS/pickled_RFC.pkl','rb'))

def main():
    st.title('HR analytics')
    
    #input variables
    experience = st.text_input('experience')
    enrolled_university = st.text_input('enrolled_university')
    relevent_experience = st.text_input('relevent_experience')
    company_size = st.text_input('company_size')
    last_new_job = st.text_input('last_new_job')
    makeprediction = ""
    
#prediction code
    if st.button('predict'):
        makeprediction = model.predict([[experience, enrolled_university, relevent_experience, company_size, last_new_job]])
        output = makeprediction[0]
        st.success('candidate remains {}'.format(output))
    
if __name__=="__main__":
    main()