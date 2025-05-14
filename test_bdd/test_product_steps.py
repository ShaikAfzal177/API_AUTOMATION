from pytest_bdd import scenarios, given, when, then, parsers

from data.payload_generator import PayloadGenerator
from response.response_file import ResponseFile


scenarios("../features/product_crud.feature")

@given(parsers.parse('I have given payload type "{payload_type}"'))
def create_payload(context, payload_type):
    context["payload"]=PayloadGenerator.get_payload(payload_type)

@when("I Send a request to create the product")
def send_create_request(context, product_api):
    context["response"]=product_api.create_product(context["payload"])
    product_id = context["response"].json()["product"]["id"]
    context["product_id"] = product_id

@then("The product should be created successfully")
def verify_create(context):
    response=context["response"]
    payload=context["payload"]
    # print(response.status_code)
    data=response.json()
    ResponseFile.response_validate(data, payload, parent_key="product", message="Product added successfully")


@when("I request all products")
def get_all_products(context,product_api):
    context["response"]=product_api.get_all_products()

@then("I Should recieve list of products")
def validate_product_list(context):
    response=context["response"].json()
    # print(response)
    assert isinstance(response,list)

@when("I Send a request to get the product")
def get_product_by_id(context, product_api ):
    product_id=context["product_id"]
    response = product_api.get_product_by_id(product_id)
    context["response"]=response

@then("The product should be fetched successfully")
def validate_get_by_id_response(context):
    payload=context['payload']
    data=context["response"].json()
    ResponseFile.response_validate(data, payload)

@when("Update the product with new details")
def update_the_product(context, product_api):
    product_id = context["product_id"]
    update_payload = PayloadGenerator.get_payload("generate-update", product_id)
    context["update_payload"]=update_payload
    response = product_api.update_product(update_payload)
    context["response"]=response.json()

@then("The product should be updated successfully")
def validate_updated_product(context):
    update_payload=context["update_payload"]
    data=context["response"]
    ResponseFile.response_validate(data, update_payload, parent_key="product", message="Product updated successfully")

@when("Send a request to Delete the product")
def delete_the_product(context,product_api):
    product_id = context["product_id"]
    response=product_api.delete_product(product_id)
    context["response"]=response.json()

@then("The product should be deleted successfully")
def validate_deleted_product(context):
    data=context["response"]
    ResponseFile.response_validate(data, message="Product deleted successfully")

