from fastapi import FastAPI, Path,HTTPException
import json 

app = FastAPI()

def load_data():
    # This function can be used to load data from a database or a file
    with open('patients.json','r') as f:
        data=json.load(f)
        return data
     
@app.get("/")
def hello():
    return {'message': 'Patients Management'}

@app.get('/about')
def about():
    return{'message' : 'This is a simple API for managing patients in a hospital.'}

@app.get('/view')
def view_patients():
    data=load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(..., description='ID of patient in DB',example="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

