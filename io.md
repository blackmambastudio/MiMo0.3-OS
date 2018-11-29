## input

 - boton reset

 - boton send
 - boton ask

 - boton pulsador A
 - boton pulsador B
 - boton pulsador C
 - boton pulsador D
 - boton pulsador E
 - boton pulsador F

 - seleccionador

 - perilla A
 - perilla B
 - RCH
 - GCH
 - BCH


## output

 - impresora
 - pantalla
 - audio
 - lcdA
 - lcdB
 - lcdC
 - lcdD
 - lcdE
 - lcdF
 - emosensemeter
 - sequence led 1
 - sequence led 2
 - sequence led 3
 - sequence led 4
 - progress send
 - progress reset
 
 
 ## Flujo
 
 
- boton ask

	- sequence led 1 - se apaga
	- sequence led 2 - se apaga
	- sequence led 3 - se apaga
	- sequence led 4 - se apaga

	- boton pulsado A - se apaga
	- boton pulsado B - se apaga
	- boton pulsado C - se apaga
	- boton pulsado D - se apaga
	- boton pulsado E - se apaga
	- boton pulsado F - se apaga

	- pantalla se pone en negro?
		- esperando informacion

	- impresora comienza a imprimir


- boton reset
	- sequence led 1 - se apaga
	- sequence led 2 - se apaga
	- sequence led 3 - se apaga
	- sequence led 4 - se apaga

	- boton pulsado A - se apaga
	- boton pulsado B - se apaga
	- boton pulsado C - se apaga
	- boton pulsado D - se apaga
	- boton pulsado E - se apaga
	- boton pulsado F - se apaga


- boton pulsador X 
	- se asigna al siguiente indice disponible
	- sequence led # - se prende del color del pulsador
	- boton pulsador X se prende

	- si no hay indice disponible, no se prende
	- en pantalla se muestra el material seleccionado

- seleccionador
	- muestra en pantalla el material en la posicion seleccionada para optimizar
	- activa el modo mejora

- perilla A
	- si esta activado modo mejora, manda senial de movimiento X

- perilla B
	- si esta activado modo mejora, manda senial de movimiento y

- RCH
	- si esta activado modo mejora, manda senial de activar/desactivar R

- GCH
	- si esta activado modo mejora, manda senial de activar/desactivar G

- BCH
	- si esta activado modo mejora, manda senial de activar/desactivar B


- boton send
	- muestra en pantalla resultados de ejecucion
	- se carga el boton de enviar
	- imprime los resultados del juego.


# estados del juego

 - en espera
 - recibiendo material
 - agregando material
 	- sin material seleccionado
 - optimizando material
 - reseteando
 - enviando material
