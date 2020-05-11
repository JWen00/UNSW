/*
Write a prolog predicate insert(Num, List, NewList)
that takes a number Num along with a list of numbers 
List which is already sorted in increasing order, 
and binds NewList to the list obtained by inserting 
Num into List so that the resulting list is still 
sorted in increasing order.
*/

% Base Case for the very last insertion 
insert(Num, [], [Num]). 

% Base Case 2 inserting in the middle of the array
insert(Num, [Head | Rest], [Num, Head | Rest]) :- 
    Num < Head. 

% Recursive Calls 
insert(Num, [Head | Rest], [Head | NewList]) :-
    insert(Num, Rest, NewList).

