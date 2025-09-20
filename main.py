import os
import sys
from dotenv import load_dotenv
from google import genai

# Global Variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Error Message Strings
error_not_a_string = [
    'The prompt provided was not a string.',
    'Please make sure when you input the prompt that is formatted with "".',
    'Example: "This is a text prompt"'
]
error_invalid_prompt_length = ['The prompt provided must be at least one character long.']

# Decorator for Output
def decorator_function(function_to_run):
    def wrapper_function(*args, **kwargs):
        print("-"*75)
        value = function_to_run(*args, **kwargs)
        print("-"*75)
        return value
    return wrapper_function

# Error Message Output
@decorator_function
def error_message(error_text):
    return print(*error_text,sep='\n')

# Sanitize Input
def check_prompt(error, not_string_msg, zero_length_msg):
    op_code = 99999
    try:
        (sys.argv[1]) == str
    except Exception:
        error(not_string_msg)
        op_code = 1
        return op_code
    if len(sys.argv[1]) <= 0:
        error(zero_length_msg)
        op_code = 1
        return op_code
    op_code = 0
    return op_code

# Execute the Prompt and Print the Response
@decorator_function
def run_prompt(prompt_contents):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=prompt_contents
        )
    llm_response = [
        print(response.text),
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}"),
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    ]
    return llm_response[0], llm_response[1], llm_response[2]


def main(check, errormsgfunc, errormsg1, errormsg2, run):
    op_code_returned = check(errormsgfunc, errormsg1, errormsg2)
    if op_code_returned != 0:
        exit(1)
    else:
        run(sys.argv[1])


if __name__ == "__main__":
    main(check_prompt, error_message, error_not_a_string, error_invalid_prompt_length, run_prompt)
