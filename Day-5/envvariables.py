import os

# Accessing an environment variable
api_key = os.environ.get("MY_API_KEY")
if api_key:
    print(f"API Key: {api_key}")
else:
    print("MY_API_KEY environment variable not set.")

# Setting an environment variable (for the current process)
os.environ["TEMP_VAR"] = "temporary_value"
print(f"TEMP_VAR: {os.environ.get('TEMP_VAR')}")
# Note: Changes to os.environ only affect the current process and its children.
# To permanently set environment variables, you typically do this outside of Python, in your operating system or shell configuration.
# To make MY_API_KEY available before running the script (on Linux/macOS): export MY_API_KEY="your_secret_key"