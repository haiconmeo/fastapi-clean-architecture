from datetime import datetime, timedelta


def get_date_range(start, end):
    date_format = "%Y-%m-%d"
    # start = datetime.strptime(start_date, date_format)
    # end = datetime.strptime(end_date, date_format)

    date_list = []
    current_date = start

    while current_date <= end:
        date_list.append(current_date.strftime(date_format))
        current_date += timedelta(days=1)

    return date_list
