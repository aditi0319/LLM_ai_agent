from fastapi import APIRouter, HTTPException
from app.services.classifier import ask_ai

router = APIRouter(prefix="/api", tags=["AI Agent"])

@router.post("/ask")
def ask_question(question: str):
    """
    Ask the AI Agent about stored GitHub issues.
    Example: "Which issue was created most recently?"
    """
    try:
        answer = ask_ai(question)
        return {"question": question, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
