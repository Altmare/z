# py-calculadora
Calculadora basica utilizando python este proyecto con las funciones de resta, multiplicación, suma y resta.

## Funcionalidades
- **Sumar**: Suma dos números.
- **Resta**: Resta el primer número del otro
- **Multiplicación**: Múltiplica dos números
- **División**: Divide el primer número con el segundo

# Instalar lo siguiente
Tener instalado docker 
Tener instalado python

#Instruciones para la instalación 
1. Clonar el repositorio en la máquina local:

   ```sh
   git clone https://github.com/MaxYRGZ/z.git
   ```
2. Navega en el directorio del proyecto:

   ```sh
   cd z
   ```
3. Ejecuta el archivo z.py.
   
4. Sigue las instrucciones en la consola para seleccionar la operación deseada y los números a operar.
   
5. Para salir de la calculadora, elige la opción correspondiente en el menú.


Después debes de iniciar los contenedores
    ```sh
    docker-compose up -d
    ```
Construye la imagen con lo siguiente:

   ```sh
   docker build -t z
   ```
Ejecutar el contenedor 
   ```sh
   docker run -it z
   ```   
- **NOTA**: Asegurate que se este ejecutando el contenedor

La API estará disponible en `http://localhost:3100`.