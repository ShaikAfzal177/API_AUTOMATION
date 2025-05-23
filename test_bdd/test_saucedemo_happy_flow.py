
from pytest_bdd import scenarios, given, when, parsers, then

scenarios("../features/saucedemo.feature")


@given("the user is on the saucedemo login page")
def open_login(login_page):
    login_page.load()

@when(parsers.parse('the user logs in with "{username}" and "{password}"'))
def user_login(login_page, username, password):
    login_page.login_user(username,password)

@given("the user land on the products page")
@then("the user land on the products page")
def user_on_product_page(login_page):
    assert login_page.page_logo()



@when(parsers.parse('Add to cart "{product_name}" from  all product list'))
def add_product_from_list(login_page, product_name):
    assert login_page.select_product(product_name)

@then(parsers.parse('validate cart item "{product_name}"'))
def validate_cart_item(login_page, product_name):
    assert  login_page.cart_item_validate(product_name)

@given("click check out button")
def click_checkout(login_page):
    login_page.checkout()

@when(parsers.parse('fill the userdetails "{first_name}" "{last_name}" "{pin}" and click continue and finish button'))
def add_user_details(login_page,first_name, last_name, pin):
    login_page.add_details(first_name,last_name,pin)

@then("show the order placed message")
def order_message(login_page):
    assert login_page.order_success_message()

