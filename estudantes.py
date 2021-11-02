import numpy as np
import joblib
import streamlit as st

st.markdown("By Eric Oliveira  [LinkedIn](https://www.linkedin.com/in/eric-oliveira-ds) ")

model = open("modelo.sav", "rb")
model = joblib.load(model)

def ridge_pred(var1, var2, var3):

    pred_arr = np.array([var1, var2, var3])
    preds = pred_arr.reshape(1,-1)
    model_prediction = model.predict(preds)
    return model_prediction

def run():

    st.title("Como meu aluno se sairá no 3º ano letivo ?")
    st.markdown("Apenas por diversão!")
    html_temp = """
    """

    st.markdown(html_temp)

    var1 = st.selectbox("Cursa português bem (1) ou matemática bem (0) ?",{0:'math',1:'portuguese'})
    var2 = st.slider("Nota do 1º ano ?", min_value=0, max_value=40, value=40)
    var3 = st.slider("Nota do 2º ano ?", min_value=0, max_value=40, value=40)
    
    prediction = " "

    if st.button("Prever"):
        prediction = ridge_pred(var1,var2,var3)
        st.success("A previsão da nota é : %d"% prediction)

if __name__=='__main__':
    run()





