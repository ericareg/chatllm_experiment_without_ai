from __future__ import annotations

from pydantic import BaseModel, Field


class InstructionsUpdate(BaseModel):
    instructions: str = Field(default="", max_length=8000)


class InstructionsResponse(BaseModel):
    instructions: str
    is_default: bool