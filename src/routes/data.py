from fastapi import FastAPI, APIRouter, Depends, UploadFile
from Helpers.config import get_settings, Settings
from Controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,app_settings : Settings = Depends(get_settings)):
    # validate the file properties
    data_controller = DataController()

    is_valid = data_controller.validate_uploaded_file(file=file)
    return is_valid