# Welcome to RK4 Module!

Este es un módulo que ayuda a resolver sistemas dinámicos.

Los sistemas dinámicos son de suma importancia en las ciencias. En general, un modelo dinámico intenta resolver la trayectoria temporal de alguna cantidad física como función de algún generador dinámico; este último usualmente representado de forma funcional.

En algunos casos, podemos modelar la dinámica de un estado genérico mediante la ecuación dinámica:

$$
\begin{equation}
  \frac{dy}{dt} = f(t, y),
\end{equation}
$$

sujeta a la condición inicial

$$
\begin{equation}
  y(t_0) = y_0
\end{equation}
$$

En esta notación, $\textit{y}$ corresponde a un estado del sistema. Este estado puede ser representado mediante diferentes objetos matemáticos: desde cantidades escalares hasta matrices que representan cierto operador lineal. En la ecuación anterior, $\textit{t}$ corresponde a la variable temporal.

Con este módulo se va a resolver un problema dinámico genérico.

Se quiere estudiar la evolución temporal de un estado $\textbf{y}(\textit{t})$. Este estado será representado mediante una matriz 2x2 que corresponde a algún operador lineal. La función que genera la dinámica del problema es:

$$
\begin{equation}
 f(\textit{t}, \textbf{y}) = -i[\textbf{O}, \textbf{y}(\textit{t})]
\end{equation}
$$

donde $\textbf{O}$ es otro operador lineal, es la constante compleja y es un operación de conmutación. Note que la función $f(\textit{t}, \textbf{y})$ no depende explícitamente de la variable temporal. 

El operador $\textbf{O}$ puede tener distintos significados físicos dependiendo del problema dinámico en cuestión. Puede representar un mapa algebraico, el generador dinámico de un sistema caótico, un Hamiltoniano, etc.

Este módulo resuleve estos sistemás dinámicos genéricos mediante el uso del método númerico Runge-Kutta de orden 4 (RK4).

Esta página es la página de documentación del módulo.

For full documentation visit [github.com](https://github.com/RudyMiranda04/RK4.-Tarea).


