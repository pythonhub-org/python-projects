# Python Program to Convert seconds into hours, minutes and seconds

import argparse
 
def convert(seconds):
    hour = seconds // 3600
    seconds %= 3600
    print(seconds)
    minutes = seconds // 60
    seconds %= 60
      
    return "%s:%0s:%02s" % (hour, minutes, seconds)
      
if __name__ == "__main__":  
    parser = argparse.ArgumentParser(description='Program to Convert seconds into hours, minutes and seconds')
    parser.add_argument('-s','--seconds', type=int, help="Input seconds", required=True)
    args = parser.parse_args() 
    print("Seconds: ", args.seconds)
    user_seconds = args.seconds
    print(convert(user_seconds))
