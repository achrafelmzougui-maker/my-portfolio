# Jeu de dames en Prolog — educational rules prototype

**Reconstructed demonstration**, not the recovered source of the earlier university expert-systems project. SWI-Prolog required.

Run:
```bash
swipl -q -s checkers.pl -g run_demo -t halt
swipl -q -s checkers.pl -g run_tests -t halt
```

The demo models an **8×8 simplified board**, legal diagonal moves for regular pieces, and mandatory forward captures as individual moves. It does **not** implement the full international 10×10 rules, kings, multi-jump chains, turn orchestration or a game UI.

The aim is to demonstrate declarative rules, inference and unit testing.
