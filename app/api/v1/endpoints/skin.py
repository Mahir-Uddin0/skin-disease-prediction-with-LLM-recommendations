from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pipeline import analyze_skin
from app.schemas.response import SkinAnalysisResponse

router = APIRouter()


@router.post("/analyze", response_model=SkinAnalysisResponse)
async def analyze_skin_endpoint(file: UploadFile = File(...)):
    try:
        contents = await file.read()

        result = analyze_skin(contents)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))