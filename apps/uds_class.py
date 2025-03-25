#import resources.general_id as general
#import csv

class UDSGeneral:
    # TODO: read all assignations from a file
    author_name: str = 'Julio Angulo'
    actual_oem: str = 'Stellantis'
    actual_my: str = 'MY25'
    actual_project: str = 'RAM FDC'
    actual_variants: tuple = ('Long Horn', 'TRX')
    instance_count: int = 0
    all: list = []
    def __init__(self, ecu_name: str = '', can_id: str = '', services_supported: str = ''):
        if not isinstance(ecu_name, str) and not isinstance(services_supported, str) and not isinstance(can_id, str):
            raise TypeError('Invalid types: Params must be a string and `Service` must be an integer')
        
        #Assign to self object
        self.ecu_name = ecu_name
        self.can_id = can_id
        self.services_supported = services_supported

        # Action to execute when instance is called
        UDSGeneral.all.append(self)

        # Increase by one unit everytime constructor init is called
        UDSGeneral.instance_count += 1

    def __repr__(self): # Use to define a string representation of an object, de-bugging purposes
            return f'My {self.__class__.__name__} class: title={self.ecu_name}, CAN ID={self.can_id}, Services Supported={self.services_supported}'

    def __str__(self): # Use to debug, return a list of all classes details
        return f"The class is {self.__class__.__name__}"

    @classmethod
    def get_instance_count(cls):
        return cls.instance_count

    # Create Test Scenarios by replacing the keywords
    @staticmethod
    def create_test_scenario(tc_template: str = '', db_did2: dict = None) -> str:
        for key, value in db_did2.items():
            #print(f"The key is {key}, The value is {value}")
            tc_template = tc_template.replace(key, value)
        return tc_template