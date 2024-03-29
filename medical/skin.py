import pickle
from django.http import JsonResponse
from sklearn.preprocessing import LabelEncoder
import pandas as pd
def skin_data(problem,location,gender):
     sex=gender
     symptoms=problem
     location=location
     df=pd.read_csv("C:/MedTech_DJ_Backend/med_backend/Dataset/Skin Disease.csv")
     le_sex=LabelEncoder()
     le_symp=LabelEncoder()
     le_his=LabelEncoder()
     le_sex = LabelEncoder().fit(df['Sex'].unique())
     le_symp = LabelEncoder().fit(df['Skin Problem'].unique())
     le_his = LabelEncoder().fit(df['Location on Body'].unique())

    # Now you can transform single inputs
     scaled_sex = le_sex.transform([gender])
     scaled_symptoms = le_symp.transform([problem])
     scaled_history = le_his.transform([location])

     print(scaled_sex[0])
     print(scaled_symptoms[0])
     print(scaled_history[0])
     se=[]
     se.append(sex)
     symp=[]
     symp.append(symptoms)
     his=[]
     his.append(location)
     print(se)
     print(symp)
     print(his)
   #   scaled_sex=le_sex.transform(se)
   #   scaled_symptoms=le_symp.transform(symp)
   #   scaled_history=le_his.transform(his)
   #   print(scaled_sex[0])
   #   print(scaled_symptoms[0])
   #   print(scaled_history[0])
     res=df[(df["Skin Problem"].str.contains(symp[0])) & (df["Location on Body"].str.contains(his[0])) & (df["Sex"] == se[0]) ]
     print(res)
     with open("C:/MedTech_DJ_Backend/med_backend/medical/skin_model.pkl","rb") as f:
        model=pickle.load(f,encoding='utf-8')
     print(model)
     predictions=model.predict([[scaled_sex[0],scaled_symptoms[0],scaled_history[0]]])
     print("Predictions is: ",predictions)
   #   return JsonResponse({"message":"Hello from the backend"})
     return predictions[0]