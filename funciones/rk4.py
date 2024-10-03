def rk4(func, oper, state, h):
    """Evalúa el estado de un sistema dinámico con respecto al anterior.

    Examples:
        >>> rk4(dyn_generator, np.array([[0,1], [1, 0]]),  np.array([[1,0], [0,0]), 1.0)
        [[0.33333333+0.j   0. +0.33333333j] [0. -0.33333333j   0.66666667+0.j]]

    Args:
        func (function): Primer argumento. Se pone la función que genera la dinámica del sistema,
        oper: Segundo argumento. Es el operador lineal.
        state: Tercer argumento. Es el estado del sistema dinámico.
        h (float): Cuarto argumento. Es el tiempo trascurrido desde el estado anterior.

    Returns:
       list : Retorna la suma del estado anterior más un sexto de h por la suma del k_1 + 2*k_2 + 2*k_3 + k_4. Puede ser un arreglo, o un float
    """
    
    k_1 = func(oper, state)
    k_2 = func(oper, state + (k_1)/2
    k_3 = func(oper, state + (k_2)/2
    k_4 = func(oper, state + (k_3)
    return state + (1/6) * h * (k_1 + 2*k_2 + 2k_3 + k_4)
