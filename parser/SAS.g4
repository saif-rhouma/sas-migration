grammar SAS;

/* =========================
   PARSER RULES
   ========================= */

parse
 : sas_stmt_block* EOF
 ;

sas_stmt_block
 : data_stmt_block
 | proc_stmt_block
 | macro_definition
 | macro_call
 | libname_stmt
 | comment_stmt
 ;

/* =========================
   DATA STEP
   ========================= */

data_stmt_block
 : DATA (ID_NULL | Identifier) ';'
   data_stmt_list*
   RUN ';'
 ;

libname_stmt
 : LIBNAME Identifier (XLSX | STRINGLITERAL)? ';'
 ;

data_stmt_list
 : comment_stmt
 | infile_stmt
 | input_stmt
 | set_stmt
 | merge_stmt
 | by_stmt
 | assignment_stmt
 | if_stmt
 | do_block
 | rename_stmt
 | delete_stmt
 | libname_stmt
 ;

comment_stmt
 : COMMENT
 ;

rename_stmt
 : RENAME name EQ name ';'
 ;

infile_stmt
 : INFILE file_specification infile_options* ';'
 ;

file_specification
 : STRINGLITERAL
 | CARDS
 | DATALINES
 ;

infile_options
 : DELIMITER EQ STRINGLITERAL
 | FIRSTOBS EQ INT
 | OBS EQ INT
 ;

input_stmt
 : INPUT name+ ';'
 ;

set_stmt
 : SET name+ ';'
 ;


condition
 : Identifier comparator value
 ;

value
 : INT
 | STRING
 ;

merge_stmt
 : MERGE name+ ';'
 ;

by_stmt
 : BY name+ ';'
 ;

assignment_stmt
 : name EQ expression ';'
 ;

delete_stmt
 : DELETE ';'
 ;

if_stmt
 : IF expression THEN data_stmt_list
 | IF expression THEN data_stmt_list ELSE data_stmt_list
 ;

do_block
 : DO ';'
   data_stmt_list*
   END ';'
 ;

/* =========================
   PROC BLOCK
   ========================= */

proc_stmt_block
 : PROC proc_name proc_options? ';'
   proc_stmt_list*
   RUN ';'
 ;

proc_name
 : MEANS
 | FREQ
 ;

proc_options
 : DATA EQ name
 ;

proc_stmt_list
 : var_stmt
 | title_stmt
 ;

var_stmt
 : VAR name+ ';'
 ;

title_stmt
 : STRINGLITERAL ';'
 ;
expression
 : relationalExpression
 ;

relationalExpression
 : additiveExpression ( comparator additiveExpression )*
 ;

additiveExpression
 : multiplicativeExpression ( (PLUS | MINUS) multiplicativeExpression )*
 ;

multiplicativeExpression
 : atom ( (STAR | DIV) atom )*
 ;

atom
 : INT
 | STRING
 | STRINGLITERAL
 | Identifier
 | MACRO_VAR
 ;

comparator
 : GT
 | LT
 | GE
 | LE
 | EQ
 | NEQ
 ;

/* =========================
   LEXER RULES
   ========================= */

/* ---- Keywords FIRST ---- */

DATA    : [dD][aA][tT][aA] ;
PROC    : [pP][rR][oO][cC] ;
RUN     : [rR][uU][nN] ;
SET     : [sS][eE][tT] ;
IF      : [iI][fF] ;
MEANS   : [mM][eE][aA][nN][sS] ;
FREQ    : [fF][rR][eE][qQ] ;
VAR     : [vV][aA][rR] ;
INFILE  : [iI][nN][fF][iI][lL][eE] ;
INPUT   : [iI][nN][pP][uU][tT] ;
CARDS   : [cC][aA][rR][dD][sS] ;
DATALINES : [dD][aA][tT][aA][lL][iI][nN][eE][sS] ;
DELIMITER : [dD][eE][lL][iI][mM][iI][tT][eE][rR] ;
FIRSTOBS  : [fF][iI][rR][sS][tT][oO][bB][sS] ;
OBS       : [oO][bB][sS] ;
ID_NULL   : '_null_' ;
MERGE  : [mM][eE][rR][gG][eE] ;
BY     : [bB][yY] ;
DELETE : [dD][eE][lL][eE][tT][eE] ;
DO     : [dD][oO] ;
END    : [eE][nN][dD] ;
THEN   : [tT][hH][eE][nN] ;
ELSE   : [eE][lL][sS][eE] ;
PLUS   : '+' ;
MINUS  : '-' ;
STAR   : '*' ;
DIV    : '/' ;
RENAME : [rR][eE][nN][aA][mM][eE] ;

/* ---- Operators ---- */

GE  : '>=' ;
LE  : '<=' ;
NEQ : '<>' ;
GT  : '>' ;
LT  : '<' ;
EQ  : '=' ;

/* ---- Literals ---- */

STRINGLITERAL
 : '"' (~["\r\n])* '"'
 ;

STRING
 : '\'' (~['\r\n])* '\''
 ;

INT
 : [0-9]+
 ;

/* ---- Identifier LAST ---- */

QuotedIdentifier
 : '\'' (~['\r\n])* '\'' 'n'?
 ;

Identifier
 : [a-zA-Z_][a-zA-Z_0-9]* ('.' [a-zA-Z_][a-zA-Z_0-9]*)*
 ;

/* ---- Comments ---- */

COMMENT
    : LINE_COMMENT
    | BLOCK_COMMENT
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> channel(HIDDEN)
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> channel(HIDDEN)
    ;

/* ---- Whitespace ---- */

WS
 : [ \t\r\n]+ -> skip
 ;

PERCENT : '%' ;
MACRO : [mM][aA][cC][rR][oO] ;
MEND  : [mM][eE][nN][dD] ;
LET   : [lL][eE][tT] ;
PUT   : [pP][uU][tT] ;

LPAREN : '(' ;
RPAREN : ')' ;
COMMA  : ',' ;
SEMI   : ';' ;


/* MACRO PARSER RULES */
macro_definition
 : PERCENT MACRO Identifier LPAREN? parameter_list? RPAREN? ';'
   macro_body*
   PERCENT MEND Identifier? ';'
 ;

macro_call
 : PERCENT Identifier LPAREN? argument_list? RPAREN? ';'
 ;

macro_body
 : ~(PERCENT | MEND)
 ;

parameter_list
 : Identifier (COMMA Identifier)*
 ;

argument_list
 : expression (COMMA expression)*
 ;

MACRO_VAR
 : '&' [a-zA-Z_][a-zA-Z_0-9]* '.'?
 ;

name
 : Identifier
 | MACRO_VAR
 | QuotedIdentifier
 ;