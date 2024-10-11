dict1 = {
    1: "ананас",
    2: 42,
    3: {
        "a": "треш",
        "b": 3.14,
        "c": True,
        "d": [1, 2, 3],
        "f": {"Анжеліка", "Поручнік"}
    },
    4: [10, 20, 30]
}

dict1_types = {}
for key, value in dict1.items():
        if isinstance(value, dict):
            dict1_types[key] = {key: type(value) for key, value in value.items()}
        else:
            dict1_types[key] = type(value)

print(dict1_types)
