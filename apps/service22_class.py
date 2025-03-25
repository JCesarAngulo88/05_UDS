from apps.uds_class import UDSGeneral
import pandas as pd  # Add pandas import

class Service22(UDSGeneral):
    instance_count_service22: int = 0
    def __init__(self, ecu_name: str = '', can_id: str = '', services_supported: str = '', dids_supported: str = ''):
        super().__init__(
            ecu_name, can_id, services_supported
        )
        # Assign to self object
        self.dids_supported = dids_supported

        Service22.instance_count_service22 += 1

    def __repr__(self):
        return f"My {self.__class__.__name__} class: title='{self.ecu_name}', CAN ID = '{self.can_id}', Service Supported = '{self.services_supported}', DIDs supported = '{self.dids_supported}')"

    def __str__(self):
        return f"The Class is {self.__class__.__name__}"

    @classmethod
    def get_instance_count_service22(cls):
        return cls.instance_count_service22

    # def create_did_db(self, csv_file_generals_22: str, csv_file_specific_22: str, inc: int = 0) -> dict:
    #     """
    #     This function creates a dictionary with all the requirements to each read from the CSV files official requirements.
    #
    #     Args:
    #         csv_file_generals_22: Path to the general parameters CSV file
    #         csv_file_specific_22: Path to the specific parameters CSV file
    #         inc: Iteration of all the values from dictionary
    #
    #     Returns:
    #         dict: Dictionary containing DID service parameters
    #     """
    #     db_did_service22 = {}
    #     generals_get_did_supported_default = ''
    #     generals_get_did_supported_extended = ''
    #     generals_did_supported_bootloader = ''
    #     generals_did_supported_security = ''
    #     generals_did_supported_physical_address = ''
    #     generals_did_supported_functional_address = ''
    #     # Read the CSV files
    #     df = pd.read_csv(csv_file_generals_22)
    #     df2 = pd.read_csv(csv_file_specific_22)
    #
    #     print(f'Increment is {inc}')
    #     generals_get_did = df.iloc[inc, 0]  # Get DID supported value
    #     match generals_get_did:
    #         case '1000':
    #             print('I got 1000')
    #             # Get values from DataFrames
    #             generals_get_did_supported_default = df.iloc[inc, 1]  # Get DID supported in Default Session
    #             generals_get_did_supported_extended = df.iloc[inc, 2]  # Get DID supported in Extended Session
    #             generals_did_supported_bootloader = df.iloc[inc, 3]  # Get DID supported in Programming Session
    #             generals_did_supported_security = df.iloc[inc, 4]  # Get DID security supported
    #             generals_did_supported_physical_address = df.iloc[inc, 5]  # Get DID Physical Address Supported
    #             generals_did_supported_functional_address = df.iloc[inc, 6]  # Get DID Functional Address Supported
    #         case '1001':
    #             print('I got 1001')
    #             # Get values from DataFrames
    #             generals_get_did_supported_default = df.iloc[inc, 1]  # Get DID supported in Default Session
    #             generals_get_did_supported_extended = df.iloc[inc, 2]  # Get DID supported in Extended Session
    #             generals_did_supported_bootloader = df.iloc[inc, 3]  # Get DID supported in Programming Session
    #             generals_did_supported_security = df.iloc[inc, 4]  # Get DID security supported
    #             generals_did_supported_physical_address = df.iloc[inc, 5]  # Get DID Physical Address Supported
    #             generals_did_supported_functional_address = df.iloc[inc, 6]  # Get DID Functional Address Supported
    #         case '1003':
    #             print('I got 1003')
    #             # Get values from DataFrames
    #             generals_get_did_supported_default = df.iloc[inc, 1]  # Get DID supported in Default Session
    #             generals_get_did_supported_extended = df.iloc[inc, 2]  # Get DID supported in Extended Session
    #             generals_did_supported_bootloader = df.iloc[inc, 3]  # Get DID supported in Programming Session
    #             generals_did_supported_security = df.iloc[inc, 4]  # Get DID security supported
    #             generals_did_supported_physical_address = df.iloc[inc, 5]  # Get DID Physical Address Supported
    #             generals_did_supported_functional_address = df.iloc[inc, 6]  # Get DID Functional Address Supported
    #         case '1010':
    #             print('I got 1010')
    #             # Get values from DataFrames
    #             generals_get_did_supported_default = df.iloc[inc, 1]  # Get DID supported in Default Session
    #             generals_get_did_supported_extended = df.iloc[inc, 2]  # Get DID supported in Extended Session
    #             generals_did_supported_bootloader = df.iloc[inc, 3]  # Get DID supported in Programming Session
    #             generals_did_supported_security = df.iloc[inc, 4]  # Get DID security supported
    #             generals_did_supported_physical_address = df.iloc[inc, 5]  # Get DID Physical Address Supported
    #             generals_did_supported_functional_address = df.iloc[inc, 6]  # Get DID Functional Address Supported
    #         case '101A':
    #             print('I got 101A')
    #             # Get values from DataFrames
    #             generals_get_did_supported_default = df.iloc[inc, 1]  # Get DID supported in Default Session
    #             generals_get_did_supported_extended = df.iloc[inc, 2]  # Get DID supported in Extended Session
    #             generals_did_supported_bootloader = df.iloc[inc, 3]  # Get DID supported in Programming Session
    #             generals_did_supported_security = df.iloc[inc, 4]  # Get DID security supported
    #             generals_did_supported_physical_address = df.iloc[inc, 5]  # Get DID Physical Address Supported
    #             generals_did_supported_functional_address = df.iloc[inc, 6]  # Get DID Functional Address Supported
    #
    #         case default:
    #             print(f'Case = {default}, do nothing')
    #
    #     specific_get_data_length = df2.iloc[0, 4]  # Get data length from first row, column E
    #     specific_get_positive_response = df2.iloc[0, 3]  # Get positive response from first row, column D
    #     specific_get_nrc = df2.iloc[0, 6]
    #
    #     # Build the dictionary with all required parameters
    #     # db_did_service22['var_DID'] = generals_get_did
    #     # db_did_service22['var_CAN_ID'] = self.CAN_ID
    #     # db_did_service22['var_Service'] = self.services_supported
    #     # db_did_service22['var_DataLength'] = str(specific_get_data_length)
    #     # db_did_service22['var_Positive_Response'] = specific_get_positive_response
    #
    #     db_did_service22.update({'var_ECU': self.ecu_name})
    #     db_did_service22.update({'var_CAN_ID': self.can_id})
    #     db_did_service22.update({'var_Service': self.services_supported})
    #     db_did_service22.update({'var_DID': self.dids_supported})
    #     db_did_service22.update({'var_ID_Supported_Physical': generals_did_supported_physical_address})
    #     db_did_service22.update({'var_ID_Supported_Functional': generals_did_supported_functional_address})
    #     db_did_service22.update({'var_ID_Supported_Default': generals_get_did_supported_default})
    #     db_did_service22.update({'var_ID_Supported_Extended': generals_get_did_supported_extended})
    #     db_did_service22.update({'var_ID_Supported_BootLoader': generals_did_supported_bootloader})
    #     db_did_service22.update({'var_Security': generals_did_supported_security})
    #     db_did_service22.update({'var_DataLength': str(specific_get_data_length)})
    #     db_did_service22.update({'var_Positive_Response': specific_get_positive_response})
    #     db_did_service22.update({'var_NRC': specific_get_nrc})
    #
    #     return db_did_service22

    def create_did_db(self, csv_file_generals_22: str, csv_file_specific_22: str, inc: int = 0) -> dict:
        """
        Creates a dictionary with UDS DID parameters from CSV files.

        Args:
            csv_file_generals_22: Path to the general parameters CSV file.
            csv_file_specific_22: Path to the specific parameters CSV file.
            inc: Row index for reading values.

        Returns:
            dict: Dictionary containing DID service parameters.
        """
        df = pd.read_csv(csv_file_generals_22)
        df2 = pd.read_csv(csv_file_specific_22)

        print(f'Increment is {inc}')

        generals_get_did = df.iloc[inc, 0]  # Get DID supported value
        generals_did_column_map = {
            '1000': [1, 2, 3, 4, 5, 6],
            '1001': [1, 2, 3, 4, 5, 6],
            '1003': [1, 2, 3, 4, 5, 6],
            '1010': [1, 2, 3, 4, 5, 6],
            '101A': [1, 2, 3, 4, 5, 6]
        }

        if generals_get_did in generals_did_column_map:
            print(f'Getting data from generals {generals_get_did}')
            col_indices = generals_did_column_map[generals_get_did]
            (
                generals_get_did_supported_default,
                generals_get_did_supported_extended,
                generals_did_supported_bootloader,
                generals_did_supported_security,
                generals_did_supported_physical_address,
                generals_did_supported_functional_address
            ) = df.iloc[inc, col_indices].tolist()
        else:
            print(f'Case = {generals_get_did}, do nothing')
            return {}
        specific_get_did = df2.iloc[inc, 0]
        specific_column_map = {
            '1000': [3, 4, 6],
            '1001': [3, 4, 6],
            '1003': [3, 4, 6],
            '1010': [3, 4, 6],
            '101A': [3, 4, 6]
        }
        if specific_get_did in specific_column_map:
            print(f'Getting data form specific {specific_get_did}')
            col_indices = specific_column_map[specific_get_did]
            (
                specific_get_positive_response, # Data length from column E
                specific_get_data_length, # Positive response from column D
                specific_get_nrc,  # NRC value from column G
            ) = df2.iloc[inc, col_indices].tolist()
        else:
            print(f'Case = {generals_get_did}, do nothing')
            return {}


        return {
            'var_ECU': self.ecu_name,
            'var_CAN_ID': self.can_id,
            'var_Service': self.services_supported,
            'var_DID': self.dids_supported,
            'var_ID_Supported_Physical': generals_did_supported_physical_address,
            'var_ID_Supported_Functional': generals_did_supported_functional_address,
            'var_ID_Supported_Default': generals_get_did_supported_default,
            'var_ID_Supported_Extended': generals_get_did_supported_extended,
            'var_ID_Supported_BootLoader': generals_did_supported_bootloader,
            'var_Security': generals_did_supported_security,
            'var_DataLength': specific_get_data_length,
            'var_Positive_Response': specific_get_positive_response,
            'var_NRC': specific_get_nrc
        }