/* Write a predicate merge(Sort1, Sort2, Sort) which 
takes two lists Sort1 and Sort2 that are already sorted 
in increasing order, and binds Sort to a new list which
 combines the elements from Sort1 and Sort2 , and is sorted
in increasing order. */


merge([], [], []). 
merge([], B, B). 
merge(A, [], A).  

merge([H1 | T1], [H2 | T2], [H2 | SortedList]) :- 
    H1 > H2, 
    merge([H1 |T1], T2, SortedList).

merge([H1 | T1], [H2 | T2], [H1 | SortedList]) :- 
    H2 > H1, 
    merge(T1, [H2 | T2], SortedList).
