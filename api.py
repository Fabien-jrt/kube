from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"routes": 
            {
                "/": "This route, useless, just for documentation",
                "/json_upload": "Post json data (post only)",
                "/docs": "Swagger UI",
                "/redoc": "Redoc UI"
            },
            "tips": "Use /docs or /redoc for better documentation. Use /docs and select the /json_upload route to see the json upload form."
        }

@app.post("/json_upload/")
async def json_upload_data(file: UploadFile):
    return {"filename": file.filename}