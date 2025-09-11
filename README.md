# 🏭 Industrial Copper Modeling – Streamlit Web App  

## 📌 Project Overview  
The copper industry often faces challenges in:  
- Predicting **sales prices** due to skewed, noisy, and outlier-heavy data  
- Identifying which **sales leads** are likely to convert  

This project addresses these challenges by building **two machine learning models** and deploying them through a **Streamlit web application**:  
- **Regression Model** → Predicts the continuous variable *Selling Price*  
- **Classification Model** → Predicts *Lead Status* (WON/LOST)  

---

## ⚙️ Workflow  
### 1. **Data Preprocessing**  
- Cleaning missing & inconsistent values  
- Handling skewness in distributions  
- Treating outliers  
- Applying feature scaling  

### 2. **Model Development**  
- **Regression Models Tested:** Linear Regression, Random Forest, XGBoost  
  - ✅ *Random Forest achieved the best accuracy for price prediction*  
- **Classification Models Tested:** Multiple classifiers with restricted STATUS (WON/LOST)  
  - ✅ *XGBoost achieved the highest accuracy and balanced performance*  

### 3. **Deployment with Streamlit**  
The models were integrated into a user-friendly Streamlit app where:  
- Users input sales order details  
- Instantly receive predictions for **Selling Price** or **Lead Status**  

---

## 🖥️ App Features  
- **Two Tabs:**  
  - Predict Selling Price  
  - Predict Lead Status (WON/LOST)  
- **Custom Styling:**  
  - Transparent header  
  - Styled submit buttons  
  - Predictions displayed in **green text**  
  - 🎈 Balloons animation for price prediction  
  - ❄️ Snow animation for status prediction  

---

## 📊 Input Options  

### 🔹 Regression (Selling Price Prediction)  
- Item Date & Delivery Date  
- Quantity (Tons)  
- Country *(dropdown)*  
- Customer ID  
- Status *(dropdown)*  
- Application *(numeric)*  
- Item Type *(dropdown)*  
- Product Reference *(dropdown)*  
- Width & Thickness  

### 🔹 Classification (Lead Status Prediction)  
- Item Date & Delivery Date  
- Quantity (Tons)  
- Country *(dropdown)*  
- Customer ID  
- Selling Price  
- Application *(numeric)*  
- Item Type *(dropdown)*  
- Product Reference *(dropdown)*  
- Width & Thickness  

---

## 🚀 How to Run the App  

1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/industrial-copper-modeling.git
   cd industrial-copper-modeling

