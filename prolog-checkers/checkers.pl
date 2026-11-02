% Reconstructed simplified 8x8 checkers rules, not a full game engine.
:- use_module(library(plunit)).
inside(X,Y) :- between(1,8,X), between(1,8,Y).
forward(white, -1).
forward(black, 1).
opponent(white,black).
opponent(black,white).
% Board list: piece(Color,X,Y).
occupied(Board,X,Y) :- member(piece(_,X,Y),Board).
move(Board,Color,X,Y,NX,NY) :-
    member(piece(Color,X,Y),Board),
    forward(Color,D),
    member(DX,[-1,1]),
    NX is X+DX, NY is Y+D,
    inside(NX,NY), \+ occupied(Board,NX,NY).
capture(Board,Color,X,Y,NX,NY,CX,CY) :-
    member(piece(Color,X,Y),Board),
    opponent(Color,Other),
    forward(Color,D),
    member(DX,[-1,1]),
    CX is X+DX, CY is Y+D,
    member(piece(Other,CX,CY),Board),
    NX is X+2*DX, NY is Y+2*D,
    inside(NX,NY), \+ occupied(Board,NX,NY).
run_demo :-
    Board=[piece(white,4,5),piece(black,5,4)],
    findall([NX,NY,CX,CY],capture(Board,white,4,5,NX,NY,CX,CY),Moves),
    format('Available demo captures: ~w~n',[Moves]).
:- begin_tests(checkers).
test(simple_move) :- move([piece(white,4,5)],white,4,5,3,4).
test(blocked_move, [fail]) :- move([piece(white,4,5),piece(black,3,4)],white,4,5,3,4).
test(capture) :- capture([piece(white,4,5),piece(black,5,4)],white,4,5,6,3,5,4).
test(out_of_bounds, [fail]) :- move([piece(white,1,1)],white,1,1,0,0).
:- end_tests(checkers).
