from fastapi import FastAPI, File, UploadFile
import os

app = FastAPI()

# Define the directory to save the uploaded images
UPLOAD_DIRECTORY = "hacked_images"

# Create the directory if it doesn't exist
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Save the file to the specified directory
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_path, "wb") as image:
        image.write(await file.read())

    return {"message": "File uploaded successfully"}

