% insert_nth(Element, List, Position, Result)
% insert_nth(i, i, i, o)

% Inserts Element into List at the given Position (1-based index) resulting in Result.

% insert_nth(Element, L1...Ln, Position, Result) = Element + L1..Ln, if Position = 1
%                                             = List[0] + insert_nth(Element, L2..Ln, Position - 1), otherwise
insert_nth(Element, List, 1, [Element|List]):-!.
insert_nth(Element, [Head|Tail], Position, [Head|ResultTail]) :-
    Position > 1,
    NewPosition is Position - 1,
    insert_nth(Element, Tail, NewPosition, ResultTail).


% gcd(X, Y, Result)
% gcd(i, i, o)

% Computes the greatest common divisor of X and Y.

% gcd(X, Y) = X, if Y = 0
%           = gcd(Y, X mod Y), otherwise
gcd(X, 0, X):-!.
gcd(X, Y, Result) :-
    Y > 0,
    Z is X mod Y,
    gcd(Y, Z, Result).



% gcd_list(List, Result)
% gcd_list(i, o)
% gcd_list(i, i)

% Computes the greatest common divisor of the elements of a list

% gcd_list(L1...Ln) = 0, if n = 0
%                   = L1, if n = 1
%                   = gcd(gcd(L1, L2), gcd_list(L2...Ln)), otherwise
gcd_list([], 0).
gcd_list([X], X):-!.
gcd_list([X, Y|Tail], Result) :-
    gcd(X, Y, GCD),
    gcd_list([GCD|Tail], Result).


