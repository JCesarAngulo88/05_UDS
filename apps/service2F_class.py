from apps.uds_class import UDSGeneral

class Service2F(UDSGeneral):
    instance_count_service2F = 0
    def __init__(self, ecu_name: str = '', can_id: str = '', services_supported: str = '', dids_supported: str = '', led: str = ''):
        super().__init__(
            ecu_name, can_id, services_supported
        )

        self.dids_supported = dids_supported
        self.led = led
        Service2F.instance_count_service2F += 1

    def __repr__(self):
        return f"My {self.__class__.__name__} class title='{self.ecu_name}', CAN ID = '{self.can_id}', Service Supported = '{self.services_supported}', DIDs supported = '{self.dids_supported}')"

    @classmethod
    def get_instance_count_service2f(cls):
        return cls.instance_count_service2F
