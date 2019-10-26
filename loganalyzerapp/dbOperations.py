from django.db import connection
from .logger import Logger

log = Logger.get_logger()

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
        log.warning(e)
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
            file_path = cursor.fetchone()[0]  # result : ex: ('D:/access.log'). We need value only.... result[0]
            log.debug("resulated file path is " + str(file_path))
    except Exception as e:
        log.warning(e)
    return file_path


def get_count_db():
    count = 0
    try:
        with connection.cursor() as cursor:
            log.debug("selecting file from loganalyzerapp_log")
            sql = "select count(*) from loganalyzerapp_log_fields;"
            cursor.execute(sql)
            print(sql)
            log.debug("executed select script")
            count = cursor.fetchone()[0]  # result : ex: ('D:/access.log'). We need value only.... result[0]
            log.debug("resulated count is " + str(count))
    except Exception as e:
        log.warning(e)
    return count


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
        log.warning(e)
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
        log.warning(e)
        return False


def process_file_data(lines, seek=0):
    if lines is None:
        return False
    for i in lines:
        value = str(i).split(" ")
        dict_value = dict()
        dict_value["ip_adress"] = value[0][2:len(value[0])]
        dict_value["date_time"] = value[3][1:len(value[3])]
        dict_value["method"] = value[5][1:len(value[5])]
        dict_value["url_loction"] = value[6]
        dict_value["res_code"] = value[8]
        dict_value["memory"] = value[9]
        if not insert_log_values(dict_value):
            log.info("Values not inserted successfully : {}".format(" ".join(value)))
            return False
    return True


def get_ip_adress():
    ip_addrs = None
    try:
        with connection.cursor() as cursor:
            sql = "select distinct lp_adrees from loganalyzerapp_log_fields;"
            cursor.execute(sql)
            records = cursor.fetchall()
            ip_addrs = []
            if records:
                ip_addrs = list(map(lambda x: x[0], records))
    except Exception as e:
        log.warning(e)
    return ip_addrs


def get_all_values(ip_address_req):
    record = None
    try:
        with connection.cursor() as cursor:
            sql = "select date_time,res_code,memory,url_loction,method from loganalyzerapp_log_fields where lp_adrees = '%s';" % ip_address_req
            cursor.execute(sql)
            record = cursor.fetchall()
    except Exception as e:
        log.warning(e)
    return record
