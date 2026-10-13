# Sales Data Calculator — Test Cases

## Testing Objective

To verify the accuracy of sales calculations and the program's ability to handle invalid data.

## Test Cases

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC01 | Run with the supplied sample dataset | 10 sales records |
| TC02 | Calculate total sales | ₹1,90,000 |
| TC03 | Calculate average sales | ₹19,000 |
| TC04 | Identify highest sale | ₹30,000 |
| TC05 | Identify lowest sale | ₹10,000 |
| TC06 | Use an empty sales list | Display an error |
| TC07 | Use a negative sale value | Reject invalid data |
| TC08 | Use a non-numeric value | Reject invalid data |
| TC09 | Use a single sale of 5000 | All four statistics equal 5000 |
| TC10 | Use repeated values of 1000 | Correct total, average, maximum, and minimum |
| TC11 | Include a zero sales value | Accept zero as valid |

## Test Execution Record

After running each test, enter the actual results and update the status.

| Test ID | Actual Result | Status |
|---|---|---|
| TC01–TC11 | Record after execution | Pending |

## Testing Conclusion

The purpose of testing is to ensure that the program calculates sales statistics correctly and handles invalid or empty datasets appropriately.

Actual results should be recorded after the tests are completed.
