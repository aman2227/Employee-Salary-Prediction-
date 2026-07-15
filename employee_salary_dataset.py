import pandas as pd
import numpy as np
import datetime
# from sklearn import GradientBoostingRegressor
import joblib
# import GradientBoostingRegressor as gbr
import streamlit as st

def main():
    html_temp = """<h1>Employee Salary Prediction</h1>""" ## isme hum htm use kar rahe hai 
    

    # gbr=GradientBoostingRegressor()
    # model = GradientBoostingRegressor()
    # model.load_model("gbr_model.pkl")
    # joblib.dump_model("xgb_model.pkl")
    # model.load_model("gbr_model.pkl")
    model = joblib.load('gbr_model.pkl')

    st.markdown(html_temp, unsafe_allow_html=True) ## ye ek methon hai streamlit (ye kisi bhi text ko browser pe show karata hai markdown)
    st.markdown("This app will help you to predict the Salary of Employee")

    p1 = st.number_input("Please enter age (In Years)",18.0,70.0,step=1.0) 

    s1 = st.selectbox("Select the Gender",("Female","Male"))

    if s1=='Female':
        p2=1
    elif s1=='Male':
        p2=2

    s2 = st.selectbox("Select the Education",("Diploma","Bachelor","Master","PhD"))

    if s2=='None':
        p3=0
    elif s2=='Diploma':
        p3=1
    elif s2=='Bachelor':
        p3=2
    elif s2=='Master':
        p3=3
    elif s2=='PhD':
        p3=4
    
    p4 = st.number_input("Please enter the Year of Experience (In Years)",0,25,step=1)

    s3 = st.selectbox("Select the Department",("None","Operations","IT","Sales","HR","Marketing"))
    
    if s3=='None':
        p5=0
    elif s3=='Operations':
        p5=1
    elif s3=='HR':
        p5=2
    elif s3=='Sales':
        p5=3
    elif s3=='Marketing':
        p5=4
    elif s3=='IT':
        p5=5



    s4 = st.selectbox("Select the Job_Level",("None","Junior","Lead","Mid","Senior","Manager"))
 
    if s4=='None':
        p6=0
    elif s4=='Junior':
        p6=1
    elif s4=='Lead':
        p6=2
    elif s4=='Mid':
        p6=3
    elif s4=='Senior':
        p6=6
    elif s4=='Manager':
        p6=5

    
    p7 = st.number_input("Enter Performance_Rating (In Numbers)",1.0,5.0,step=1.0)

    p8 = st.number_input("Enter number of Certifications ",0,10,step=1)

    p9 = st.number_input("Enter number of Overtime Work (In Hours)  ",1,60,step=1)
    

    s5 = st.selectbox("Select the Remote_Work",("None","Yes","No"))

    if s5=='None':
        p10=0
    elif s5=='Yes':
        p10=1
    elif s5=='No':
        p10=2

    
    s6 = st.selectbox("Select the City",("None","Hyderabad","Mumbai","Chennai","Delhi"))

    if s6=='None':
        p11=0
    elif s6=='Chennai':
        p11=1
    elif s6=='Delhi':
        p11=2
    elif s6=='Hyderabad':
        p11=3
    elif s6=='Mumbai':
        p11=4

    
    p12 = st.number_input("Enter number of Company_Tenure (In Crore)  ",0,15,step=1)


    p13 = st.number_input("Enter number of Project Done  ",1,30,step=1)


    p14 = st.number_input("Enter the Skill-Score  ",0,100,step=1)

    
    
    data_new = pd.DataFrame({
    'Age':p1,
    'Gender':p2,
    'Education':p3,
    'Experience_Years':p4,
    'Department':p5,
    'Job_Level':p6,
    'Performance_Rating':p7,
    'Certifications':p8,
    'Overtime_Hours':p9,
    'Remote_Work':p10,
    'City':p11,
    'Company_Tenure':p12,
    'Projects_Completed':p13,
    'Skill_Score':p14,
    },
    index=[0])

    if st.button("Predict"):
        pred = model.predict(data_new)
        # st.success("You can sell your car at {:.2f} lakhs".format(pred [0]))
         
        st.markdown(f"""
<div style="padding:20px;
background:#E8F5E9;
border-radius:15px;
text-align:center;">
<h2>💰 Predicted Salary</h2>
<h1>{pred[0]:.2f} LPA</h1>
</div>
""",unsafe_allow_html=True)




if __name__=='__main__':
    main()