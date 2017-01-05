from __future__ import print_function
import csv

infile='data-in.csv'
outfile='data-out.csv'

positive_control_threshold = 11000
sample_limit_detection = 2000

with open(infile, mode='r') as infile:
    reader = csv.reader(infile)
    with open(outfile, 'a') as output:

        for row in reader:
            temp = row[0]
            sample_6 = float(row[6])
            sample_7 = float(row[7])
            sample_8 = float(row[8])

            postive_control_test = False
            negative_control_test = False
            patient_test = False

            # Pass/Fail positive and negative control tests
            if sample_6 > positive_control_threshold:
                postive_control_test = True
            if sample_7 < 0:
                negative_control_test = True
            # Pass/Fail patient test
            if postive_control_test and negative_control_test and sample_8 > sample_limit_detection:
                patient_test = True

            # Print this temperature's result
            # print("Temp: " + temp)
            # print("  Row Data: " + str(row))

            # Print Positive Control Result
            postive_control_test_result = ""
            if postive_control_test:
                # print("  Sample 6 positive control passed.")
                postive_control_test_result="PASS"
            else:
                # print("  Sample 6 positive control failed.")
                postive_control_test_result="FAIL"

            # Print Negative Control Result
            negative_control_test_result = ""
            if negative_control_test:
                # print("  Sample 7 negative control passed.")
                negative_control_test = "PASS"
            else:
                # print("  Sample 7 negative control failed.")
                negative_control_test = "FAIL"

            patient_test_result = ""
            if patient_test:
                # print("  Sample 8 detected.")
                patient_test_result = "PASS"
            else:
                # print("  Sample 8 not detected.")
                patient_test_result = "FAIL"

            data = ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (temp, row[1], row[2], row[3], row[4], row[5], row[6], postive_control_test_result, negative_control_test, patient_test_result))
            print(data)
            output.write(data + '\n')

