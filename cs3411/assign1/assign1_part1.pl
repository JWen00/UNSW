% cs3411 Assignment 1 Part 1
% Written By Jennifer Wen Xu (z5207930) 

% 1.1 
sqEven(Num, NumSq) :-
    0 is Num mod 2,
    NumSq is Num * Num.

sqEven(Num, NumSq) :-
    1 is Num mod 2,
    NumSq is 0.

sumsq_even([], 0).
sumsq_even([H | R], Sum) :-
    sumsq_even(R, NewSum),
    sqEven(H, NumSq),
    Sum is NewSum + NumSq.


% 1.2
getLog(N, Pair):- 
    Log is log(N), 
    Pair = [N, Log]. 

log_table([], []).  
log_table([H | R], [P | Result]):- 
    log_table(R, Result), 
    getLog(H, P).


% 1.3
process(N, [], [[N]]).

process(N, [[A | B] | Rest], Output):- 
    N mod 2 =:= A mod 2, 
    Output = [[N | [A | B]] | Rest].

process(N, [[A | B] | Rest], Output):- 
    not(N mod 2 =:= A mod 2), 
    Output = [[N], [A | B] | Rest].  

paruns([], []). 

paruns([H | R], Result):- 
    paruns(R, TmpResult), 
    process(H, TmpResult, Result). 


%1.4 
eval(Expr, Expr):- 
    number(Expr).

eval(mul(Expr1, Expr2), V):-
    eval(Expr1, R1),
    eval(Expr2, R2), 
    V is R1 * R2.


% This code assumes we will not encounter divition by 0 error. 
eval(div(Expr1, Expr2), V):-
    eval(Expr1, R1),
    eval(Expr2, R2), 
    V is R1 / R2.


eval(add(Expr1, Expr2), V):-
    eval(Expr1, R1),
    eval(Expr2, R2), 
    V is R1 + R2.

eval(sub(Expr1, Expr2), V):-
    eval(Expr1, R1),
    eval(Expr2, R2), 
    V is R1 - R2.



    

