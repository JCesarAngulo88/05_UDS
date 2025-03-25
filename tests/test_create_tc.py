import pytest
import apps.create_tc as c_tc
import resources.data_base_general as guds
import resources.test_general_def as tgen

# Execution commands: pytest -v test_create_tc.py or pytest -rA -rf -v -m prio3

@pytest.mark.parametrize('ecu, can_id, test_template, expected', [
    (guds.ECUS['STELLANTIS_IPC'], guds.CAN_CLASSIC_PHYSICAL_ID, guds.TEST_SCENARIOS['Basic Reading'], tgen.expected_positive_ctc),
    (guds.ECUS['STELLANTIS_IPC'], guds.CAN_CLASSIC_PHYSICAL_ID, guds.TEST_SCENARIOS['Diagnostic Session'], tgen.expected_positive_ctc),
    (guds.ECUS['STELLANTIS_IPC'], guds.CAN_CLASSIC_PHYSICAL_ID, guds.TEST_SCENARIOS['Incorrect Length'], tgen.expected_positive_ctc)
])
@pytest.mark.prio1
@pytest.mark.smoke
def test_create_service22_tc_1(ecu, can_id, test_template, expected):
    """
    Test Prio1
    """
    result = c_tc.create_service22_tc(ecu, can_id , test_template)
    assert result == expected
    #print(f'\nTest passed for inputs:\n{guds.ECUS['STELLANTIS_IPC']}, expected: {expected} and actual: {c_tc.create_service22_tc(ecu, can_id , test_template)}')

@pytest.mark.parametrize('ecu, can_id, test_template', [
    (guds.ECUS['STELLANTIS_IPC'], guds.CAN_CLASSIC_PHYSICAL_ID, invalid_value)
    for invalid_value in tgen.invalid_values_tc
])
@pytest.mark.prio2
@pytest.mark.regression
def test_create_service22_tc_2(ecu, can_id, test_template):
    """
    Test Prio2
    """
    with pytest.raises(ValueError) as error:
        c_tc.create_service22_tc(ecu, can_id , test_template)
    assert str(error.value) == 'Invalid input, Select: \n1. Basic Reading\n2. Diagnostic Session\n3. Incorrect Length!\n'
    #result = c_tc.create_service22_tc(ecu, can_id , test_template)
    #assert result == expected
    #print(f'\nTest passed for inputs:\n{guds.ECUS['STELLANTIS_IPC']}, expected: {expected} and actual: {c_tc.create_service22_tc(ecu, can_id , test_template)}')

@pytest.mark.parametrize('ecu, can_id, test_template', tgen.INVALID_CAN_ID)
@pytest.mark.prio3
@pytest.mark.regression
def test_create_service22_tc_3(ecu, can_id, test_template):
    """
    Test Prio3: Verifies that an Exception is raised for invalid CAN IDs.
    """
    with pytest.raises(Exception) as exception_info:
        c_tc.create_service22_tc(ecu, can_id, test_template)
    assert str(exception_info.value) == 'Something went wrong, NO CAN ID SELECTED'

