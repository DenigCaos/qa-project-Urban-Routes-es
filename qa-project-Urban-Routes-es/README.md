## Automatización de Pruebas de Urban-Routes

## Descripción del Proyecto
Este proyecto implementa una serie de pruebas automatizadas 
para la aplicación web 'Urban Routes', que permite a los
usuarios reservar taxis y personalizar su viaje con opciones 
adicionales. Utiliza Selenium WebDriver para interactuar 
con la interfaz web y automatizar tareas como ingresar 
direcciones, seleccionar opciones de confort, ingresar 
métodos de pago y más.

## Tecnologías y Técnicas Utilizadas
- **Selenium WebDriver**: Para la automatización de interacciones
con el navegador.
- **Python**: Lenguaje de programación utilizado para escribir
los scripts de prueba.
- **Patrón Page Object**: Para mejorar el mantenimiento del
código y reducir la duplicación, encapsulando la lógica de
interacción con la página web en clases específicas.
- **Esperas Explícitas (Explicit Waits)**: Para manejar condiciones
de carrera y asegurar que los elementos estén presentes antes de
interactuar con ellos.
- **Registro de Rendimiento (Performance Logging)**: Para capturar
y analizar mensajes de rendimiento del navegador, útil para 
recuperar códigos de confirmación de teléfono a través de
solicitudes de red.

## Estructura del Código
El código está organizado en dos clases principales:
- `UrbanRoutesPage`: Define los elementos de la página y las 
acciones que se pueden realizar en ella, como ingresar 
direcciones y seleccionar opciones.
- `TestUrbanRoutes`: Contiene los métodos de prueba que 
utilizan instancias de `UrbanRoutesPage` para llevar a
cabo los escenarios de prueba.

## Cómo Ejecutar las Pruebas
Para ejecutar las pruebas, asegúrate de tener instaladas 
las dependencias necesarias y sigue estos pasos:
1. Inicia el servidor de Selenium y asegúrate de que el 
navegador objetivo esté disponible.
2. Ejecuta el script de prueba con un comando como
`pytest test_urban_routes.py`.

Se crearon los archivos UrbanRoutesPage.py, 
helpers.py, data.py y main.py para el desarrollo del código

Se definieron los localizadores y métodos necesarios en la
clase UrbanRoutesPage y las pruebas en la clase TestUrbanRoutes.

### main.py

test1_set_route: Establece una ruta ingresando direcciones
de origen y destino.

test2_select_confort: Selecciona opciones de confort en la
página.

test3_set_phone: Ingresa y verifica un número de teléfono.

test4_add_card: Añade información de tarjeta de crédito 
para el pago.

test5_message_for_driver: Envía un mensaje al conductor.

test6_blanket_active: Verifica que la opción de manta y
pañuelo esté activa después de seleccionarla.

test7_ice_cream: Confirma que se pueden agregar helados
al pedido y verifica que el número correcto haya sido añadido.

test8_order_taxi: Realiza el proceso completo de pedir un
taxi, incluyendo la selección de un conductor, y asegura 
que el conductor haya sido seleccionado correctamente.

teardown_class: Método de limpieza que se ejecuta después
de todas las pruebas para cerrar el navegador.

### UrbanRoutesPage.py

Métodos Disponibles
set_from(from_address): Ingresa una dirección en el
campo de dirección de origen.

set_to(to_address): Ingresa una dirección en el campo
de dirección de destino.

get_from(): Obtiene el valor actual del campo de dirección
de origen.

get_to(): Obtiene el valor actual del campo de dirección
de destino.

click_botton_round(): Hace clic en el botón para solicitar
un taxi.

click_confort_select(): Hace clic en la opción de confort.
click_check_confort_select(): Verifica si la opción de 
confort está seleccionada.

set_phone_number(number_phone): Ingresa un número de teléfono
en el campo correspondiente.

get_phone_number(): Obtiene el número de teléfono ingresado.
set_sms_code(code_sms): Ingresa el código SMS recibido.

click_payment_method(): Hace clic en el método de pago.

set_card_number(number_card): Ingresa el número de una
tarjeta de crédito o débito.

set_code_number(code_card): Ingresa el código de seguridad
de la tarjeta.

set_message_for_driver(driver_message): Ingresa un mensaje
para el conductor.

click_blanket_selector(): Selecciona opciones adicionales
como mantas y pañuelos.

### helpers.py

Este módulo contiene funciones auxiliares para automatizar
pruebas con Selenium. Proporciona métodos para recuperar
códigos de confirmación de teléfono y esperar ciertas
condiciones en elementos web.

### data.py

Este archivo de configuración contiene las variables 
necesarias para ejecutar las pruebas automatizadas en la 
página web de Urban Routes. Incluye la URL del sitio, 
direcciones de origen y destino, información de contacto
y de pago, y un mensaje para el conductor.
