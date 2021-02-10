def tallest_people(**kwargs):
    max_height, persons = 0, []
    for name in kwargs:
        if max_height < kwargs[name]:
            max_height, persons = kwargs[name], [name]
        elif max_height == kwargs[name]:
            persons.append(name)

    for name in sorted(persons):
        print(name, ':', max_height)

# tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)
