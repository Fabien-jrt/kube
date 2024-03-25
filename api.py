from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import json
import sqlite3

app = FastAPI()
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS data (medication_intake_id INTEGER PRIMARY KEY AUTOINCREMENT, patient_id TEXT, medication TEXT, taken_at TEXT)')
conn.commit()
conn.close()


@app.get("/")
async def root():
    return {
        "routes": 
            {
                "/": "This route, useless, just for documentation",
                "/json_upload": "Post json data (post only)",
                "/docs": "Swagger UI",
                "/redoc": "Redoc UI"
            },
            "data_format":
                {
	            "patient_id": "8ac774aa-4f04-4ea5-83b5-296af7364be3",
	            "medication" : "microxidanol",
	            "taken_at": "2023-05-26T06:29:53Z"
                },
            "tips": "Use /docs or /redoc for better documentation. Use /docs and select the /json_upload route to see the json upload form."
        }

@app.post("/json_upload/")
async def json_upload_data(file: UploadFile):
    content = await file.read()
    data = json.loads(content)
    print(f"""Inserting the following data: 
          {data}""")

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    for med in data:
        cursor.execute('INSERT INTO data (patient_id, medication, taken_at) VALUES (?, ?, ?)', (med['patient_id'], med['medication'], med['taken_at']))
        conn.commit()
    conn.close()

    return JSONResponse(content={"message": "Data inserted into SQLite database"})

@app.get("/all_data/")
async def get_all_data(skip: int = 0, limit: int = 10):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    # execute the query with pagination
    cursor.execute('SELECT * FROM data LIMIT ? OFFSET ?', (limit, skip))
    data = cursor.fetchall()
    conn.close()
    return data

@app.get("/data/{id}")
async def get_by_id(id: str):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data WHERE medication_intake_id = ?', (id))
    data = cursor.fetchall()
    conn.close()
    return data
