/* Write a predicate mergesort(List, NewList)
 which has the same functionality as the isort/2 predicate
  from part 2 above, but uses the MergeSort algorithm. 
  Hint: you will need to use the split/3 and merge/3 
  predicates from parts 3 and 4 above. */ 

insert(Num, [], [Num]).
insert(Num, [H | R], [Num, H | R]) :- 
    Num < H. 
insert(Num, [H | R], [H | NewList]) :-
    insert(Num, R, NewList).


isort([], []).
isort([H | R], NewList) :- 
    isort(R, Sorted), 
    insert(H, Sorted, NewList). 

split([], [], []).
split([A], [A], []).
split([H1 | [H2 | T]], [H1 | List1], [H2 | List2]) :-
    split(T, List1, List2).
 

merge([], [], []). 
merge([], B, B). 
merge(A, [], A).  

merge([H1 | T1], [H2 | T2], [H2 | SortedList]) :- 
    H1 > H2, 
    merge([H1 |T1], T2, SortedList).

merge([H1 | T1], [H2 | T2], [H1 | SortedList]) :- 
    H2 > H1, 
    merge(T1, [H2 | T2], SortedList).

mergeSort([], []). 
mergeSort([X], [X]). 

mergeSort(List, SortedList) :- 
    split(List, A, B),
    mergeSort(A, SortedA), 
    mergeSort(B, SortedB),
    merge(SortedA, SortedB, SortedList).
    


    
