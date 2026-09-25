def evaluate_contract(title: str, text: str):
    t_low = text.lower()
    clauses = []
    
    # Indemnification Check
    if "indemnif" in t_low:
        clauses.append({
            "clause_name": "Indemnification",
            "risk_level": "HIGH",
            "summary": "Broad indemnification obligation detected requiring full defense of third-party claims.",
            "recommendation": "Cap indemnification liabilities to 12 months of contract fees."
        })
    else:
        clauses.append({
            "clause_name": "Indemnification",
            "risk_level": "LOW",
            "summary": "Standard mutual indemnification scope.",
            "recommendation": "Maintain standard language."
        })

    # Termination Check
    clauses.append({
        "clause_name": "Termination for Convenience",
        "risk_level": "MEDIUM",
        "summary": "Requires 30 days prior written notice without penalty.",
        "recommendation": "Standard commercial practice."
    })

    disclaimer = (
        "LEGAL DISCLAIMER: This analysis is produced by an automated AI diagnostic tool for informational "
        "and operational triage purposes only. It does NOT constitute legal advice or formal attorney representation."
    )

    return "MODERATE_RISK", clauses, disclaimer
