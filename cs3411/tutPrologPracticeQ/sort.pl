 
%Write a predicate isort(List, NewList) that takes a 
%List of numbers in any order, and binds NewList to the
%list containing the same numbers sorted in increasing order. 
%Hint: your predicate should call the insert/3 predicate from part 1.


% Base Case for the very last insertion 
insert(Num, [], [Num]). 

% Base Case 2 inserting in the middle of the array
insert(Num, [Head | Rest], [Num, Head | Rest]) :- 
    Num < Head. 

% Recursive Calls 
insert(Num, [Head | Rest], [Head | NewList]) :-
    insert(Num, Rest, NewList).


% Base case, start with nothing in the array  
isort([], []).


isort([Head | Rest], NewList) :- 
    isort(Rest, Sorted), 
    insert(Head, Sorted, NewList). 


