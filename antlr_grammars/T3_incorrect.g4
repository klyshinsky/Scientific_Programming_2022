grammar T3_incorrect;

@header {
import math
}
 
@members {
res = ""
}

// Rule stat.
stat locals [stack=[]]    :
          'return ' e ';' 
          {print("calculated:", $stack)} # Return
 	| 'break' ';' # Break
 	;

// Rule e.
e   
@after{print("processed", $stat::stack);}
    : e '*' e 
      {$stat::stack[-2]*=$stat::stack[-1]; $stat::stack.pop(); print("*"); 
      } # Mult
    | e '/' e 
      {$stat::stack[-2]/=$stat::stack[-1]; $stat::stack.pop(); print("/"); 
      } # Div
    | e '+' e 
      {$stat::stack[-2]+=$stat::stack[-1]; $stat::stack.pop(); print("+"); 
      } # Add
    | e '-' e 
      {$stat::stack[-2]-=$stat::stack[-1]; $stat::stack.pop(); print("-|"); 
      } # Sub
    | 'pow(' INT {a=int($INT.text)} ',' INT {b=int($INT.text)} ')'
      {
$stat::stack.append(math.pow(a,b)); print("pow"); 
      } # Pow
    | INT 
      {
self.res+=$text; 
$stat::stack.append(int($text)); 
print("->", $stat::stack)
      } # Int
    | ID # Id
    | '(' e ')' # Braced
    ;

// Lexer rules after.
INT: [0-9]+;
ID: [a-zA-Z][a-zA-Z0-9]*;
WS : [ \r\t\n]+ ;

