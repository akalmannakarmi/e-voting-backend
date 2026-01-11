from fastapi import FastAPI

from internal.voting.api import router as vote_router

app = FastAPI(title="Vote Service")

app.include_router(vote_router)


@app.get("/health")
def health():
    return {"status": "ok"}
