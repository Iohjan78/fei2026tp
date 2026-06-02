levantar el sistema:

docker compose up -d --build





- entrar a la consola de python:

bash bin/shell.sh

- para pasarle un parametro:

bash bin/python.sh -c "print('hola')"

- o si tenés un archivo script.py en la carpeta backend/:

bash bin/python.sh script.py


##para crear la app aulas##

bash bin/python.sh manage.py startapp aulas



- para crear un profesor: 
enrar a admin:
http://localhost:8000/admin
seleccionar tabla profesor
agregar los valores a los campos

verificar si instanciaron en base de datos 
y probar los verbos con esta url: (GET, PUT, DELETE)
http://localhost:8000/api/profesores/1/
(importante, usar el slash al final ya que se encuentra activo esta opcioon por defecto)