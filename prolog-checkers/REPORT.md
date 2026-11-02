# Technical report — Rule-based Checkers

## Objective
Illustrate an expert-system approach to board-game move validation using logical predicates and unification.

## Knowledge representation
`piece(Color,X,Y)` facts are represented as list members. Rules `move/7` and `capture/9` determine forward diagonal movement and a single capture on an 8×8 board.

## Tests
PlUnit examples verify a legal move, occupied destination, capture and board boundary. Tests have not been executed in this GitHub session.

## Scope
A deliberately partial prototype. The earlier full academic implementation is not available for source verification. Full game rules, king promotion, capture priority, multiple captures and interactive play are future work.
