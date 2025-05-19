from pytest_bdd import scenarios, given, when, parsers, then



scenarios("../features/flipkart.feature")

@given("the user opens the Flipkart homepage")
def open_flipkart(flipkart_page):
    flipkart_page.load_flipkart()

@when(parsers.parse('the user searches for a product "{product_name}"'))
def search_product(flipkart_page, product_name):
    flipkart_page.search_product(product_name)

@when("the user clicks on the 3rd product in the search results")
def click_the_product(flipkart_page):
    flipkart_page.click_the_product()

@then("the product name, price, and description should be displayed")
def product_details(flipkart_page):
    flipkart_page.get_product_details()
@then("the product should be created via API")
def product_create(context,flipkart_page,product_api):
    data=flipkart_page.product_create(product_api)
    if data:
        product_id=data["product"]["id"]
        context["product_id"]=product_id
@then("the created product should be deleted")
def product_delete(context,flipkart_page,product_api):
    product_id=context["product_id"]
    flipkart_page.product_delete(product_api,product_id)
