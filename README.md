# multi_detector

## NOTES
 11,000 -> Positive Control Threshold
 2,000 -> Sample Limit of Detection
 ['105', '-499', '-1330', '-1359', '-2702', '-1392', '12601', '-899', '3545']

 print("Temp 105")
 print("  Sample 6 positive control passed.")
 print("  Sample 7 negative control passed.")
 print("  Sample 8 detected.")


 Sample 6 (positive control) passes b/c gt postive_control_threshold

 Sample 7 (negative control) passes b/c lt 0

 Sample 8 is detected b/c positive_control and negative_control passed and gt sample_limit_detection

 105, '-499', '-1330', '-1359', '-2702', '-1392', PASS, PASS, DETECTED
