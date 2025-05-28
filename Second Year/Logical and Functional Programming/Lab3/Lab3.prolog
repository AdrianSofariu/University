/*Generate all permutation of N (N - given) respecting the property: for every 2<=i<=n exists an 1<=j<=i,
so |v(i)-v(j)|=1.*/


% Generate numbers from Low to High in a list
% generate_numbers(Low: integer, High: integer, L: list)
%(i, i, o) deterministic

%generate_numbers(low, high) = [] if low > high
%                              = low + generate_numbers(low+1, high) otherwise
generate_numbers(Low, High, [Low | Rest]) :-
    Low =< High,
    !,
    Next is Low + 1,
    generate_numbers(Next, High, Rest).
generate_numbers(Low, High, []) :-
    Low > High.


%% Select a number from the list
% select_num(L: list, Selected: integer, Rest: list)
%(i, o, o) non-deterministic
select_num([H | T], H, T).
select_num([H | T], Selected, [H | Rest]) :-
    select_num(T, Selected, Rest).

%abs difference
%abs(X: integer, Y: integer)
%(i, i) deterministic
%(i, o) deterministic

%abs(X) = X if X >= 0
%         = -X otherwise
abs(X, X) :- X >= 0, !.
abs(X, Y) :- Y is -X.

%check that for a given number there is one in the list that has the abs difference of 1
%exists(X: integer, L: list)
%(i, i) non-deterministic

%exists(X, L1..Ln) = true if |X - L1| = 1
%                  = exists(X, L2..Ln) otherwise
exists(X, [H|_]) :- 
    D is X-H,
    abs(D, 1), 
    !.
exists(X, [_|T]) :-
    exists(X, T).

%predicate that checks the validity of the property that for every 2<=i<=n exists an 1<=j<=i, so |v(i)-v(j)|=1
%check(Curr: integer, Remaining: list, Col: list)
%(i, i, i) deterministic

%check(Curr, L1..Ln, Col) = true if exists(Curr, Col) and check(L2..Ln, [Curr | Col])
%                          = false otherwise
check(_, [], _).
check(Curr, [Next | Rest], Col):-
    exists(Curr, Col),
    check(Next, Rest, [Next | Col]).


%validity check for the permutation (wrapper)
%validity(L: list)
%(i) deterministic
validity([_]).
validity([H1, H2|T]):-
    check(H2, T, [H2, H1]).

%predicate to generate permutations
%permute_and_check(L: list, Col: list, Perm: list)
%(i, i, o) non-deterministic

%permute_and_check(L, Col) = Col if L = []
%                           = permute_and_check(L1..Ln - Lk, E + Col) where Lk = select_num(L) otherwise
permute_and_check([], Col, Perm):-
    validity(Col),
    Perm = Col.
permute_and_check(L, Col, Perm):-
    select_num(L, E, Rest),
    permute_and_check(Rest, [E | Col], Perm).


%wrapper for the permutation
%permutation(N: integer, L: list)
%(i, o) non-deterministic
permutation(N, Res):-
    generate_numbers(1, N, L),
    findall(R, permute_and_check(L, [], R), Res).





