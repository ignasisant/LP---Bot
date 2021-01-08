grammar Skyline;
root : skyline EOF;

skyline : PARO skyline PARC //3
    | MINUS skyline //2
    | skyline MUL skyline
    | skyline MUL NUM
    | skyline MES skyline //3 tots
    | skyline MES NUM
    | skyline MES VAR
    | skyline MINUS NUM
    | VAR IGUAL skyline
    | CORO skyline skyline CORC //4
    | COMA PARO NUM COMA NUM COMA NUM PARC skyline //9
    | PARO NUM COMA NUM COMA NUM PARC //7
    | CLAUDO NUM COMA NUM COMA NUM COMA NUM COMA NUM CLAUDC //11
    | MINUS VAR
    | VAR MUL NUM
    | VAR MES skyline
    | VAR
    | 
    ;

// variableOperations :  
//     | MINUS VAR
//     | VAR MUL NUM
//     | VAR MES skyline
//     | VAR
//     |
//     ;



// createSkyline : PARO NUM COMA NUM COMA NUM PARC
//     | CORO createSkyline altreSkyline CORC
//     | 
//     ;

// altreSkyline : COMA PARO NUM COMA NUM COMA NUM PARC altreSkyline
//     |
//     ;


IGUAL : ':=' ;
VAR : [a-zA-Z]+ ;
COMA : ',' ;
PARO : '(' ;
PARC : ')' ;
CORO : '[' ;
CORC : ']' ;
CLAUDO : '{' ;
CLAUDC : '}' ;
NUM : [0-9]+ ;
MES : '+' ;
MINUS : '-' ;
MUL : '*' ;
WS : [ \n]+ -> skip ;