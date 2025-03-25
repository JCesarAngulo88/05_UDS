import pandas as pd
import resources.data_base_general as guds # general UDS references
from apps.service22_class import Service22
import logging
from apps.csv_write import write_to_csv

# Set logging to show INFO messages in the console
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def create_did_supported_db(csv_file_generals_22: str = '', csv_file_specific_22: str = ''):
    """
    This function returns a dictionary of all valid DIDs in the requirements table
    inputs:
    param csv_file_supported_did is the path of the csv
    outputs:
    A dict with the key('id_ + did' from the csv) and value 'did' from the csv
    """
    did_generals = pd.read_csv(csv_file_generals_22)
    did_list_generals_supported = list(did_generals.iloc[0:5, 0])  # Get DID string from the table Example: did_supported ='1000'
    # print(type(did_list_supported))

    did_specific = pd.read_csv(csv_file_specific_22)
    did_list_specific_supported = list(did_specific.iloc[0:5, 0])

    # did_dict_supported: dict = {}
    # for item in did_list_supported:
    # did_completion = 'id_' + item
    # did_dict_supported.update({did_completion: item})
    # return did_dict_supported

    return {f'id_{did}': did for did in did_list_generals_supported}, {f'id_{did2}': did2 for did2 in did_list_specific_supported}

# def create_service22_tc_old(ecu_name: str = '', can_id: str = '') -> str:
#     # Create a dict of the DIDs declared in csv generals requirements
#     service22_data_base_generals, service22_data_base_specific = create_did_supported_db(guds.csv_generals_path,
#                                                                                          guds.csv_specific_path)
#     print(f'DIDs read {service22_data_base_generals}')
#     # service22_data_base_specific = create_did_supported_db(guds.csv_specific_path) # Return a dict of the DIDs declared in csv specific
#
#     # Chose what type of test scenario is going to be created
#     var_test_scenario = int(input(f'\nSelect: \n1. Basic Reading\n2. Diagnostic Session\n3. Incorrect Length\n'))
#
#     if can_id == guds.CAN_CLASSIC_PHYSICAL_ID:
#         # Test Cases Physical Address creation
#         for inc, values in enumerate(service22_data_base_generals.values()):
#             # Create an instance to Service 22 class
#             s22_testcase = Service22(ecu_name, can_id, guds.SERVICES_SUPPORTED['Service22'], values)
#             # Create a database of the did declare with all the specs
#             db_s22_did = s22_testcase.create_did_db(guds.csv_generals_path, guds.csv_specific_path, inc)
#             print(type(db_s22_did))
#             print(db_s22_did)
#
#             match var_test_scenario:
#                 case 1:
#                     print('1. Basic Reading selected')
#                     if db_s22_did['var_ID_Supported_Physical'] == 'Y' and db_s22_did['var_ID_Supported_Default'] == 'Y':
#                         basic_reading_tc = s22_testcase.create_test_scenario(guds.basic_positive_reading_template,
#                                                                              db_s22_did)  # Create test scenario to Basic Reading template
#                         print(basic_reading_tc)
#                     else:
#                         print(f'Test Case scenario doesnt apply for this DID {db_s22_did}')
#
#                 case 2:
#                     print('2. Diagnostic Sessions Selected')
#                     if db_s22_did['var_ID_Supported_Physical'] == 'Y' and db_s22_did['var_ID_Supported_Extended'] == 'Y' and db_s22_did['var_ID_Supported_BootLoader']:
#                         diag_sessions_tc = s22_testcase.create_test_scenario(guds.diag_sessions_positive_reading_template,
#                                                                              db_s22_did)  # Create test scenario to Diag Sessions template
#                         print(diag_sessions_tc)
#                     else:
#                         print(f'Test Case scenario doesnt apply for this DID {db_s22_did}')
#                 case 3:
#                     print('3. Incorrect Length Selected')
#                     if db_s22_did['var_ID_Supported_Physical'] == 'Y' and db_s22_did['var_ID_Supported_Default'] == 'Y':
#                         incorrect_length_reading_tc = s22_testcase.create_test_scenario(guds.incorrect_length_template,
#                                                                                   db_s22_did)  # Create test scenario to Functional template
#                         print(incorrect_length_reading_tc)
#                     else:
#                         print(f'Test Case scenario doesnt apply for this DID {db_s22_did}')
#                 case _:
#                     print(f'Error. No correct selection {var_test_scenario}')
#     elif can_id == guds.CAN_CLASSIC_FUNCTIONAL_ID:
#         # Test Cases Functional Address creation
#         for inc, values in enumerate(service22_data_base_generals.values()):
#             # Create an instance to Service 22 class
#             s22_testcase = Service22('IPC', guds.CAN_CLASSIC_FUNCTIONAL_ID, guds.SERVICES_SUPPORTED['Service22'],
#                                      values)
#             # Create a database of the did declare with all the specs
#             db_s22_did = s22_testcase.create_did_db(guds.csv_generals_path, guds.csv_specific_path, inc)
#             print(type(db_s22_did))
#             print(db_s22_did)
#
#             match var_test_scenario:
#                 case 1:
#                     if db_s22_did['var_ID_Supported_Functional'] == 'Y' and db_s22_did['var_ID_Supported_Default'] == 'Y':
#                         print('1. FA Basic Reading selected')
#                         fa_basic_reading_tc = s22_testcase.create_test_scenario(guds.fa_positive_reading_template,
#                                                                              db_s22_did)  # Create test scenario to Basic Reading template
#                         print(fa_basic_reading_tc)
#                 case 2:
#                     if db_s22_did['var_ID_Supported_Functional'] == 'Y' and db_s22_did[
#                         'var_ID_Supported_Extended'] == 'Y' and db_s22_did['var_ID_Supported_BootLoader']:
#                         print('2. FA Diagnostic Sessions Selected')
#                         fa_diag_sessions_tc = s22_testcase.create_test_scenario(guds.fa_diag_sessions_positive_reading_template,
#                                                                              db_s22_did)  # Create test scenario to Diag Sessions template
#                         print(fa_diag_sessions_tc)
#                 case 3:
#                     if db_s22_did['var_ID_Supported_Functional'] == 'Y' and db_s22_did['var_ID_Supported_Default'] == 'Y':
#                         print('3. FA Incorrect Length Selected')
#                         fa_incorrect_length_tc = s22_testcase.create_test_scenario(guds.fa_incorrect_length_template,
#                                                                                   db_s22_did)  # Create test scenario to Functional template
#                         print(fa_incorrect_length_tc)
#                 case _:
#                     print(f'Error. No correct selection {var_test_scenario}')
#     else:
#         print('Something went wrong, NO CAN ID SELECTED')
#
#     return 'Test Cases were created successfully'

