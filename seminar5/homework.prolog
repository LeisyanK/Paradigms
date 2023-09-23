% сумма элементов списка
% Rules
len([], 0).
len([X|T], Sum) :-
    len(T, Sum1), Sum is Sum1 + X.

% Query
len([1,2,3,4,5,6,7,8], Sum), write (Sum).