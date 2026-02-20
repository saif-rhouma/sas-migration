from dataclasses import dataclass, field
from typing import List, Union
# Base expression for filters, assignments, etc.
@dataclass
class Expression:
    expr: str  # raw SAS expression


class Comment:
    def __init__(self, text, token_index):
        self.text = text
        self.token_index = token_index

class Expr:
    def __init__(self, expr: str):
        self.expr = expr

class IRNode:
    def __init__(self, token_index=None):
        self.token_index = token_index
# Assignments inside DATA step
@dataclass
class Assignment:
    def __init__(self, target, expr, token_index=None):
        self.target = target
        self.expr = expr
        self.token_index = token_index

# IF / DO blocks
@dataclass
class IfBlock:
    def __init__(self, condition, body=None, else_body=None, token_index=None):
        self.condition = condition
        self.body = body or []
        self.else_body = else_body or []
        self.token_index = token_index

@dataclass
class DoBlock:
    def __init__(self, statements=None, token_index=None):
        self.statements = statements or []
        self.token_index = token_index


# Merge or SET operations
@dataclass
class Merge:
    def __init__(self, datasets, by=None, token_index=None):
        self.datasets = datasets
        self.by = by or []
        self.token_index = token_index

@dataclass
class Set:
    def __init__(self, dataset, token_index=None):
        self.dataset = dataset
        self.token_index = token_index

# DATA step now holds a list of operations
@dataclass
class DataStep:
    def __init__(self, target, operations=None, token_index=None):
        self.target = target
        self.operations = operations or []
        self.token_index = token_index

# PROC steps
@dataclass
class ProcMeans:
    dataset: str
    variables: List[str] = field(default_factory=list)

@dataclass
class ProcFreq:
    dataset: str

@dataclass
class SQLCreateTable:
    table: str
    source_tables: List[str] = field(default_factory=list)

@dataclass
class ProcSQL:
    statements: List[SQLCreateTable] = field(default_factory=list)

# Full program
@dataclass
class Program:
    steps: List[Union[DataStep, ProcMeans, ProcFreq, ProcSQL]] = field(default_factory=list)



