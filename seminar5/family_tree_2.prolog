% Rules
male(sergey).
male(vladimir).
male(alexey).
male(alexandr).
male(serafim).
female(lubov).
female(galina).
female(vera).
female(anastasiya).
female(olga).

parent(vera, sergey).
parent(vera, lubov).
parent(alexey, vladimir).
parent(alexey, galina).
parent(anastasiya, vera).
parent(anastasiya, alexey).
parent(olga, vera).
parent(olga, alexey).
parent(serafim, anastasiya).
parent(serafim, alexandr).

father(X,Y):- parent(X,Y), male(Y).
mother(X,Y):- parent(X,Y), female(Y).

grandfather(X,Z):- parent(X,Y), father(Y,Z).
grandmother(X,Z):- parent(X,Y), mother(Y,Z).

child(Y, X):- parent(X,Y).

% Query
grandfather(anastasiya, Z), write(Z);
grandmother(anastasiya, Z), write(Z);
grandfather(alexey, Z), write(Z);
grandmother(alexey, Z), write(Z);
father(anastasiya, Y);
mother(anastasiya, Y);
father(alexey, Y);
mother(alexey, Y);
child(anastasiya, X);
child(alexey, X).