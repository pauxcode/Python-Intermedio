def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'Paul', 'lastname': 'Hernandez'}

    super_list = [
        {'firstname': 'Paul', 'lastname': 'Hernandez'},
        {'firstname': 'Ian', 'lastname': 'Aleman'},
        {'firstname': 'Miguel', 'lastname': 'Torres'},
        {'firstname': 'Pepe', 'lastname': 'Rodelo'},
        {'firstname': 'Susana', 'lastname': 'Gracia'},
        {'firstname': 'Jose', 'lastname': 'Garcia'}
    ]

    super_dict = {
        'natural_nums': [1,2,3,4,5,6],
        'integer_nums': [-2,-1,0,1,2],
        'floating_nums': [1.1,4.5,6.43]
    }

    for key, value in super_dict.items():
        print(key,'-',value)

if __name__ == '__main__':
    run()
