from pydantic import BaseModel


class VoteRequest(BaseModel):
    ballot_id: int
    choice: int


class VoteResponse(BaseModel):
    ballot_id: int
    user_id: int
    choice: int
