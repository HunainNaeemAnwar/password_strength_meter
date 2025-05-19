import streamlit as st
import re
import random

# Some Common Passwords 
common_passwords:list=["password", "123456", "qwerty", "abc123", "letmein", "password123", "admin", "welcome", "12345678"] 
#Special  Characters
special_chars:str="!@#$^&*"

def gernerate_strong_password()->str:
    length=12
    uppercase=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lowercase=random.choice("abcdefghijklmnopqrstuvwxyz")
    digit=random.choice("123456790")
    remaining="".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456790" +special_chars,k=length-4))
    password=list(uppercase+lowercase+digit+remaining)
    random.shuffle(password)
    return "".join(password)

def check_password_strength(password):
    score:int=0
    feedback:list=[]

    if password.lower() in common_passwords:
        return 0 ,["This Password Is Too Common"]

    if len(password) >=8:
        score+=2
    else:
        feedback.append("Password Should Be 8 Characters Long")
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score+=1
    else:
        feedback.append("Password Should Include Lowercase and uppercase Characters Both")
    if re.search(r"\d",password):
        score+=1
    else:
        feedback.append("Password Must Contain Numbers")
    if re.search(r"[!@#$%^*&]",password):
        score+=1
    else:
        feedback.append("Password Should Include At leaset One Special Character")
    return score,feedback


st.title("Password Strength Meter")
st.write("Enter Password To Check It's strength ")
password= st.text_input("Enter Password" ,type="password")
if st.button("Check Strength"):
    if password:
        score ,feedback=check_password_strength(password)
        if score==5:
            st.success("Strong Password ! You're Secure")
        elif score >=3 and score <5 :
            st.warning("Moderate Pssword - Consider Adding More Security Features")
        else:
            st.error("Weak Password - Improve It Using The Suggestions Below")
        for issue in feedback:
            st.write(issue)
        if score <5:
            st.write("Suggested Strong Password")
            st.code(gernerate_strong_password())
    else:
        st.error("Please Enter A Password")

            

    

