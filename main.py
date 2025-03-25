import sys
import resources.data_base_general as guds # general UDS references
#from apps.service22_class import Service22
#from apps.service2F_class import Service2F
#from apps.uds_class import UDSGeneral
from apps.user_db import UserLoginApp
from apps.create_tc import create_service22_tc
#import apps.user_features as uf
from apps.csv_write import csv_file_init


def say_hello(name: str = '') -> None:
    print(f'Hello and welcome {name}')

def main():
    say_hello('Julio')
    csv_file_init()
    #####  Debugging #####
    # Creating book objects or crating instances of the UDSGeneral Class
    # uds_general = UDSGeneral('DCSD', 'Physical', '2E')
    # uds_service22 = Service22('IPC', 'CANFD_Physical', '19', '1001')
    # uds_service2f = Service2F('HUD', 'CAN_Classic_Functional', '2F', '100A')

    # Checking Classes details
    # print(f'UDS details {uds_general}') # Str use
    # print(f'Service22 details {uds_service22}') # Str use
    # print(f'Service2F details {uds_service2f}') # str use
    # result_classes = [uds_general, uds_service22, uds_service2f] # Create a general list of strings of the classes
    # print(f'The type is {type(result_classes)}, The content is {result_classes}') # repr use
    #
    # print(f'The number of all Test Cases is {uds_general.get_instance_count()}')
    # print(f'The number of Test Cases created by Service22 {uds_service22.get_instance_count_service22()}')
    # print(f'The number of Test Cases created by Service2F {uds_service2f.get_instance_count_service2f()}')
    ############

    ##### Testing user_feature.py functions #####
    # uf.setup_database()

    # # Register some users (you can comment this out after the first run)
    # uf.register_user("user1", "pass123", "ProjectA")
    # uf.register_user("user2", "pass456", "ProjectB")
    # uf.register_user('JulioAngulo', 'JA123', 'UDS_Champs')
    #
    # # Login
    # if uf.user_login():
    #     print("Welcome to the app!")
    # else:
    #     print("Exiting the app.")
    ###############################################

    ####### Testing user_db.py methods ############
    # userdb = UserLoginApp()
    # userdb.register_users()
    # # Login
    # if userdb.login():
    #     print("Welcome to the app!")
    #     if sys.argv[1].lower() == 'physical':
    #         tc_result = create_service22_tc(guds.ECUS['STELLANTIS_IPC'], guds.CAN_CLASSIC_PHYSICAL_ID)
    #         print(f'{tc_result}, check the tcs in the {guds.result_path}')
    #     elif sys.argv[1].lower() == 'functional':
    #         tc_result = create_service22_tc(guds.ECUS['STELLANTIS_IPC'], guds.CAN_CLASSIC_FUNCTIONAL_ID)
    #         print(f'{tc_result}, check the tcs in the {guds.result_path}')
    #     else:
    #         print('Command execution fail, check arguments')
    # else:
    #     print("Exiting the app.")
    ############################################################

########################### With Error handling #######################
    try:
        userdb = UserLoginApp()
        userdb.register_users()
        # Login
        if userdb.login():
            # Check if the correct number of arguments is provided
            if len(sys.argv) != guds.MAX_ARGS_EXE_COMMAND: # Valid command -> python3 main.py physical 1
                raise ValueError("Incorrect number of arguments. Usage: python3 main.py 'str: Arg1' 'int: Arg2'")

            #Check if the command contains arguments: Physical, Functional and an integer range: 1-2
            if sys.argv[1].lower() == 'physical' and 1 <= int(sys.argv[2]) <= 3:
                tc_result = create_service22_tc(guds.ECUS['STELLANTIS_IPC'], guds.CAN_CLASSIC_PHYSICAL_ID, int(sys.argv[2]))
                print(f'{tc_result}, check the tcs in the {guds.result_path}')
            elif sys.argv[1].lower() == 'functional' and 1 <= int(sys.argv[2]):
                tc_result = create_service22_tc(guds.ECUS['STELLANTIS_IPC'], guds.CAN_CLASSIC_FUNCTIONAL_ID, int(sys.argv[2]))
                print(f'{tc_result}, check the tcs in the {guds.result_path}')
            else:
                raise ValueError("First argument must be 'physical' or 'functional', and second must be between 1 and 3.")
        else:
            print("Exiting the app.")
    except ValueError as e:
        raise ValueError(f'Error: Second argument {e}')
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
#####################################################################



if __name__ == "__main__":
    main()
