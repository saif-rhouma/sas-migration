from fastapi import FastAPI, File, UploadFile
from parser.generated.SASLexer import SASLexer
from parser.generated.SASParser import SASParser
from parser.visitor import IRVisitor
from compiler.compiler import compile_program
from ai.refiner import refine_code
from scorer.scorer import compute_score
from antlr4 import InputStream, CommonTokenStream
from metrics.metrics import (
    count_total_codes,
    count_total_lines,
    count_egps,
    compute_complexity_metrics,
    count_data_tables,
    count_hardcoded_paths,
    analyze_data_dependencies
)
# import json
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


# Allow React frontend origin
origins = [
    "http://localhost:8080",  # React dev server
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],         # GET, POST, PUT, DELETE…
    allow_headers=["*"],         # Accept all headers
)

@app.post("/convert-file")
async def convert_file(file: UploadFile = File(...)):
    sas_code = (await file.read()).decode("utf-8")

    # ANTLR Lexer + Parser
    input_stream = InputStream(sas_code)
    lexer = SASLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()  # 🔥 IMPORTANT — load all tokens

    # Extract comments BEFORE parsing
    all_tokens = stream.tokens
    comments = []

    for t in all_tokens:
        if t.type in [SASLexer.COMMENT, SASLexer.LINE_COMMENT]:
            comments.append({
                "text": t.text.strip(),
                "token_index": t.tokenIndex  # <-- add this
            })

    parser = SASParser(stream)
    tree = parser.parse()  # 'program' is usually the root rule

    # AST → IR
    visitor = IRVisitor(token_stream=stream, comments=comments)
    ir_nodes = visitor.visit(tree)

    program = ir_nodes


    # Metrics:
    total_codes = count_total_codes(program)
    total_lines = count_total_lines(sas_code)
    total_egps = count_egps(program)
    complexity_metrics = compute_complexity_metrics(program)

    data_tables = count_data_tables(program)
    hardcoded_paths = count_hardcoded_paths(sas_code)

    dependency_metrics = analyze_data_dependencies(program, sas_code)
   
    # Deterministic compiler
    draft = compile_program(ir_nodes)

    # AI refinement
    # refined = refine_code(sas_code, json.dumps([n.dict() for n in ir_nodes]), draft)

    # Confidence scoring
    score = compute_score(sas_code)

    return {
        "filename": file.filename,
        "original_sas": sas_code,
        "draft_python": draft,
        # "refined_python": refined,
        "confidence_score": score,
        "metrics": {
            "total_codes": total_codes,
            "total_lines": total_lines,
            "total_egps": total_egps,
            "average_complexity": complexity_metrics["average_complexity"],
            "code_complexity": complexity_metrics["code_complexity"],
            "complexity_distribution": complexity_metrics["distribution"],
            "data_tables": data_tables,
            "hardcoded_paths": hardcoded_paths,
            "dependency_by_type": dependency_metrics
        }
    }
