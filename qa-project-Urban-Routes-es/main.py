import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import helpers
import UrbanRoutesPage

class TestUrbanRoutes:

    driver = webdriver.Chrome()
    @classmethod
    def setup_class(cls):
        # Configuración de las opciones de Chrome
        options = Options()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920x1080")
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        # Inicialización del WebDriver con las opciones definidas
        cls.driver = webdriver.Chrome(options=options)
    def test1_set_route(self):
        # Acceder a la URL de Urban Routes.
        self.driver.get(data.urban_routes_url)
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que cargue el logo principal de la pagina
        helpers.Wait_visibility_of_element(self.driver, routes_page.logo_principal, 3)
        # Iguala las variales de direccion origen y destino a la respectivas en el archivo data
        address_from = data.address_from
        address_to = data.address_to
        # Llamar al método set_from en la instancia de UrbanRoutesPage.
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Confirmación de la prueba
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test2_select_confort(self):
        # Acceder a la URL de Urban Routes.
        self.driver.get(data.urban_routes_url)
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que cargue el logo principal de la pagina
        helpers.Wait_visibility_of_element(self.driver, routes_page.logo_principal, 3)
        # Iguala las variales de direccion origen y destino a la respectivas en el archivo data
        address_from = data.address_from
        address_to = data.address_to
        # Llamar al método set_from en la instancia de UrbanRoutesPage.
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Espera hasta que cargue el boton de pedir un taxi
        helpers.Wait_visibility_of_element(self.driver, routes_page.botton_round, 3)
        # Hace click en el boton de pedir un taxi
        routes_page.click_botton_round()
        # Hace click en el boton de confort
        routes_page.click_confort_select()
        assert True, routes_page.click_check_confort_select
    def test3_set_phone(self):
        # Acceder a la URL de Urban Routes.
        self.driver.get(data.urban_routes_url)
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que cargue el logo principal de la pagina
        helpers.Wait_visibility_of_element(self.driver, routes_page.logo_principal, 3)
        # Iguala las variales de direccion origen y destino a la respectivas en el archivo data
        address_from = data.address_from
        address_to = data.address_to
        # Llamar al método set_from en la instancia de UrbanRoutesPage.
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Espera hasta que cargue el boton de pedir un taxi
        helpers.Wait_visibility_of_element(self.driver, routes_page.botton_round, 3)
        # Hace click en el boton de pedir un taxi
        routes_page.click_botton_round()
        # Hace click en el boton de confort
        routes_page.click_confort_select()
        # Hace click en el boton del home page del numero de telefono
        routes_page.click_phone_number_home_page()
        phone_number = data.phone_number
        routes_page.set_phone_number(phone_number)

        # Hace click en el boton siguiente despues de ingresar el numero de telefono
        routes_page.click_phone_number_pop_up_window()
        # Utilizo codigo ya preestablecido para obtener codigo sms para agregar numero telefonico
        # El codigo no esta arrojando nada, hice pruebas con print y el valor era none
        codigo_confirmacion = helpers.retrieve_phone_code(self.driver)
        routes_page.set_sms_code(str(codigo_confirmacion))
        assert True, (str(codigo_confirmacion)).isdigit()
        #click boton siguiente de ventana emergente de codigo de telefono
        routes_page.click_next_code_phone()
        assert routes_page.get_phone_number() == phone_number

    def test4_add_card(self):
        # Acceder a la URL de Urban Routes.
        self.driver.get(data.urban_routes_url)
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que cargue el logo principal de la pagina
        helpers.Wait_visibility_of_element(self.driver, routes_page.logo_principal, 3)
        # Iguala las variales de direccion origen y destino a la respectivas en el archivo data
        address_from = data.address_from
        address_to = data.address_to
        card_number=data.card_number
        card_code=data.card_code
        # Llamar al método set_from en la instancia de UrbanRoutesPage.
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Espera hasta que cargue el boton de pedir un taxi
        helpers.Wait_visibility_of_element(self.driver, routes_page.botton_round, 3)
        # Hace click en el boton de pedir un taxi
        routes_page.click_botton_round()
        # Hace click en el boton de confort
        routes_page.click_confort_select()
        # Hace click en el boton de metodo de pago en home page
        routes_page.click_payment_method()
        # Hace click en el boton añadir tarjeta
        routes_page.click_add_card()
        # Ingresa el numero de tarjeta
        routes_page.set_card_number(card_number)
        # Ingresa el numero de codigo de la tarjeta
        routes_page.set_code_number(card_code)
        helpers.Wait_to_be_clickable_of_element(self.driver, routes_page.botton_agree_card, 3)
        assert routes_page.get_card_number() == card_number
        assert routes_page.get_code_number() == card_code
        # Hace click en el boton añadir tarjeta de la segunda ventana emergente
        routes_page.click_add_card_2nd_pop_up_window()
        assert True, routes_page.check_agree_tcard()

    def test5_message_for_driver(self):
        # Acceder a la URL de Urban Routes.
        self.driver.get(data.urban_routes_url)
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que cargue el logo principal de la pagina
        helpers.Wait_visibility_of_element(self.driver, routes_page.logo_principal, 3)
        # Iguala las variales de direccion origen y destino a la respectivas en el archivo data
        address_from = data.address_from
        address_to = data.address_to
        message_for_driver=data.message_for_driver
        # Llamar al método set_from en la instancia de UrbanRoutesPage.
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Espera hasta que cargue el boton de pedir un taxi
        helpers.Wait_visibility_of_element(self.driver, routes_page.botton_round, 3)
        # Hace click en el boton de pedir un taxi
        routes_page.click_botton_round()
        # Hace click en el boton de confort
        routes_page.click_confort_select()
        # Ingresa el mensaje del conductor
        routes_page.set_message_for_driver(message_for_driver)
        assert routes_page.get_message_for_driver() == message_for_driver

    def test6_blanket_active(self):
        # Acceder a la URL de Urban Routes.
        self.driver.get(data.urban_routes_url)
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que cargue el logo principal de la pagina
        helpers.Wait_visibility_of_element(self.driver, routes_page.logo_principal, 3)
        # Iguala las variales de direccion origen y destino a la respectivas en el archivo data
        address_from = data.address_from
        address_to = data.address_to
        # Llamar al método set_from en la instancia de UrbanRoutesPage.
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Espera hasta que cargue el boton de pedir un taxi
        helpers.Wait_visibility_of_element(self.driver, routes_page.botton_round, 3)
        # Hace click en el boton de pedir un taxi
        routes_page.click_botton_round()
        # Hace click en el boton de confort
        routes_page.click_confort_select()
        # Seleccionar la manta y pañuelo
        routes_page.click_blanket_selector()
        assert routes_page.get_blanket_value() == 'on'


    def test7_ice_2_cream(self):
        # Acceder a la URL de Urban Routes.
        self.driver.get(data.urban_routes_url)
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que cargue el logo principal de la pagina
        helpers.Wait_visibility_of_element(self.driver, routes_page.logo_principal, 3)
        # Iguala las variales de direccion origen y destino a la respectivas en el archivo data
        address_from = data.address_from
        address_to = data.address_to
        # Llamar al método set_from en la instancia de UrbanRoutesPage.
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Espera hasta que cargue el boton de pedir un taxi
        helpers.Wait_visibility_of_element(self.driver, routes_page.botton_round, 3)
        # Hace click en el boton de pedir un taxi
        routes_page.click_botton_round()
        # Hace click en el boton de confort
        routes_page.click_confort_select()
        # Agregar 2 helados
        for _ in range(2):
            routes_page.click_ice_cream_plus()
        assert routes_page.get_ice_cream_value() == '2'


    def test8_order_taxi(self):
        # Acceder a la URL de Urban Routes.
        self.driver.get(data.urban_routes_url)
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que cargue el logo principal de la pagina
        helpers.Wait_visibility_of_element(self.driver, routes_page.logo_principal, 3)
        # Iguala las variales de direccion origen y destino a la respectivas en el archivo data
        address_from = data.address_from
        address_to = data.address_to
        message_for_driver = data.message_for_driver
        # Llamar al método set_from en la instancia de UrbanRoutesPage.
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Espera hasta que cargue el boton de pedir un taxi
        helpers.Wait_visibility_of_element(self.driver, routes_page.botton_round, 3)
        # Hace click en el boton de pedir un taxi
        routes_page.click_botton_round()
        # Hace click en el boton de confort
        routes_page.click_confort_select()
        # Ingresa el mensaje del conductor
        routes_page.set_message_for_driver(message_for_driver)
        assert True, routes_page.check_botton_find_taxi()
        # Hace click pedir un taxi y espera hasta que el sistema seleccione un conductor
        routes_page.click_find_taxi()
        helpers.Wait_visibility_of_element(self.driver, routes_page.taxi_driver_selected, 40)
        assert True, routes_page.taxi_driver_selected()

    def test9_order_header_title(self):
        # Acceder a la URL de Urban Routes.
        self.driver.get(data.urban_routes_url)
        # Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        # Espera hasta que cargue el logo principal de la pagina
        helpers.Wait_visibility_of_element(self.driver, routes_page.logo_principal, 3)
        # Iguala las variales de direccion origen y destino a la respectivas en el archivo data
        address_from = data.address_from
        address_to = data.address_to
        message_for_driver = data.message_for_driver
        # Llamar al método set_from en la instancia de UrbanRoutesPage.
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Espera hasta que cargue el boton de pedir un taxi
        helpers.Wait_visibility_of_element(self.driver, routes_page.botton_round, 3)
        # Hace click en el boton de pedir un taxi
        routes_page.click_botton_round()
        # Hace click en el boton de confort
        routes_page.click_confort_select()
        # Ingresa el mensaje del conductor
        routes_page.set_message_for_driver(message_for_driver)
        # Hace click pedir un taxi y espera hasta que el sistema seleccione un conductor
        routes_page.click_find_taxi()
        helpers.Wait_visibility_of_element(self.driver, routes_page.taxi_driver_selected, 40)
        assert True, routes_page.check_order_header_title()
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



