import datetime


def time_slice_to_datetime_duration(base_datetime, time_slice):
    # Mon 01:00-23:00 -> (datetime.datetime(2018, 7, 7, 1, 0), datetime.datetime(2018, 7, 7, 23, 0))

    weekday_to_int_map = {
        "Mon": 0,
        "Tue": 1,
        "Wed": 2,
        "Thu": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6
    }

    weekday, duration = time_slice.split(" ", 1)
    days = weekday_to_int_map[weekday]
    start_time, end_time = duration.split("-")
    start_time_hours, start_time_minutes = start_time.split(":")
    end_time_hours, end_time_minutes = end_time.split(":")
    start_datetime = base_datetime + datetime.timedelta(days=days, hours=int(start_time_hours), minutes=int(start_time_minutes))
    end_datetime = base_datetime + datetime.timedelta(days=days, hours=int(end_time_hours), minutes=int(end_time_minutes))
    return start_datetime, end_datetime


def diff_datetime_in_minutes(first_datetime, second_datetime):
    if not isinstance(first_datetime, datetime.datetime) or not isinstance(second_datetime, datetime.datetime):
        raise TypeError("Invalid argument(s), argument(s) should be datetime object")
    the_time_delta = first_datetime - second_datetime if first_datetime > second_datetime else second_datetime - first_datetime
    return the_time_delta.seconds / 60


def solution(s):
    # get today for base_datetime
    base_datetime = datetime.datetime.combine(datetime.date.today(), datetime.time.min)

    # parse the time slices information
    time_slices = s.split("\n")

    # time_slice -> (datetime, datetime)
    formatted_time_slices = list()
    for time_slice in time_slices:
        formatted_time_slices.append(time_slice_to_datetime_duration(base_datetime, time_slice))
    formatted_time_slices = sorted(formatted_time_slices, key=lambda x: x[0])

    # insert first moment and the last moment
    the_last_moment = datetime.datetime.combine((base_datetime + datetime.timedelta(7)).date(), datetime.time.min)
    formatted_time_slices.insert(0, (base_datetime, base_datetime))
    formatted_time_slices.append((the_last_moment, the_last_moment))

    # find the longest time slot in minutes
    longest_time_slot_in_minutes = 0
    for index in range(len(formatted_time_slices) - 1):
        current_time_slice = formatted_time_slices[index]
        next_time_slice = formatted_time_slices[index + 1]
        current_end_datetime = current_time_slice[1]
        next_start_datetime = next_time_slice[0]
        time_slot_in_minutes = diff_datetime_in_minutes(current_end_datetime, next_start_datetime)
        if time_slot_in_minutes > longest_time_slot_in_minutes:
            longest_time_slot_in_minutes = time_slot_in_minutes
    return longest_time_slot_in_minutes

if __name__ == "__main__":
    meetings = ["Sun 10:00-20:00", "Fri 05:00-10:00", "Fri 16:30-23:50", "Sat 10:00-24:00", "Sun 01:00-04:00",
                "Sat 02:00-06:00", "Tue 03:30-18:15", "Tue 19:00-20:00", "Wed 04:25-15:14", "Wed 15:14-22:40",
                "Thu 00:00-23:59", "Mon 05:00-13:00", "Mon 15:00-21:00"]
    input_str = "\n".join(meetings)
    result = solution(s=input_str)
    print(result)
