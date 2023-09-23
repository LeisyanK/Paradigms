https://swish.swi-prolog.org/
###################### Генеалогическое древо #####################

############### Описание задачи ###############
male(egor).
male(vasiliy).
male(ivan).
male(foma).
female(ekaterina).
female(sofya).
female(maria).

parent(ivan, vasiliy).
parent(ivan, maria).
parent(egor, ivan).
parent(egor, sofya).
parent(sofya, foma).
parent(sofya, ekaterina).

father(X,Y):- parent(X,Y), male(Y).
mother(X,Y):- parent(X,Y), female(Y).

grandfather(X,Z):- parent(X,Y), father(Y,Z).
grandmother(X,Z):- parent(X,Y), mother(Y,Z).


################# Запуск запроса ######################
grandfather(egor, Z);
grandmother(egor, Z).