%9. 
%a. For a list of integer number, write a predicate to add in list after 1-st, 3-rd, 7-th, 15-th element a given value e.

%predicates to define correct positions
ok_pos(1).
ok_pos(3).
ok_pos(7).
ok_pos(15).

% wrapper function for add_elem
%add_elem_wrapper(L: list, E: integer, R: list)
%flow model: (i, i, o) - deterministic
add_elem_wrapper(L, E, R):-
    add_elem(L, E, 1, R).

%add_elem(L: list, E: integer, P: integer, R: list)
%flow model: (i, i, i, o) - deterministic

%add_elem(L1..Ln, E, P) = [] if L = []
%                                = L1 + E + add_elem(L2..Ln, E, P + 1) if ok_pos(P)
%                                = L1 + add_elem(L2..Ln, E, P + 1) otherwise
add_elem([], _, _, []).
add_elem([H|T], E, P, [H, E | R]):-
    ok_pos(P),
    !,
    P1 is P+1,
    add_elem(T, E, P1, R).
add_elem([H|T], E, P, [H|R]):-
    P1 is P+1,
    add_elem(T, E, P1, R).


/*b. For a heterogeneous list, formed from integer numbers and list of numbers; add in every sublist after 1-st, 
3-rd, 7-th, 15-th element the value found before the sublist in the heterogenous list. The list has the particularity 
that starts with a number and there aren’t two consecutive elements lists.
Eg.: [1, [2, 3], 7, [4, 1, 4], 3, 6, [7, 5, 1, 3, 9, 8, 2, 7], 5] =>
[1, [2, 1, 3], 7, [4, 7, 1, 4, 7], 3, 6, [7, 6, 5, 1, 6, 3, 9, 8, 2, 6, 7], 5].*/

%add_elem_hetero(L: list, R: list)
%flow model: (i, o) - deterministic

%add_elem_hetero(L1..Ln) = [] if L = []
%                                = L1 + add_elem_wrapper(L2, L1) + add_elem_hetero(L3..Ln) if is_list(L2)
%                                = L1 + add_elem_hetero(L2..Ln) otherwise
add_elem_hetero([], []).
add_elem_hetero([H, L | T], [H , Res | R]):-
    is_list(L),
    !,
    add_elem_wrapper(L, H, Res),
    add_elem_hetero(T, R).
add_elem_hetero([H|T], [H|R]):-
    add_elem_hetero(T, R).
    