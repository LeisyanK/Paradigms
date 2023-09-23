% Rules
len([], 0).
len([_|T], Len) :-
    len(T, Len1), Len is Len1 + 1.

% Query
len([1,2,3,4,5,6,7,8], Len), write (Len).