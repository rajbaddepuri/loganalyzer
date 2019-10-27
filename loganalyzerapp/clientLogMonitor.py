"""
This module is intended to run on client machines to update and get
the latest updated log data to server side. Since log file will have
few data  to update everytime, this code needs to run manually on local
machine.
"""
import logging

import requests

URL = "http://127.0.0.1:8000/monitor/"


class LogMonitoring(object):
    def __init__(self):
        self.log = logging.getLogger("LogMonitor")
        # create console handler
        _ch = logging.StreamHandler()
        _ch.setLevel(logging.DEBUG)

        # formatter
        _formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        _ch.setFormatter(_formatter)

        # set handler
        self.log.setLevel(logging.DEBUG)
        self.log.addHandler(_ch)
        self.log.info("Logger initiated")

    def get_log_file_details(self):
        self.log.info("Getting log file details from server side")
        _data = requests.get(URL + 'get_data')
        _data = _data.json()
        _path = str(_data['PATH']).replace("_", "\\")
        _count = int(_data['COUNT'])

        with open(_path, 'r') as file:
            self.log.debug("Set file seek at {}".format(_count))
            for k, v in enumerate(file.readlines()):
                new_data = []
                if (k >= _count):
                    new_data.append(v)
                    print(new_data)
                    params = {"NEWDATA": new_data}
                    _status = requests.get(URL + 'update_new_data', params)
                    if _status.status_code == 200:
                        if _status.json()['STATUS'] == 0:
                            self.log.info("Successfully updated new data to server")
                        else:
                            self.log.critical("Unable to update the new data  to server, problem at server side")
                    else:
                        self.log.warning("Something went wrong")


LogMonitoring().get_log_file_details()
