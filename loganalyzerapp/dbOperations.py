from django.db import connection
from .logger import Logger


log=Logger.get_logger()

""" def create_tables_if_not_exists():
    with connection.cursor() as cursor:
        cursor.execute("create table if not exist \"loganalayzerfilename\""
                       "('filename' varchar(20) nut null") """


def insert_log_path(log_path):
    try:
        with connection.cursor() as cursor:
            log.debug("inserting file path into loganalyzerapp_log")
            sql = "insert into loganalyzerapp_log(`file`) values('" + str(log_path) + "');"
            cursor.execute(sql)
            log.debug("inserted file path into loganalayzerapp_log")
        return True
    except Exception as e:
        log.warning(e.message())
        return False

def get_log_path():
    """
    This method is used to get already stored file path.
    If no data found, then it will return None object reference
    :return: file path as string or None if not found
    """
    file_path = None
    try:
        with connection.cursor() as cursor:
            log.debug("selecting file from loganalyzerapp_log")
            sql = "select file from loganalyzerapp_log;"
            cursor.execute(sql)
            log.debug("executed select script")
            file_path = cursor.fetchone()[0]   #result : ex: ('D:/access.log'). We need value only.... result[0]
            log.debug("resulated file path is "+str(file_path))
    except Exception as e:
        log.warning(e.message())
    return file_path


def clean_log_analyzer():
    try:
        with connection.cursor() as cursor:
            sql = "delete from loganalyzerapp_log_fields;"
            sql1 = "delete from loganalyzerapp_log;"
            cursor.execute(sql)
            log.debug("the data in the loganalayzerapp_log_fileds are deleted")
            cursor.execute(sql1)
            log.debug("the data in the loganalayzerapp_log are deleted")
        return True
    except Exception as e:
        log.warning(e.message())
        return False


def insert_log_values(dict_value):
    try:
        with connection.cursor() as cursor:
            sql = "insert into loganalyzerapp_log_fields (`lp_adrees`,`date_time`,`res_code`,`memory`,`url_loction`,`method`) " \
                  "values('" + str(dict_value["ip_adress"]) + "','" + str(dict_value["date_time"]) + "'," + str(
                dict_value["res_code"]) + "" \
                                          "," + str(dict_value["memory"]) + ",'" + str(
                dict_value["url_loction"]) + "','" + str(dict_value["method"]) + "');"
            cursor.execute(sql)
            # cursor.commit(True)
            return True
    except Exception as e:
        log.warning(e.message())
        return False
