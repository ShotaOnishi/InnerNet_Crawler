write_lang :- language(X), write(X), nl, fail.
write_library(Y) :- library(Y, X), write(X), nl, fail.
write_lang_from_library(X) :- library(Y, X), write(Y), nl, fail.
