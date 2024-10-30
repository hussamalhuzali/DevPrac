from behave import given, when, then
from app import app
from bs4 import BeautifulSoup

@given('the Flask calculator is running')
def step_flask_calculator_running(context):
    context.client = app.test_client()

@when('I add {a:d} and {b:d}')
def step_add_numbers(context, a, b):
    response = context.client.post('/add', data={'a': a, 'b': b})
    context.result = extract_result_from_html(response.data)

@when('I subtract {b:d} from {a:d}')
def step_subtract_numbers(context, a, b):
    # Corrected: to subtract `b` from `a` based on the feature file
    response = context.client.post('/subtract', data={'a': a, 'b': b})
    context.result = extract_result_from_html(response.data)

@when('I divide {a:d} by {b:d}')
def step_divide_numbers(context, a, b):
    response = context.client.post('/divide', data={'a': a, 'b': b})
    context.result = extract_result_from_html(response.data)

@then('the result should be {expected_result:d}')
def step_check_result_numeric(context, expected_result):
    # Convert the result to a float first, then to an integer if it matches an int value
    result_float = float(context.result)
    if result_float.is_integer():
        result_value = int(result_float)
    else:
        result_value = result_float
    assert expected_result == result_value, f'Expected "{expected_result}", but got "{result_value}"'

@then('the result should be "{expected_message}"')
def step_check_result_string(context, expected_message):
    assert expected_message == context.result, f'Expected "{expected_message}", but got "{context.result}"'

# Helper function to extract the result from HTML content
def extract_result_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Assuming the result is inside a <div id="result">
    result_tag = soup.find('div', id='result')
    if result_tag:
        return result_tag.text.strip()
    else:
        raise ValueError("Could not find the result in the HTML response")
