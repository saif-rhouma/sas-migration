import requests

def refine_code(sas_code, ir_json, python_code):
    prompt = f"""
You are a SAS-to-Python migration expert.

SAS Code:
{sas_code}

Intermediate Representation:
{ir_json}

Generated Python Code:
{python_code}

Improve the Python code:
- Make it idiomatic pandas
- Add helpful comments
- Do not change logic
Return only the improved Python code.
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )
    return response.json()["response"]
