:- initialization main.
main :-
  ['./control.pl'],
  ['./knowledge.pl'],
  current_prolog_flag(argv, Argv),
  nth0(0, Argv, Argument0),
  write_library(Argument0),
  halt(0).
