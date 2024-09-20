from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from sklearn.cluster import KMeans
import random

app = FastAPI()

#adding CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# loaded_model = joblib.load('models/academicperformanceprediction.pkl')

class feature(BaseModel):
    features:conlist(float, min_length = 5, max_length = 5)

@app.post('/group')
def predict():
# def predict(data: feature):
    try:
        data = pd.read_csv('data/data.csv')
        kmeans = KMeans(n_clusters = 4, random_state = 42)

        skillset = ['Coding','Leadership', 'Communication Skill', 'Presentation designing']

        kmeans.fit(data[[x for x in skillset]])

        data['cluster'] = kmeans.labels_

        dataframes = {}

        for x in data['cluster'].unique().tolist():
            dataframes[f'data_{x}'] = data[data['cluster'] == x]

        smallest_dataset_name = min(dataframes, key=lambda k: len(dataframes[k]))

        group = {}
        minvalue = len(dataframes[smallest_dataset_name])

        for y in range(minvalue):
            singlegroup = []
            for x in dataframes.keys():
                if len(dataframes[x]) > 0:
                    item = random.randint(0, len(dataframes[x])-1)
                
                    singlegroup.append(dataframes[x].iloc[item].to_dict())
                    dataframes[x] = dataframes[x].drop(dataframes[x].index[item]).reset_index(drop=True)
                else:
                    singlegroup.append(0)

            group[y] = singlegroup


        return group
        #getting standardscaled value from scaler
        # scaler = joblib.load('models/scaler.pkl')
        # features = np.array(data.features).reshape(1, -1)
        # features_reshape = scaler.transform(features)
        # prediction = loaded_model.predict(features_reshape)
        # return (int(prediction))
    except Exception as e:
        return HTTPException(status_code = 500, detail = str(e))