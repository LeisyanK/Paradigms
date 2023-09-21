pep = [{"name": "Ivan", "age": 31},{"name": "Peter", "age": 24}, {"name": "Polya", "age": 34}]
print(sum(map(lambda x: x["age"] > 30, pep)))