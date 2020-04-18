#!/usr/bin/python

"""

"""
from subprocess import check_output
import time
import datetime
from uiautomator import Device
import pytz


# ---------------------------------------------------------

def read_serial():
    output = check_output(['adb', 'devices'])
    lines = output.splitlines()
    first_dev = lines[1].split()[0]
    print ("1st Device on List = {}".format(first_dev))
    return first_dev


def turn_wifi_on(device):
    device.wakeup()
    device.press.home()
    device.open.quick_settings()
    wait()
    device(resourceId='com.android.systemui:id/settings_button', className='android.widget.ImageButton').click()
    wait()
    device(text='Connections').click()
    wait()
    wifi_opt = device(resourceId='android:id/switch_widget', className='android.widget.Switch')
    if wifi_opt.__getattr__('text') == 'On':
        print 'Wifi is already turned on'
    else:
        wifi_opt.click()
    device.press.home()
    return


def wait(sec=0.1):
    time.sleep(sec)


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    serial = read_serial()
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
    print('serial: %s' % serial)

    try:
        d = Device(serial)

        print("** Script Turn On Wifi **")
        turn_wifi_on(d)

    except Exception as ex:
        print(ex)
    finally:

        stop_ts = datetime.datetime.now()
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("--------------- RESULTS ---------------")
        print('test start:  %s ' % start_ts_pst)
        print('test end  :  %s' % stop_ts_pst)
