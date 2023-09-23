########################## Описание задачи ########################
# https://swish.swi-prolog.org/
houses(Hs):-
	% h(Nationality, Pet, Cigarette, Drink, Color)
    length(Hs, 5),
    member(h(english,_,_,_,red), Hs),
    member(h(spanish,dog,_,_,_), Hs),
    member(h(_,_,_,coffee,green), Hs),
    member(h(ukrainian,_,_,tea,_), Hs),
    next(h(_,_,_,_,green), h(_,_,_,_,white), Hs),
    member(h(_,snail,oldgold,_,_), Hs),
    member(h(_,_,kool,_,yellow), Hs),
    Hs = [_,_,h(_,_,_,milk,_),_,_],
    Hs = [h(norwegian,_,_,_,_)| _],
    next(h(_,fox,_,_,_), h(_,_,chesterfield,_,_), Hs),
    next(h(_,_,kool,_,_), h(_,horse,_,_,_), Hs),
    member(h(_,_,luckystrike,juice,_), Hs),
    member(h(japanese,_,parliament,_,_), Hs),
    next(h(norwegian,_,_,_,_), h(_,_,_,_,blue), Hs),
    member(h(_,zebra,_,_,_), Hs),
    member(h(_,_,_,water,_), Hs).
    
next(A, B, Ls) :- append(_, [A, B|_], Ls).
next(A, B, Ls) :- append(_, [B, A|_], Ls).

zebra_owner(Owner) :- 
    houses(Hs),
    member(h(Owner,zebra,_,_,_), Hs).

water_drinker(Drinker) :-
    houses(Hs),
    member(h(Drinker,_,_,water,_), Hs).


################################ Запуск запроса ####################################
zebra_owner(Owner); water_drinker(Drinker).