def create_service22_tc(ecu_name: str = '', can_id: str = '', var_test_scenario: int = None) -> str:
    """
    Creates test cases for UDS service 22 based on specified ECU and CAN ID.

    Inputs:
        ecu_name (str): The ECU name.
        can_id (str): The CAN ID (physical or functional).
        var_test_scenario (int): The test scenario type (1: Basic Reading, 2: Diagnostic Session, 3: Incorrect Length).

    Returns:
        list: A list of generated test cases.
    """
    try:
        # Read DID databases
        service22_data_base_generals, service22_data_base_specific = create_did_supported_db(
            guds.csv_generals_path, guds.csv_specific_path
        )

        logging.info(f'DIDs read: {service22_data_base_generals}')

        # If test scenario is not provided, ask the user
        if var_test_scenario is None:
            var_test_scenario = int(input("\nSelect: \n1. Basic Reading\n2. Diagnostic Session\n3. Incorrect Length\n"))

        if not isinstance(ecu_name, str) or not isinstance(can_id, str) or not isinstance(var_test_scenario, int):
            logging.warning(f'Warning, ecu_name type is {type(ecu_name)}')
            logging.warning(f'Warning, can_id type is {type(can_id)}')
            logging.warning(f'Warning, the variable {var_test_scenario} is type {type(var_test_scenario)}')
            raise TypeError
        elif not 1 <= var_test_scenario <= 3:
            raise ValueError
        else:
            logging.info(f'Everything good with the type of values an Range of templates!! The type of var is: {type(var_test_scenario)}')

        can_id_type = 'Physical' if can_id == guds.CAN_CLASSIC_PHYSICAL_ID else 'Functional' if can_id == guds.CAN_CLASSIC_FUNCTIONAL_ID else None  # Define CAN ID type
        logging.info(f'The value of can_id_type is {can_id_type}')
        if not can_id_type:
            #logging.error("Something went wrong, NO CAN ID SELECTED")
            #print("Something went wrong, NO CAN ID SELECTED")
            #return 'Something went wrong, NO CAN ID SELECTED'  # return []
            raise Exception('Something went wrong, NO CAN ID SELECTED')

        #test_cases = []
        test_templates = {
            'Physical': {
                1: guds.basic_positive_reading_template,
                2: guds.diag_sessions_positive_reading_template,
                3: guds.incorrect_length_template
            },
            'Functional': {
                1: guds.fa_positive_reading_template,
                2: guds.fa_diag_sessions_positive_reading_template,
                3: guds.fa_incorrect_length_template
            }
        }

        # Iterate over the DIDs
        for inc, values in enumerate(service22_data_base_generals.values()):
            # Create an instance of Service22 class
            s22_testcase = Service22(ecu_name, can_id, guds.SERVICES_SUPPORTED['Service22'], values)
            db_s22_did = s22_testcase.create_did_db(guds.csv_generals_path, guds.csv_specific_path, inc)

            logging.info(f"DID database: {db_s22_did}")

            # Check if the selected scenario is valid
            template = test_templates[can_id_type].get(var_test_scenario)
            if not template:
                logging.error(f"Error. No correct selection {var_test_scenario}")
                return "Error. No correct selection"

            # Verify the conditions before creating a test case
            if db_s22_did.get(f'var_ID_Supported_{can_id_type}') == 'Y' and db_s22_did.get('var_ID_Supported_Default') == 'Y':
                test_case = s22_testcase.create_test_scenario(template, db_s22_did)
                write_to_csv(guds.csv_test_cases_result_path, test_case, inc + 1, 0)
                #test_cases.append(test_case)
                logging.info(f"Created test case: {test_case}")
            else:
                logging.warning(f'Test case scenario does not apply for this DID {db_s22_did}')
                # TODO: Check if we could create a error here
        return 'Valid Test Cases were created!' # if test_cases else ["No valid test cases were created"]

    except ValueError:
        logging.error("Invalid input! Please enter a number between 1 and 3.")
        raise ValueError('Invalid input, Select: \n1. Basic Reading\n2. Diagnostic Session\n3. Incorrect Length!\n')
    except TypeError as e:
        raise TypeError(f'Invalid input {e}! First variable must be a string, Second variable a string and third variable an integer')
    except KeyError as e:
        logging.error(f"Missing key in database: {e}")
    except FileNotFoundError as e:
        logging.error(f"CSV file not found: {e}")
    #except Exception as e:
        #logging.error(f"An unexpected error occurred: {e}")

    return 'Test Cases were created successfully'