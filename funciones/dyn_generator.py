def dyn_generator(oper, state):
    """Evalúa de la dinámica de un sistema.

    Examples:
        >>> dyn_generator(np.array([[0,1], [1,0]], np.array([[1,0], [0,0]])
        [[0.-j  0.+1.j] [0.-1j  0.-0.j]]

    Args:
        oper (matrix): Primer argumento. Es el operador lineal. 
        state (matrix): Segundo argumento. Es el estado del sistema dinámico. 

    Returns:
       (matrix): Retorna la multiplicación de la constante compleja por la operación de conmutación del primer argumento con el segundo argumento. 

    """
    return -1.0j * (np.dot(oper, state) - np.dot(state, oper))
