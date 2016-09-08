:- initialization main.
main :-
  ['./prolog/control.pl'],
  ['./prolog/knowledge.pl'],
  current_prolog_flag(argv, Argv),
  nth0(0, Argv, Argument0),
  write_library(Argument0),
  halt.
