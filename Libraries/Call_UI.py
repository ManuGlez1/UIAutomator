#!/usr/bin/python

"""

"""
from subprocess import check_output
from collections import namedtuple
import time
import datetime
import pytz
import re

# ---------------------------------------------------------
from uiautomator import Device


def read_serial():
    output = check_output(['adb', 'devices'])
    lines = output.splitlines()
    first_dev = lines[1].split()[0]
    print ("1st Device on List = {}".format(first_dev))
    return first_dev


def call(device):
    number = raw_input("Enter number to call ").strip()
    while not validate_number(number):
        number = raw_input("Enter a valid number ").strip()
    device.wakeup()
    device.press.home()
    wait()
    device(resourceId='com.sec.android.app.launcher:id/iconview_imageView'
           , className='android.widget.ImageView').click()
    wait()
    dial(device, number)
    print("Calling " + number)
    device(resourceId='com.samsung.android.dialer:id/dialButton'
           , className='android.widget.FrameLayout').click()
    wait(2)
    return


def dial(device, number):
    digits = device(resourceId='com.samsung.android.dialer:id/digits'
                    , className='android.widget.EditText')
    if digits.exists:
        digits.set_text("")
    for i in number:
        if i == '0':
            device(resourceId='com.samsung.android.dialer:id/zero'
                   , className='android.widget.RelativeLayout').click()
        elif i == '1':
            device(resourceId='com.samsung.android.dialer:id/one'
                   , className='android.widget.RelativeLayout').click()
        elif i == '2':
            device(resourceId='com.samsung.android.dialer:id/two'
                   , className='android.widget.RelativeLayout').click()
        elif i == '3':
            device(resourceId='com.samsung.android.dialer:id/three'
                   , className='android.widget.RelativeLayout').click()
        elif i == '4':
            device(resourceId='com.samsung.android.dialer:id/four'
                   , className='android.widget.RelativeLayout').click()
        elif i == '5':
            device(resourceId='com.samsung.android.dialer:id/five'
                   , className='android.widget.RelativeLayout').click()
        elif i == '6':
            device(resourceId='com.samsung.android.dialer:id/six'
                   , className='android.widget.RelativeLayout').click()
        elif i == '7':
            device(resourceId='com.samsung.android.dialer:id/seven'
                   , className='android.widget.RelativeLayout').click()
        elif i == '8':
            device(resourceId='com.samsung.android.dialer:id/eight'
                   , className='android.widget.RelativeLayout').click()
        elif i == '9':
            device(resourceId='com.samsung.android.dialer:id/nine'
                   , className='android.widget.RelativeLayout').click()
        elif i == '*':
            device(resourceId='com.samsung.android.dialer:id/star'
                   , className='android.widget.RelativeLayout').click()
        elif i == '#':
            device(resourceId='com.samsung.android.dialer:id/pound'
                   , className='android.widget.RelativeLayout').click()
        else:
            device(resourceId='com.samsung.android.dialer:id/zero'
                   , className='android.widget.RelativeLayout').long_click()
        wait(0.2)


def validate_number(number):
    return True if 15 > len(number) > 2 and re.match(r'^([\s\d\+\*\+\#]+)$', number) else False


def wait(sec=0.1):
    time.sleep(sec)


# ---------------------------------------------- -----------------------------

if __name__ == "__main__":
    serial = read_serial()
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
    print('serial: %s' % serial)

    try:
        d = Device(serial)
        print("** Script calling number with adb and uiautomator **")
        call(d)

    except Exception as ex:
        print(ex)
    finally:

        stop_ts = datetime.datetime.now()
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("--------------- RESULTS ---------------")
        print('test start:  %s ' % start_ts_pst)
        print('test end  :  %s' % stop_ts_pst)
