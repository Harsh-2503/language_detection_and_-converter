from fastapi import APIRouter, Depends, HTTPException
from src.services.lagchain import language_processor
import asyncio
from src.utils.validators.auth import get_current_user

router = APIRouter()

@router.get("/convert")
async def test2(text: str, current_user=Depends(get_current_user)):
    try:
        results = await asyncio.to_thread(language_processor.map_chain.invoke, {"question": text})
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing the request")

