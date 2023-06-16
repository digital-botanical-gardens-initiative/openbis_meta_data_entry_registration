# openbis_meta_data_entry_registration
Collection to store python (openBIS pyBIS) scripts to register new metadata entries into the ELN LIMS openBIS

# openBIS Property Registration Script
This Python script is used to read properties from an Excel file and register them in the openBIS database if they are not already registered.

## Prerequisites
To run this script, you need:
- Python 3.6 or higher
- `pandas` Python package
- `pybis` Python package
- `getpass` Python package

You also need to have an Excel file named 'openbis_object_observation_properties_revised.xlsx' in the same directory as the script.

The Excel file should have columns named 'Code', 'Label', 'Description', and 'Data Type'.

## Usage under Linux/Ubuntu
Before running the script, please, provide your openBIS login to connect to the openBIS instance by modifying the line:
 o.login('<your_openbis_login>', password, save_token=True) 

## To run the script: 
1.	Navigate to the directory containing the script and the Excel file with the properties to be registered.
2.	Run the following command:
python3 ./DBGI_openBIS_pybis_object_and_property_registrator.py
3.	Provide your openBIS login password. 
