# Explanation

La metodología númerica que se va a utilizar es RK4, como se mencionó anteriormente.

Este método numérico lo que hace es evaluar el estado del sistema a partir del anterior, es decir, de forma iterativa. Para ello, utiliza cuatro variables, razón por la que el método es de orden 4. A continuación, se presenta el valor que tiene cada una de las variables, y el valor que toma el estado.

$$
\begin{aligned}
    k_1 &= h f(t_n, y_n) \\
    k_2 &= h f(t_n + \frac{h}{2}, y_n + \frac{k_1}{2})  \\
    k_3 &= h f(t_n + \frac{h}{2}, y_n + \frac{k_2}{2})  \\
    k_4 &= h f(t_n + h, y_n + k_3)  \\
    y_{n+1} &= y_n + \frac{1}{6} (k_1 + 2k_2 + 2k_3 + k_4) \\,
\end{aligned}
$$

donde h es el tiempo transcurrido, y f es la función que genera la dinámica del problema en cuestión, que en este caso es: 

$$
\begin{equation}
  \textit{f(t,)} \textbf{y}) = -i[\textbf{O}, \textbf{y} (\textit{t})]
\end{equation}
$$

Note que esta función no depende explícitante de la variable temporal, por lo que a la hora de emplear el método RK4, se puede prescindir de esa parte, y emplear solo el operador lineal en su lugar.


