#!/usr/bin/python

"""

"""
from subprocess import check_output
import time
import datetime
import pytz
import re


# ---------------------------------------------------------

def read_serial():
    output = check_output(['adb', 'devices'])
    lines = output.splitlines()
    first_dev = lines[1].split()[0]
    print ("1st Device on List = {}".format(first_dev))
    return first_dev


def call_adb(s):
    number = raw_input("Enter number to call ")
    while not validate_number(number):
        number = raw_input("Enter a valid number ")
    check_output(['adb', '-s', s, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])
    print("Calling "+number)
    check_output(['adb', '-s', s, 'shell', 'am', 'start', '-a', 'android.intent.action.CALL', '-d', 'tel:' + number])
    time.sleep(5)
    return


def validate_number(number):
    return True if 15 > len(number) > 2 and re.match(r'^([\s\d\+\*\+\#]+)$', number) else False


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    serial = read_serial()
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
    print('serial: %s' % serial)

    try:
        print("** Script calling number with adb **")
        call_adb(serial)

    except Exception as ex:
        print(ex)
    finally:

        stop_ts = datetime.datetime.now()
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("--------------- RESULTS ---------------")
        print('test start:  %s ' % start_ts_pst)
        print('test end  :  %s' % stop_ts_pst)
