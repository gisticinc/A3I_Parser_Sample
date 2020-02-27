# Overview

This project includes samples to send request to A3I parse service.

User has to specify addresses to parse, project and model ID and a token containing authorization info. The token can be generated in LB Portal.

## python.py

The python sample uses requests library to send request. It's the basic usage of the API. When execute the script, please provide a valid A3I token. For example `python python.py a3i_token`

## python_excel_file.py

They python_excel_file sample take excel file as input. To use it, the user has to execute the script with excel path and column of addresses parameters. For example, `python python_excel_file.py path_to_your_data.xls full_address_column_name`. The script will generate a `result.xls` file at your current folder.