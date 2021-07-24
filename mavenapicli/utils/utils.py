import datetime


def from_time_in_millis_to_extended_date(timestamp_in_millis):
    '''
    Starting from a date in millis returns it in the following format ->  datetime.datetime(YYYY, mm, dd, HH, MM, SS)
    '''
    extended_date = datetime.datetime.fromtimestamp(timestamp_in_millis/1000.0)
    return extended_date


def from_time_in_millis_to_ymd_date(timestamp_in_millis):
    '''
    Starting from a date in millis returns it in the following format ->  YYYY-mm-dd
    '''
    extended_date = from_time_in_millis_to_extended_date(timestamp_in_millis)
    ymd_date = extended_date.strftime('%Y-%m-%d')
    return ymd_date
