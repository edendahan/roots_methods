# f(x) = x ** 2 + 2 * x + 2
# f(x1) * f(x2) < 0
#ruth avivi 208981555
#eden dahan 318641222
def f_tag(f, x):
    """
    x = c
    f'(x) = lim h->0 (f(c + h) - f(c))/h
    """
    h = 0.0000000001

    return (f(x + h) - f(x))/h

def biscetion(f, start, end, epsilon, max_iteration = 200):
    c = start
    i = 1
    while abs(f(c)) > epsilon and max_iteration > 0:
        c = (end + start)/2
        if f(c) * f(start) > 0:
            start = c
        elif f(c) * f(end) > 0:
            end = c
        else:
            return c
        i += 1
        max_iteration -= 1

    if max_iteration == 0:
        print(f'guess {c} is not an approximated root')

    return c, i

def nethon_raphson(f, start, end, epsilon, max_iteration = 200):
    guess = (end + start) / 2
    if max_iteration < 0:
        max_iteration *= -1
    i = 1
    while abs(f(guess)) > epsilon and max_iteration >= 0:
        guess = guess - f(guess)/ f_tag(f, guess)
        i += 1
        max_iteration -= 1
    if max_iteration == 0:
        print(f'guess {guess} is not an approximated root')
    return guess, i

def secant(f, start, end, epsilon, max_iteration = 200):
    '''

    :param f:
    :param start:
    :param end:
    :param epsilon:
    :param max_iteration:
    :return:
    '''
    guess1 = (end + start) / 2
    guess2 = (end + start) / 3
    s = 0.00000001
    i = 0
    while abs(f(guess2)) > epsilon and max_iteration > 0:
        tmp = guess2
        if f(guess2) - f(guess1) == 0:
            guess1 += s
        guess2 = guess2 - f(guess2) * ((guess2 - guess1)/ (f(guess2) - f(guess1)))
        guess1 = tmp
        max_iteration -= 1
        i += 1

    if max_iteration == 0:
        print(f'guess {guess2} is not an approximated root')

    return guess2, i


def main():
    polinom = lambda x: x ** 2 - 4
    start = -10
    end = 10
    jump = 0.1
    epsilon = 0.0001
    method_choices = {"1": biscetion, "2": nethon_raphson, "3": secant}
    choice = input("Please enter method:\n1) Bisection\n2) Nethon raphson\n3) Secant")
    while choice not in method_choices.keys():
        choice = input("Please enter method:\n1) Bisection\n2) Nethon raphson\n3) Secant")
    method = method_choices[choice]
    print(f'{choice} has been selected')
    roots = []
    s = start
    e = start + jump
    root_exits = False
    while e < end:
        print(f'interval ({s}, {e}):')
        root , i = method(polinom, s, e, epsilon)
        if abs(polinom(root)) <= epsilon:
            for r in roots:
                if abs(root - r) <= epsilon:
                    root_exits = True
                    break
            if not root_exits:
                roots.append(root)
                print("------------------------------------")
                print(f'root : {root}, iterations: {i}')
                print("------------------------------------")
            root_exits = False
        s = e
        e = e + jump
        print("")
    print(roots)


if __name__ == "__main__":
    main()
