import sys
try:
 x = int(input('Choose task (Baseline:1, XRD ANN:2): '))
 if x == 1:
    print('You have chosen baseline.py \nPlease go to the csv file and select the XRD spectrum to analyze!')
    import baseline
 elif x == 2:
    print('You have chosen XRD.py \nPlease go to the csv file and select the XRD spectrum to analyze!')
    import XRD_ANN
 else:
    print('You have not selected anything, please go to main function to run it again')
except:
 print("Finish!")