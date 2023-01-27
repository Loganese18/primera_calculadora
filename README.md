Esta Calculadora es el primer proyecto que he realizado con Python.
Luego de todo el aprendizaje por el camino recorrido, elaboré una segunda Calculadora, cuyo repositorio también se encuentra disponible. 
Jamás habia usado Tkinter, por lo que tuve un proceso inicial de descubrimiento de las distintas opciones que ofrece.
He consultado material sobre dicho módulo pero no recurrí a tutoriales sobre como hacer una calculadora en Python.
En retrospectiva, considero que este desconocimiento inicial resultó positivo, ya que me obligó a explorar casi en su totaliad las caracteristicas del módulo.
Esta situación, en contrapartida, generó el problema central que atravezó todo el desarrollo de la Calculadora, provocado por la incorrecta elección del widget correspondiente a la pantalla de la Calculadora. 
Al comenzar el proyecto, mi primer objetivo fue generar el conjunto de botones de la Calculadora, y que estos estuvieran alineados, fueran simetricos y se encontraran centrados en la Ventana (top level widget). Dispuse los botones dentro de un Frame creado unicamente para estos.
Luego agregué un segundo Frame, que contendría primero un solo widget capaz de mostrar los caracteres que se fueran ingresando, y finalmente dos widgets, incorporando uno que mostrara la operación luego de realizada.
El problema central del proyecto surgió a partir de la elección del widget Label para la parte de la pantalla que debia mostrar los caracteres en tiempo real, a medida que el usuario los ingresaba, o bien eliminarlos, dado el caso. Label no contiene los metodos insert o delete, lo que implicó pensar algun camino para poder incorporar los caracteres, contemplando que luego debían poder ser operados matematicamente.
Luego descubrí que más adecuado era usar el widget Entry.
Un segundo gran obstáculo fue incorporar el caracter punto(.), para los decimales, que quedaba en evidencia a la hora de desarrollar la operación matematica, ya que los datos que se ingresaban eran tipo String.
Este problema se encontraba estrechamente ligado al tercer problema que se me presentó, principalmente: como operar matematicamente con datos tipo String.
La solución que encontré fue un complicado pasaje de todos los numeros a tipo integer, con el agregado de lograr la adecuada inclusión de los decimales, si hubiera, y finalemnte realizar la operación.
Para esto último utilicé el módulo operator, asociando cada caracter que representaba una operación en la pantalla, con la operación correspondiente. Es decir si la función recibía '+', efectuaba una suma entre los numeros correspondientes, ya tipo integer.
