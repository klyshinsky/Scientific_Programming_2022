grammar T3_correct;

@header {
import math

def make_op(stack, op):
    if op == '*': 
        stack[-2] *= stack[-1] 
    elif op == '/':
        stack[-2] /= stack[-1]
    elif op == '+':
        stack[-2] += stack[-1]
    elif op == '-':
        stack[-2] -= stack[-1]

    stack.pop()
    print(op)
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
    : e OP_MUL e 
      {make_op($stat::stack, $OP_MUL.text)
      } # Mult
    | e OP_ADD e 
      {make_op($stat::stack, $OP_ADD.text)
      } # Add
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
OP_ADD: [+-];
OP_MUL: [*/];

