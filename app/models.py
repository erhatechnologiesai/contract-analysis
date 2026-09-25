from pydantic import BaseModel
from typing import List, Dict

class ContractAnalysisRequest(BaseModel):
    contract_title: str
    contract_text: str

class RiskClause(BaseModel):
    clause_name: str
    risk_level: str # LOW, MEDIUM, HIGH
    summary: str
    recommendation: str

class ContractReport(BaseModel):
    contract_title: str
    overall_risk_score: str
    key_clauses: List[RiskClause]
    disclaimer: str
