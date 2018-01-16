from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from win10toast import ToastNotifier
toaster = ToastNotifier()

driver = webdriver.Chrome()

# Exito search
driver.get("http://www.exito.com")
assert "exito" in driver.title
elem = driver.find_element_by_id("tbxSearch")
elem.clear()
elem.send_keys("moto g5s plus")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
dorado = driver.find_element_by_partial_link_text("Dorado")
exito_price = dorado.find_element_by_class_name("price")

# Falabella search
driver.get("https://www.falabella.com.co/falabella-co/")
assert "Falabella" in driver.title
elem = driver.find_element_by_id("searchQuestion")
elem.clear()
elem.send_keys("moto g5s plus")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
dorado = driver.find_element_by_partial_link_text("Dorado")
dorado.click()
falabella_price = driver.find_element_by_class_name("fb-product-sets__product-price")
falabella_price = re.findall(r'\d+\.\d+', falabella_price.text)

if exito_price<900.000:
    toaster.show_toast("Heyy!!!", "Exito lowered the price: "+ str(exito_price))
if falabella_price<900.000:
    toaster.show_toast("Heyy!!!", "Falabella lowered the price"+ str(falabella_price))

driver.close()
