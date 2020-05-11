/* Write a predicate split(BigList, List1, List2) 
which takes a list BigList and divides the items into 
two smaller lists List1 and List2 , as evenly as possible
 (i.e. so that the number of items in List1 and List2 
 differs by no more that 1). Can it be done without measuring 
 the length of the list? */

% Even number in the list 
split([], [], []).

% Odd numer in the list 
split([A], [A], []).

% Recursive call
split([Head1 | [Head2 | Tail]], [Head1 | List1], [Head2 | List2]) :-
    split(Tail, List1, List2).
