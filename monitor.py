# -*- coding: utf-8 -*-

import sensors

#COLORS
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"


def getTemp():
    sensors.init()
    avg = 0
    try:
        for chip in sensors.iter_detected_chips():
            print HEADER + '%s at %s' % (chip, chip.adapter_name) + ENDC
            for feature in chip:
                _system = feature.label
                _system_temp = feature.get_value()
                print BLUE + '\tSystem: %s ' % (_system) + ENDC
                print WARNING + '\tTemp: %.2f°C ' % (_system_temp) + ENDC
                if _system_temp > 60:
                    print FAIL + '\tSystem Overheating' + ENDC
                else:
                    print GREEN + BOLD + '\tSystem OK' + ENDC
                print '\n'
    finally:
        sensors.cleanup()


if __name__ == "__main__":
    getTemp()






