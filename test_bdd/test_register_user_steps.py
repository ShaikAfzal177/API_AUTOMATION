from pytest_bdd import scenarios, given, when, then, parsers

from conftest import register_api
from data.payload_generator import PayloadGenerator
from data.registered_data import RegisteredData
from response.response_file import ResponseFile


scenarios("../features/register_user.feature")


@given(parsers.parse('I have given payload type "{payload_type}"'))
def create_payload(context, payload_type):
    context["payload"]=PayloadGenerator.get_payload(payload_type)

@when("I send a request to register the user")
def send_create_request(context, register_api):
    context["response"]=register_api.register_user(context["payload"])
    username=context["payload"]["username"]
    context["username"]=username

@then("User should registered successfully")
def validate_register_user(context):
    data=context["response"].json()
    user_name=context["username"]
    ResponseFile.response_validate(data, user=user_name, message="User registered successfully")

@then("Save register user data in yaml file")
def save_register_data(context, yaml_file):
    payload=context["payload"]
    RegisteredData.save_register_data(yaml_file, payload)

@then(parsers.parse('User should get "{response_message}" as response'))
def validate_register_user_response(context, response_message):
    response=context["response"].json()
    assert response["detail"] == response_message
    print(response)
@when(parsers.parse('I have send a request to login with valid users "{username}" and "{password}"'))
def login_valid_user(context,register_api,username, password):
    registered_user={"username":username, "password":password}
    context["response"] =register_api.login(payload=registered_user)

@then(parsers.parse('I will get "{response_message}" message as response'))
def login_response(context, response_message):
    data=context["response"].json()
    ResponseFile.response_validate(data, message=response_message)