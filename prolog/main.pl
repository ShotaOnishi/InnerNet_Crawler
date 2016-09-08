:- initialization main.
main :-
  ['./control.pl'],
  ['./knowledge.pl'],
  current_prolog_flag(argv, Argv),
  format('Hello World, argv:~w\n', [Argv]),
  write(Argv), 
  write_lang,
  halt(0).
