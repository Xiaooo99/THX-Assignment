#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib
model = joblib.load("XGBoost.joblib")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        print(income, age, loan)
        model = joblib.load("XGBoost.joblib")
        pred = model.predict([[float(income), float(age), float(loan)]])
        print(pred)
        pred= pred[0]
        s= "The predicted default is " + str(pred)
        
        
        return(render_template("index.html", result =s))
    else: 
        return(render_template("index.html", result = "Predict 1"))

        return(render_template("index.html", result = "Predict 1"))


# In[ ]:


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1111)


# In[ ]:




