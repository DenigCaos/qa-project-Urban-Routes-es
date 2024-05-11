import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    botton_round = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    confort_select = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    button_phone_num = (By.CLASS_NAME, 'np-text')
    input_phone = (By.XPATH, '//*[@id="phone"]')
    button_phone_num_pop_up_window = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    sms_code_field = (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/form/div[1]/div/input')
    close_element_pop_up_window_phone_number = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/button')
    button_payment_method = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]')
    button_add_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    card_number_field = (By.CLASS_NAME, 'card-input')
    card_code_number_field = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')
    button_agree_card = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_element_pop_up_window_payment_method = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/button')
    message_for_driver_field = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/input')
    blanket_selector = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    ice_cream_plus = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    button_find_taxi = (By.XPATH, '/html/body/div/div/div[3]/div[4]/button')
    taxi_driver_selected = (By.XPATH, '/html/body/div/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_botton_round(self):
        # click en el boton del home page para pedir un taxi
        self.driver.find_element(*self.botton_round).click()

    def click_confort_select(self):
        # click en el boton de confort del home page
        self.driver.find_element(*self.confort_select).click()

    def click_phone_number_home_page(self):
        # click en el boton de home page para ingresar el numero de telefono
        self.driver.find_element(*self.button_phone_num).click()

    def set_phone_number(self, number_phone):
        # Encuentra y envia los datos en el campo del numero de telefono
        self.driver.find_element(*self.input_phone).send_keys(number_phone)

    def click_phone_number_pop_up_window(self):
        # click en el boton para agregar el numero de telefono desde la ventana emergente
        self.driver.find_element(*self.button_phone_num_pop_up_window).click()

    def set_sms_code(self, code_sms):
        # Encuentra y envia los datos en el campo del numero del codigo sms
        self.driver.find_element(*self.sms_code_field).send_keys(code_sms)

    def click_closet_pop_up_window_phone_number(self):
            # click para cerrar la ventana emergente del numero de telefono
            self.driver.find_element(*self.close_element_pop_up_window_phone_number).click()

    def click_payment_method(self):
        # click para el boton de metodo de pago de home page
        self.driver.find_element(*self.button_payment_method).click()

    def click_add_card(self):
        # click para el boton de añadir una tarjeta
        self.driver.find_element(*self.button_add_card).click()

    def set_card_number(self, number_card):
        # Encuentra y envia los datos en el campo del numero de tarjeta
        self.driver.find_element(*self.card_number_field).send_keys(number_card)

    def set_code_number(self, code_card):
        # Encuentra el campo del código de la tarjeta y envía el código
        code_field = self.driver.find_element(*self.card_code_number_field)
        code_field.send_keys(code_card)
        # Envía la tecla TAB para cambiar el enfoque
        code_field.send_keys(Keys.TAB)

    def click_add_card_2nd_pop_up_window(self):
        # click para el boton de añadir una tarjeta en la segunda ventana emergente
        self.driver.find_element(*self.button_agree_card).click()

    def click_closet_pop_up_window_payment_method(self):
        # click para cerrar la ventana emergente del metodo de pago
        self.driver.find_element(*self.close_element_pop_up_window_payment_method).click()

    def set_message_for_driver(self, driver_message):
        # Encuentra y envia los datos en el campo de mensaje para el conductor
        self.driver.find_element(*self.message_for_driver_field).send_keys(driver_message)

    def click_blanket_selector(self):
        # click para seleccionar manta y pañuelos
        self.driver.find_element(*self.blanket_selector).click()

    def click_ice_cream_plus(self):
        # click para agregar helados
        self.driver.find_element(*self.ice_cream_plus).click()

    def click_find_taxi(self):
        # click para pedir un taxi
        self.driver.find_element(*self.button_find_taxi).click()

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

# Crea una instancia del navegador.
driver = webdriver.Chrome()

# Acceder a la URL de Urban Routes.
driver.get(data.urban_routes_url)

# Espera hasta que cargue el logo principal de la pagina
logo_principal = (By.CLASS_NAME, 'logo-image')
WebDriverWait(driver, 3).until(EC.visibility_of_element_located(logo_principal))

# Crea una instancia de UrbanRoutesPage pasando el driver como argumento.
routes_page = UrbanRoutesPage(driver)

# Llamar al método set_from en la instancia de UrbanRoutesPage.
routes_page.set_from(data.address_from)
routes_page.set_to(data.address_to)

# Espera hasta que cargue el boton de pedir un taxi
WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UrbanRoutesPage.botton_round))

# Hace click en el boton de pedir un taxi
routes_page.click_botton_round()

# Espera hasta que cargue el menu del tipo de transporte
WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UrbanRoutesPage.confort_select))

# Hace click en el boton de confort
routes_page.click_confort_select()

# Hace click en el boton del home page del numero de telefono
routes_page.click_phone_number_home_page()

# Espera hasta que cargue la ventana emergente para ingresar el numero de telefono
WebDriverWait(driver, 3).until(EC.visibility_of_element_located(UrbanRoutesPage.button_phone_num))

# Ingresa el numero de telefono en el campo de la ventana emergente
routes_page.set_phone_number(data.phone_number)

# Hace click en el boton siguiente despues de ingresar el numero de telefono
routes_page.click_phone_number_pop_up_window()

# Utilizo codigo ya preestablecido para obtener codigo sms para agregar numero telefonico
# El codigo no esta arrojando nada, hice pruebas con print y el valor era none
codigo_confirmacion = retrieve_phone_code(driver)
routes_page.set_sms_code(str(codigo_confirmacion))

# Cierro la ventana emergente para ingresar el numero de telefono
routes_page.click_closet_pop_up_window_phone_number()

# Hace click en el boton de metodo de pago en home page
routes_page.click_payment_method()

# Hace click en el boton añadir tarjeta
routes_page.click_add_card()

# Ingresa el numero de tarjeta
routes_page.set_card_number(data.card_number)

# Ingresa el numero de codigo de la tarjeta
routes_page.set_code_number(data.card_code)
WebDriverWait(driver, 3).until(EC.element_to_be_clickable(UrbanRoutesPage.button_agree_card))

# Hace click en el boton añadir tarjeta de la segunda ventana emergente
routes_page.click_add_card_2nd_pop_up_window()

# Hace click para cerrar en la segunda ventana de metodo de pago
routes_page.click_closet_pop_up_window_payment_method()

# Ingresa el mensaje del conductor
routes_page.set_message_for_driver(data.message_for_driver)

# Seleccionar la manta y pañuelo
routes_page.click_blanket_selector()

# Agregar 2 helados
routes_page.click_ice_cream_plus()
routes_page.click_ice_cream_plus()

# Hace click pedir un taxi y espera hasta que el sistema seleccione un conductor
routes_page.click_find_taxi()

WebDriverWait(driver, 40).until(EC.visibility_of_element_located(UrbanRoutesPage.taxi_driver_selected))

