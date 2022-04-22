import datetime
import os
import pytz
import random
import string


def get_local_time(dt, timezone):
    if dt.tzinfo != timezone:
        local_dt = dt.astimezone(timezone)
    else:
        local_dt = dt
    return local_dt


def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


def get_pytz_timezone(tz_str):
    tz = pytz.timezone(tz_str)
    return tz


def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


def convert_from_and_to_date_str_in_utc_datetime(
    user_timezone_str, from_date_str, to_date_str
):
    user_timezone = get_pytz_timezone(user_timezone_str)
    utc_timezone = pytz.timezone("UTC")

    # converting datetime to user's timezone and then in UTC
    from_date = datetime.datetime.strptime(from_date_str, "%d-%m-%Y")
    from_date = user_timezone.localize(from_date)
    from_date = from_date.replace(hour=0, minute=0, second=0)
    from_date = from_date.astimezone(tz=utc_timezone)

    # converting datetime to user's timezone and then in UTC
    to_date = datetime.datetime.strptime(to_date_str, "%d-%m-%Y")
    to_date = to_date + datetime.timedelta(days=1)
    to_date = user_timezone.localize(to_date)
    to_date = to_date.astimezone(tz=utc_timezone)

    return (from_date, to_date)
