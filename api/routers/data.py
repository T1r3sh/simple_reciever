from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status

from api.core.auth import get_current_user
from api.models.schemas import DataPayload, DataResponse
from api.utils.file_handler import file_handler
from api.core.config import settings

router = APIRouter()


@router.put("/ingest", response_model=DataResponse)
async def ingest_data(payload: DataPayload, _: None = Depends(get_current_user)):
    """
    Вставка данных

    Необходима Bearer token аутентификация.
    """
    try:
        # Save the data
        data = {"body": payload.body}
        file_handler.save_data(data)

        return DataResponse(message="Success", timestamp=datetime.now())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to save data: {str(e)}",
        )
