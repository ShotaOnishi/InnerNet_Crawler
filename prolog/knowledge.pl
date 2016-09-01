language(javaScript).
language(python).
language(commonLisp).
language(ruby).
language(prolog).
library(javascript, angularJS).
library(javascript, reactJS).
library(python, bottle).
write_lang :- language(X), write(X), nl, fail.
write_library(Y) :- library(Y, X), write(X), nl, fail.
