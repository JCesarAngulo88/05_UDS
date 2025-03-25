from typing import Final

ECUS: Final[dict] = {
    'STELLANTIS_IPC': 'IPC',
    'STELLANTIS_FDC': 'FDC',
    'FORD_HUD': 'HUD'
}

TEST_SCENARIOS: Final[dict] = {
    'Basic Reading': 1,
    'Diagnostic Session': 2,
    'Incorrect Length': 3
}

CAN_CLASSIC_PHYSICAL_ID: Final[str] = "1096DAF1"
CAN_FD_PHYSICAL_ID: Final[str] = "1096DAF2"
CAN_CLASSIC_FUNCTIONAL_ID: Final[str] = "1096FEF1"
CAN_FD_FUNCTIONAL_ID: Final[str] = "1096FEF2"

MAX_ARGS_EXE_COMMAND: Final[int] = 3

#GENERIC_PAYLOAD: Final[str] = "XX.."

#SERVICES_SUPPORTED: tuple = ("22", "2E", "2F")
SERVICES_SUPPORTED: dict = {
    'Service22': '22',
    'Service2E': '2E',
    'Service2F': '2F'
}

csv_generals_path = '/Users/jcesar/Documents/Programming_Python/Personal/05_UDS/csv_files/Services.csv'
csv_specific_path = '/Users/jcesar/Documents/Programming_Python/Personal/05_UDS/csv_files/General IDs-Table 1.csv'
result_path = '/Users/jcesar/Documents/Programming_Python/Personal/05_UDS/results_files/service22_tc.txt'
csv_test_cases_result_path = '/Users/jcesar/Documents/Programming_Python/Personal/05_UDS/results_files/service22_tc.csv'

basic_positive_reading_template: str = 'Verify {var_ECU} responds positive to DID {var_DID} and with data length of {var_DataLength} under below conditions:\n \
    Physical Address {var_ID_Supported_Physical}\n \
    Default Session {var_ID_Supported_Default}\n \
    Security Level {var_Security} \n \
    Preconditions:\n \
    - Turn On ECU\n \
    - Set Default Session\n \
    Steps:\n \
    1.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID}\n \
    Expected:\n \
    1.- ECU responds: {var_DataLength} {var_Positive_Response}'

diag_sessions_positive_reading_template: str = 'Verify {var_ECU} responds positive to DID {var_DID} and with data length of {var_DataLength} under below conditions:\n \
    Physical Address {var_ID_Supported_Physical}\n \
    Extended Session {var_ID_Supported_Extended}\n \
    BootLoader Session {var_ID_Supported_BootLoader}\n \
    Security Level {var_Security} \n \
    Preconditions:\n \
    - Turn On ECU\n \
    - Set Default Session\n \
    Steps:\n \
    1.- Change to Extended Session by sending: 10 03\n \
    2.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID}\n \
    3.- Change to Bootloader Session by sending: 10 02\n \
    4.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID}\n \
    Expected:\n \
    1.- Check {var_ECU} set correctly Extended Session by sending respective reading\n \
    2.- ECU responds: {var_DataLength} {var_Positive_Response}\n \
    3.- Check {var_ECU} set correctly Bootloader Session by sending respective reading\n \
    4.- ECU responds: {var_DataLength} {var_Positive_Response}\n'

fa_positive_reading_template: str = 'Verify {var_ECU} responds positive to DID {var_DID} and with data length of {var_DataLength} under below conditions:\n \
    Functional Address {var_ID_Supported_Functional}\n \
    Default Session {var_ID_Supported_Default}\n \
    Security Level {var_Security} \n \
    Preconditions:\n \
    - Turn On ECU\n \
    - Set Default Session\n \
    Steps:\n \
    1.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID}\n \
    Expected:\n \
    1.- ECU responds: {var_DataLength} {var_Positive_Response}'

fa_diag_sessions_positive_reading_template: str = 'Verify {var_ECU} responds positive to DID {var_DID} and with data length of {var_DataLength} under below conditions:\n \
    Functional Address {var_ID_Supported_Physical}\n \
    Extended Session {var_ID_Supported_Extended}\n \
    BootLoader Session {var_ID_Supported_BootLoader}\n \
    Security Level {var_Security} \n \
    Preconditions:\n \
    - Turn On ECU\n \
    - Set Default Session\n \
    Steps:\n \
    1.- Change to Extended Session by sending: 10 03\n \
    2.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID}\n \
    3.- Change to Bootloader Session by sending: 10 02\n \
    4.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID}\n \
    Expected:\n \
    1.- Check {var_ECU} set correctly Extended Session by sending respective reading\n \
    2.- ECU responds: {var_DataLength} {var_Positive_Response}\n \
    3.- Check {var_ECU} set correctly Bootloader Session by sending respective reading\n \
    4.- ECU responds: {var_DataLength} {var_Positive_Response}\n'

incorrect_length_template: str = 'Verify ECU responds negative to DID {var_DID} and NRC of 0x13 under below conditions:\n \
    Physical Address {var_ID_Supported_Functional}\n \
    Default Session {var_ID_Supported_Default}\n \
    Incorrect Length \n \
    Preconditions:\n \
    - Turn On ECU\n \
    - Set Default Session\n \
    Steps:\n \
    1.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID} 00\n \
    2.- Change to Extended Session by sending: 10 03\n \
    3.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID} 00\n \
    4.- Change to Bootloader Session by sending: 10 02\n \
    5.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID} 00\n \
    Expected:\n \
    1.- ECU responds: 03 7F {var_Service} 13\n \
    2.- Check {var_ECU} set correctly Extended Session by sending respective reading\n \
    3.- ECU responds: 03 7F {var_Service} 13\n \
    4.- Check {var_ECU} set correctly Bootloader Session by sending respective reading\n \
    5.- ECU responds: 03 7F {var_Service} 13\n'

fa_incorrect_length_template: str = 'Verify ECU responds negative to DID {var_DID} and NRC of 0x13 under below conditions:\n \
    Functional Address {var_ID_Supported_Functional}\n \
    Default Session {var_ID_Supported_Default}\n \
    Incorrect Length \n \
    Preconditions:\n \
    - Turn On ECU\n \
    - Set Default Session\n \
    Steps:\n \
    1.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID} 00\n \
    2.- Change to Extended Session by sending: 10 03\n \
    3.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID} 00\n \
    4.- Change to Bootloader Session by sending: 10 02\n \
    5.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID} 00\n \
    Expected:\n \
    1.- ECU responds: 03 7F {var_Service} 13\n \
    2.- Check {var_ECU} set correctly Extended Session by sending respective reading\n \
    3.- ECU responds: 03 7F {var_Service} 13\n \
    4.- Check {var_ECU} set correctly Bootloader Session by sending respective reading\n \
    5.- ECU responds: 03 7F {var_Service} 13\n'

basic_negative_reading_template: str = 'Verify ECU responds negative to DID {var_DID} and NRC of {var_NRC} under below conditions:\n \
    Functional Address {var_ID_Supported_Functional}\n \
    Default Session {var_ID_Supported_Default}\n \
    Preconditions:\n \
    - Turn On ECU\n \
    - Set Default Session\n \
    Steps:\n \
    1.- Send by {var_CAN_ID} diagnostic request: {var_Service} {var_DID}\n \
    Expected:\n \
    1.- ECU responds: 03 7F {var_Service} one of the next: {var_NRC}'
