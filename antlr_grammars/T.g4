grammar T;

stat: 'return ' e ';' # Return
 	| 'break' ';' # Break
 	;
e   : e '*' e # Mult
    | e '+' e # Add
    | INT # Int
    | ID # Id
    ;

WS : [ \r\t\n]+ ;
INT: [0-9]+;
ID: [a-zA-Z][a-zA-Z0-9]*;

