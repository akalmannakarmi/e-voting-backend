from sqlalchemy import Column, Integer, UniqueConstraint
from sqlalchemy.orm import Session

from internal.shared.db import Base


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True)
    ballot_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    choice = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint("ballot_id", "user_id", name="uq_ballot_user"),
    )


class VoteRepo:
    def __init__(self, db: Session):
        self.db = db

    def has_voted(self, ballot_id: int, user_id: int) -> bool:
        return (
            self.db.query(Vote)
            .filter(Vote.ballot_id == ballot_id, Vote.user_id == user_id)
            .first()
            is not None
        )

    def create_vote(self, ballot_id: int, user_id: int, choice: int):
        vote = Vote(
            ballot_id=ballot_id,
            user_id=user_id,
            choice=choice,
        )
        self.db.add(vote)
        self.db.commit()
        return vote
