from fastapi import FastAPI
from app.config import settings
from app.models import ContractAnalysisRequest, ContractReport, RiskClause
from app.services.contract_engine import evaluate_contract

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/analyze-contract", response_model=ContractReport)
def analyze(req: ContractAnalysisRequest):
    risk, clauses_raw, disc = evaluate_contract(req.contract_title, req.contract_text)
    clauses = [RiskClause(**c) for c in clauses_raw]
    return ContractReport(
        contract_title=req.contract_title,
        overall_risk_score=risk,
        key_clauses=clauses,
        disclaimer=disc
    )
