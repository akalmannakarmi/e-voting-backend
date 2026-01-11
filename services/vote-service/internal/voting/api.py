from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from internal.shared.db import get_db
from internal.shared.dependencies import get_current_user
from .service import VoteService
from .schemas import VoteRequest, VoteResponse

router = APIRouter(prefix="/votes", tags=["votes"])


@router.post("/", response_model=VoteResponse)
def vote(
    req: VoteRequest,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    service = VoteService(db)
    try:
        vote = service.cast_vote(
            req.ballot_id,
            user_id,
            req.choice,
        )
        return vote
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
