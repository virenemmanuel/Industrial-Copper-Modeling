from datetime import date
import numpy as np
import pickle
import streamlit as st

# ----------------- Streamlit page configuration -----------------
def streamlit_config():
    st.set_page_config(page_title='INDUSTRIAL COPPER MODELING')

    # Page header transparent color
    page_background_color = """
    <style>
    [data-testid="stHeader"] { background: rgb(0,0,0,0); }
    </style>
    """
    st.markdown(page_background_color, unsafe_allow_html=True)

    # Page title centered
    st.markdown(f'<h1 style="text-align: center;">INDUSTRIAL COPPER MODELING</h1>', unsafe_allow_html=True)


# ----------------- Custom styles -----------------
def style_submit_button():
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color : #367F89;
            color: white;
            width: 70%
        }
        </style> """, unsafe_allow_html=True)

def style_prediction():
    st.markdown("""
        <style>
        .center-text { text-align: center; color : #20CA0C }
        </style>
        """, unsafe_allow_html=True)

# ----------------- Input data options -----------------
country_values = [25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 32.0, 38.0, 39.0, 40.0, 77.0,
                  78.0, 79.0, 80.0, 84.0, 89.0, 107.0, 113.0]

status_values = ['Won', 'Lost', 'Draft', 'To be approved', 'Not lost for AM',
                 'Wonderful', 'Revised', 'Offered', 'Offerable']

status_dict = {'Won':0, 'Lost':1, 'Draft':2, 'To be approved':3, 'Not lost for AM':4,
               'Wonderful':5, 'Revised':6, 'Offered':7, 'Offerable':8}

item_type_values = ['W', 'WI', 'S', 'PL', 'IPL', 'SLAWR', 'Others']

item_type_dict = {'W':5.0, 'WI':6.0, 'S':3.0, 'Others':1.0, 'PL':2.0, 'IPL':0.0, 'SLAWR':4.0}

application_values = [10., 41., 28., 15., 4., 59., 38., 56., 42., 26., 27., 19., 20.,
                      66., 29., 22., 40., 25., 67., 3., 79., 99., 2., 5., 39., 69.,
                      70., 65., 58., 68.]

product_ref_values = [1670798778, 1668701718, 611993, 1668701376, 164141591,
                      628377, 1671863738, 640665, 1332077137, 640405,
                      1693867550, 1665572374, 1282007633, 1668701698, 628117,
                      1690738206, 640400, 1671876026, 628112, 164336407,
                      164337175, 1668701725, 1665572032, 611728, 1721130331,
                      1693867563, 611733, 1690738219, 1722207579, 1665584662,
                      1665584642, 929423819, 1665584320]

# ----------------- Prediction Class -----------------
class Prediction:

    @staticmethod
    def regression():
        with st.form("Regression"):
            col1, col2 = st.columns(2)

            with col1:
                item_date = st.date_input("Item Date", min_value=date(2020,7,1), max_value=date(2021,5,31), value=date(2020,7,1))
                quantity_log = st.text_input("Quantity Tons (Min: 0.00001 & Max: 10000000000)")
                country = st.selectbox("Country", options=country_values)
                item_type = st.selectbox("Item Type", options=item_type_values)
                thickness_log = st.number_input("Thickness", min_value=0.1, max_value=2500000.0, value=1.0)
                product_ref = st.selectbox("Product Ref", options=product_ref_values)

            with col2:
                delivery_date = st.date_input("Delivery Date", min_value=date(2020,8,1), max_value=date(2022,2,28), value=date(2020,8,1))
                customer = st.text_input("Customer ID (Min: 12458000 & Max: 2147484000)")
                status = st.selectbox("Status", options=status_values)
                application = st.number_input("Application", min_value=0.0, max_value=100.0, value=10.0)
                width = st.number_input("Width", min_value=1.0, max_value=2990000.0, value=1.0)

            submitted = st.form_submit_button("Predict Selling Price")
            style_submit_button()

            if submitted:
                with open(r'C:\\Users\\viren\\OneDrive\\Desktop\\IIT-MADARAS(GUVI)\\data\\INDUSTRIAL COPPER MODELING\\pickle\\regression_model.pkl', 'rb') as f:
                    model = pickle.load(f)

                user_data = np.array([[customer, float(country), status_dict[status], item_type_dict[item_type],
                                       application, width, product_ref, np.log(float(quantity_log)),
                                       np.log(float(thickness_log)), item_date.day, item_date.month, item_date.year,
                                       delivery_date.day, delivery_date.month, delivery_date.year]])

                y_pred = model.predict(user_data)
                selling_price = round(np.exp(y_pred[0]), 2)

                style_prediction()
                st.markdown(f'<h3 class="center-text">Predicted Selling Price = {selling_price}</h3>', unsafe_allow_html=True)
                st.balloons()

    @staticmethod
    def classification():
        with st.form("Classification"):
            col1, col2 = st.columns(2)

            with col1:
                item_date = st.date_input("Item Date", min_value=date(2020,7,1), max_value=date(2021,5,31), value=date(2020,7,1))
                quantity_log = st.text_input("Quantity Tons (Min: 0.00001 & Max: 10000000000)")
                country = st.selectbox("Country", options=country_values)
                item_type = st.selectbox("Item Type", options=item_type_values)
                thickness_log = st.number_input("Thickness", min_value=0.1, max_value=2500000.0, value=1.0)
                product_ref = st.selectbox("Product Ref", options=product_ref_values)

            with col2:
                delivery_date = st.date_input("Delivery Date", min_value=date(2020,8,1), max_value=date(2022,2,28), value=date(2020,8,1))
                customer = st.text_input("Customer ID (Min: 12458000 & Max: 2147484000)")
                selling_price_log = st.text_input("Selling Price (Min: 0.1 & Max: 100001000)")
                application = st.number_input("Application", min_value=0.0, max_value=100.0, value=10.0)
                width = st.number_input("Width", min_value=1.0, max_value=2990000.0, value=1.0)

            submitted = st.form_submit_button("Predict Status")
            style_submit_button()

            if submitted:
                with open('C:\\Users\\viren\\OneDrive\\Desktop\\IIT-MADARAS(GUVI)\\data\\INDUSTRIAL COPPER MODELING\\pickle\\classification_model.pkl', 'rb') as f:
                    model = pickle.load(f)

                user_data = np.array([[customer, float(country), item_type_dict[item_type], application,
                                       width, product_ref, np.log(float(quantity_log)),
                                       np.log(float(thickness_log)), np.log(float(selling_price_log)),
                                       item_date.day, item_date.month, item_date.year,
                                       delivery_date.day, delivery_date.month, delivery_date.year]])

                y_pred = model.predict(user_data)
                status_result = y_pred[0]

                style_prediction()
                st.markdown(f'<h3 class="center-text">Predicted Status = {status_result}</h3>', unsafe_allow_html=True)
                st.snow()


# ----------------- Streamlit App -----------------
streamlit_config()

tab1, tab2 = st.tabs(['PREDICT SELLING PRICE', 'PREDICT STATUS'])

with tab1:
    Prediction.regression()

with tab2:
    Prediction.classification()
