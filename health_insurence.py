
import streamlit as st
import joblib

def main():

        
    custom_css = """
    
     <style>
         body {
             margin: 0;
             padding: 0;
         }
         .stApp {
             top: 0;
             left: 0;
         }
     </style>
     """
    st.markdown(custom_css, unsafe_allow_html=True)

    st.image("https://th.bing.com/th/id/R.e56f0b4eea4fcc654db364a0b5fea0d7?rik=i9ejhoU%2bQMUjaQ&riu=http%3a%2f%2fsvecwexams.in%2fimgs%2flogo.png&ehk=fqI%2fnx8iyOYoJETkjZ%2bMab6d2AYr%2brDy9tY%2bTnkAPUM%3d&risl=&pid=ImgRaw&r=0")
    html_temp = """
    <div style = "background-color : lightblue;padding:16px"> 
    <h2 style="color:black";text-align:center>Health Insurance Cost Prediction</h2>
    </div>
    
    """
    
    
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('C:\python_ws\model_joblib_gr')
    
    p1 = st.slider('Enter your age',18,100)
    s2 = st.radio('Gender',('Male','Female'),horizontal=True)
    
    if s2=='Male':
       p2=1
    elif s2=='Female':
        p2=0  

    p3 = st.number_input("Enter you BMI Value")
    
    p4 = st.number_input("Enter number of children",0 ,4,value=None,placeholder="Enter number of children")
    
    s5 = st.radio('Smoker',('Yes','No'),horizontal=True)
    
    if s5=='Yes':
       p5=1
    else:
       p5=0
    
    s6 = st.radio('Region',('North East','North West','South East','South West'),horizontal=True)
    
    if s6=='North East':
       p6=1
    elif s6=='North West':
       p6=2
    elif s6=='South East':
       p6=3
    else:
       p6=4

    
    if st.button('predict'):
        
        if p3<=0 and p4==None :
            st.error("Fields must not be empty")
            st.error("Enter valid BMI value")
            st.error("Enter valid number of children")
            
        elif p3<=0  :
            st.error("Enter valid BMI value")
        elif p4==None or p4>=5:
            st.error("Enter valid number of children")
        
        else:
            pred = model.predict([[p1,p2,p3,p4,p5,p6]])
            st.balloons()
            #st.snow()
            
            st.success("Your Insurance cost is {}".format(round(pred[0],2)))
            
        
       
        
   
     



if __name__ == '__main__':
    main()