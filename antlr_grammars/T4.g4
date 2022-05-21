grammar T4;

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
values = {}
}

// Rule start.
start:
      (decl | a_expr)+
;

// Rule decl.
decl:
      'int' ID {self.values[$ID.text]=0} (',' ID {self.values[$ID.text]=0} )* ';' WS*
{print('delcared', $text)
}   
;

// Rule a_expr.
a_expr locals [stack=[]]    :
      ID {if $ID.text not in self.values.keys(): print(f"wasn't declared:{$ID.text}")} '=' e ';' WS*
      {print("calculated:", $stack);self.values[$ID.text]=$stack[-1];} # Return
    | 'break' ';' # Break
;

// Rule e.
e   
@after{print("processed", $a_expr::stack);}
    : e OP_MUL e 
      {make_op($a_expr::stack, $OP_MUL.text)
      } # Mult
    | e OP_ADD e 
      {make_op($a_expr::stack, $OP_ADD.text)
      } # Add
    | 'pow(' INT {a=int($INT.text)} ',' INT {b=int($INT.text)} ')'
      {
$a_expr::stack.append(math.pow(a,b)); print("pow"); 
      } # Pow
    | INT 
      {
$a_expr::stack.append(int($text)); 
print("->", $a_expr::stack)
      } # Int
    | ID 
       {
if $ID.text not in self.values.keys(): print(f"wasn't declared:{$ID.text}")
else: $a_expr::stack.append(self.values[$text]); 
       } # Id
    | '(' e ')' # Braced
    ;

// Lexer rules after.
INT: [0-9]+;
ID: [a-zA-Z][a-zA-Z0-9]*;
WS : [ \r\t\n]+ ;
OP_ADD: [+-];
OP_MUL: [*/];

