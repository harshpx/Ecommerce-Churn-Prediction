import numpy as np
import streamlit as st
import pickle

def load_churn_model():
    model = pickle.load(open('models/churn_model.pkl','rb'))
    return model

def load_customer_satisfaction_model():
    model = pickle.load(open('models/customer_satisfaction_model.pkl','rb'))
    return model

def predict_churn(data):
    model = load_churn_model()
    pred = model.predict(np.array(data).reshape(1,-1))[0]
    return pred

def predict_satisfaction_score(data):
    model = load_customer_satisfaction_model()
    pred = model.predict(np.array(data).reshape(1,-1))[0]
    return pred


def main():
    st.title("Storepro Customer Analysis")
    st.markdown("<p>Made with ❤️ by Harsh Priye</p>", unsafe_allow_html=True)

    tool = st.radio("Select Tool", ("Churn Prediction", "Customer Satisfaction Analyzer"))

    if tool == "Churn Prediction":
        data = []
        col1, col2, col3 = st.columns(3)

        with col1:
            tenure = st.number_input("Enter Customer tenure (in Years)", step=1, value=0, format="%d")
            data.append(tenure)
        with col2:
            tiers = [1,2,3]
            tier = st.selectbox("Select Customer's city Tier", tiers)
            data.append(tier)
        with col3:
            dist = st.number_input("Enter dist from warehouse (in Km)", step=0.1, value=0.0)
            data.append(dist)


        col4, col5, col6 = st.columns(3)
        with col4:
            payment_dict = {'Debit Card':0, 'Credit Card':1, 'E wallet':2, 'UPI':3, 'COD':4, 'CC':5, 'Cash on Delivery':6}
            modes = ['Debit Card','Credit Card','E wallet','UPI','COD','CC','Cash on Delivery']
            payment_mode = st.selectbox("Select preferred payment method", modes)
            payment_mode = payment_dict[payment_mode]
            data.append(payment_mode)
        with col5:
            gender_dict = {'Female':0, 'Male':1}
            gen = ['Female','Male']
            gender = st.selectbox("Select customer's gender", gen)
            gender = gender_dict[gender]
            data.append(gender)
        with col6:
            time = st.number_input("Enter hours spent on app (in Hours)", step=0.1, value=0.0)
            data.append(time)


        col7, col8, col9 = st.columns(3)
        with col7:
            num_devices = st.number_input("Enter number of devices registered", step=1, value=0)
            data.append(num_devices)
        with col8:
            category_dict = {'Laptop & Accessory':0, 'Mobile Phone':1, 'Fashion':2, 'Mobile':3, 'Grocery':4, 'Others':5}
            cat = ['Laptop & Accessory','Mobile Phone','Fashion','Mobile','Grocery','Others']
            category = st.selectbox("Select preferred category", cat)
            category = category_dict[category]
            data.append(category)
        with col9:
            satisfaction_score = [1,2,3,4,5]
            score = st.selectbox("Select customer satisfaction score", satisfaction_score)
            data.append(score)
            
        col10, col11, col12 = st.columns(3)
        with col10:
            status_dict = {'Married':0, 'Single':1, 'Divorced':2}
            rel = ['Married','Single','Divorced']
            status = st.selectbox("Select customer's maritial status", rel)
            status = status_dict[status]
            data.append(status)
        with col11:
            comp_dict = {'No':0, 'Yes':1}
            comp = ['No','Yes']
            complaints = st.selectbox("Had any complaint history?", comp)
            complaints = comp_dict[complaints]
            data.append(complaints)
        with col12:
            order_count = st.number_input("Enter total order count", step=1, value=0)
            data.append(order_count)

        
        col13, col14, col15 = st.columns(3)
        with col13:
            last_order_time = st.number_input("When did the order placed? (in Days)", step=1, value=0)
            data.append(last_order_time)
        with col14:
            cashback_amount = st.number_input("Total cashback recieved (in Rupees)", step=1, value=0)     
            data.append(cashback_amount)

        submit_button = st.button("Predict Churn")
        if submit_button:
            result = predict_churn(data)
            if result==0:
                st.write("Customer is unlikely to withdraw anytime soon")
            else:
                st.write("Customer is likely to withdraw within a month")

    else:
        data = []
        col1, col2, col3 = st.columns(3)

        with col1:
            tenure = st.number_input("Enter Customer tenure (in Years)", step=1, value=0, format="%d")
            data.append(tenure)
        with col2:
            tiers = [1,2,3]
            tier = st.selectbox("Select Customer's city Tier", tiers)
            data.append(tier)
        with col3:
            dist = st.number_input("Enter dist from warehouse (in Km)", step=0.1, value=0.0)
            data.append(dist)


        col4, col5, col6 = st.columns(3)
        with col4:
            payment_dict = {'Debit Card':0, 'Credit Card':1, 'E wallet':2, 'UPI':3, 'COD':4, 'CC':5, 'Cash on Delivery':6}
            modes = ['Debit Card','Credit Card','E wallet','UPI','COD','CC','Cash on Delivery']
            payment_mode = st.selectbox("Select preferred payment method", modes)
            payment_mode = payment_dict[payment_mode]
            data.append(payment_mode)
        with col5:
            gender_dict = {'Female':0, 'Male':1}
            gen = ['Female','Male']
            gender = st.selectbox("Select customer's gender", gen)
            gender = gender_dict[gender]
            data.append(gender)
        with col6:
            time = st.number_input("Enter hours spent on app (in Hours)", step=0.1, value=0.0)
            data.append(time)


        col7, col8, col9 = st.columns(3)
        with col7:
            num_devices = st.number_input("Enter number of devices registered", step=1, value=0)
            data.append(num_devices)
        with col8:
            category_dict = {'Laptop & Accessory':0, 'Mobile Phone':1, 'Fashion':2, 'Mobile':3, 'Grocery':4, 'Others':5}
            cat = ['Laptop & Accessory','Mobile Phone','Fashion','Mobile','Grocery','Others']
            category = st.selectbox("Select preferred category", cat)
            category = category_dict[category]
            data.append(category)
        with col9:
            status_dict = {'Married':0, 'Single':1, 'Divorced':2}
            rel = ['Married','Single','Divorced']
            status = st.selectbox("Select customer's maritial status", rel)
            status = status_dict[status]
            data.append(status)
            
        col10, col11, col12 = st.columns(3)
        with col10:
            comp_dict = {'No':0, 'Yes':1}
            comp = ['No','Yes']
            complaints = st.selectbox("Had any complaint history?", comp)
            complaints = comp_dict[complaints]
            data.append(complaints)
        with col11:
            order_count = st.number_input("Enter total order count", step=1, value=0)
            data.append(order_count)
        with col12:
            last_order_time = st.number_input("When did the order placed? (in Days)", step=1, value=0)
            data.append(last_order_time)

        
        col13, col14, col15 = st.columns(3)
        with col13:
            cashback_amount = st.number_input("Total cashback recieved (in Rupees)", step=1, value=0)     
            data.append(cashback_amount)
            

        submit_button = st.button("Predict satisfaction score")
        if submit_button:
            result = predict_satisfaction_score(data)
            st.write(f"Customer satisfaction score(out of 5, higher the better): {result+1}")

if __name__ == "__main__":
    main()
