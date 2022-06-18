DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    #This comprehension returns a list with the name of the workers who use python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    #Same list but with high order functions
    all_python = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python = list(map(lambda worker: worker["name"], all_python))
    print(all_python_devs , "  " , all_python)

    #Filter for adults
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    #Map to obtain only the names
    adults = list(map(lambda worker: worker["name"], adults))
    #Same but with comprehensions
    adults_list = [worker["name"] for worker in DATA if worker["age"] > 18]
    print(adults, "   ", adults_list)

    #Both print made to compare the results of different methods


if __name__ == '__main__':
    run()