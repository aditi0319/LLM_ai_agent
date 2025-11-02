from fastapi import APIRouter
from pydantic import BaseModel
from app.services.classifier import TicketClassifier
from app.services.response_generator import generate_solution  # 👈 Import your HuggingFace function

router = APIRouter(prefix="/tickets", tags=["Tickets"])

classifier = TicketClassifier()

class TicketQuery(BaseModel):
    query: str

@router.get("/health")
def health_check():
    return {"status": "ok", "message": "Ticket routes are active!"}

@router.post("/classify")
def classify_ticket(request: TicketQuery):
    query = request.query

    # Step 1: Predict the category
    category = classifier.predict(query)
    

    # Step 2: Generate a solution from Hugging Face model
    solution = generate_solution(category, query)
    

    # Step 3: Return both
    return {
        "query": query,
        "predicted_category": category,
        "solution": solution
    }
