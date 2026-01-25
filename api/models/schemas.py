from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, Dict, Optional


class DataPayload(BaseModel):
    """Schema for incoming data payload."""

    body: str = Field(..., description="The main data content", min_length=1)


class DataResponse(BaseModel):
    """Schema for data ingestion response."""

    message: str
    timestamp: datetime


class ErrorResponse(BaseModel):
    """Schema for error responses."""

    detail: str
    timestamp: datetime
