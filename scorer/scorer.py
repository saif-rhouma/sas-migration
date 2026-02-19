def compute_score(sas_code):
    score = 100
    if "%macro" in sas_code.lower():
        score -= 20
    if "merge" in sas_code.lower():
        score -= 15
    return max(score, 0)