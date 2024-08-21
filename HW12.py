import random as rnd

# Question 1
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
"Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo",
"Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# # a
# oscar_winners.add("Emma Watson");
# print(oscar_winners);
#
# # b
# oscar_winners.clear();
# print(oscar_winners);
#
# # c
# oscar_winners.copy();
# print(oscar_winners);
#
# # d
# oscar_winners.remove("Meryl Streep");
# print(oscar_winners);
#
# # e
# print(titanic_actors.intersection(dark_knight_actors));
# print(True) if titanic_actors & dark_knight_actors else print(False);
#
# # f
# print(True) if iron_man_actors & avengers_actors else print(False);
#
# # g
# print(True) if actor_list <= oscar_winners else print(False);
#
# # h
# print(True) if actor_list < avengers_actors else print(False);
#
# # i
# print(f"before pop: {movie_cast}");
# movie_cast.pop();
# print(f"after pop: {movie_cast}");
#
# # j
# print(f"before remove: {movie_cast}");
# movie_cast.remove("Will Smith");
# print(f"after remove: {movie_cast}");
#
# # k
# print(titanic_actors - oscar_winners);
#
# # l
# print(titanic_actors ^ dark_knight_actors);
#
# # m
# print(f"before update: {oscar_winners}");
# oscar_winners |= {"Tom Hanks", "Natalie Portman"};
# print(f"after update: {oscar_winners}");
#
# # n
# print(titanic_actors.union(dark_knight_actors));
#
# # o
# dark_knight_rises_actors = {"Christian Bale", "Michael Caine", "Gary Oldman",
# "Tom Hardy", "Joseph Gordon-Levitt"};
# print(dark_knight_actors <= dark_knight_rises_actors);
#
# # p
# print(legendary_actors >= oscar_winners);
#
# # q
# print(avengers_actors - iron_man_actors);
#
# # r
# print(dark_knight_actors ^ avengers_actors);
#
# # s
# print(iron_man_actors | dark_knight_actors);
#
# # t
# new_set: frozenset = frozenset(legendary_actors);
# print(new_set);
#

# Question 2
# sets do not maintain order, and trying to access elements via index would return a 'TypeError'.

# Question 3
# both are hashable, dict keys and set elems are both distinct, both are mutable.

# Question 4
n100: set = {i for i in range(1, 101)};
print(n100);

# Question 5
nums: list = [rnd.randint(100, 500) for _ in range(50)];
s_nums: set = set(nums);
print(f"nums set: {s_nums}\nnums set length: {len(s_nums)}");