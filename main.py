def exo_1 (a : int, b : int):
    my_boolean = True
    my_int = 9
    my_str = f"""En résumé :
        my_bloolean = {my_boolean}
        my_int = {my_int} 
    """


    my_power = a**b
    my_modulo = a%b
    my_full_div = a//b
    pretty_sentence = f"""
    Les opérateurs :

        {a}^{b} : {my_power}
        {a}%{b} : {my_modulo}
        {a}//{b} : {my_full_div}
        """
    print(pretty_sentence)

def generate_value () :
    k = 1
    while True :
        yield 2**k
        k+=1

def exo_gener_val() :
    generator = generate_value()

    oneliner_list = [next(generator) for _ in range (7)]
    oneliner_matrix = [[next(generator) for _ in range (7)] for __ in range (3)]

    import tabulate

    pretty_m = tabulate.tabulate(oneliner_matrix)
    print(pretty_m)