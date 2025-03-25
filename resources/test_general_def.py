from typing import Final

###### test_create_tc.py #####

# Test Case 1
expected_positive_ctc: Final[str] = 'Valid Test Cases were created!'

# Test Case 2
invalid_values_tc = [0, 4, 5, 6, 7, 8, 9, 10]  # List of invalid values


# Test Case 3
INVALID_CAN_ID = [
    ('IPC', '1096D9F1', 1),
    ('IPC', '1096DBF1', 1),
    ('IPC', '1096DAF0', 1),
    ('IPC', '1096DAF3', 1),
    ('IPC', '0196D9F1', 1),
]