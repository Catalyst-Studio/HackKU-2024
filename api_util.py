import datetime
import uuid

import config


def total_hours_sort(dictlist: list):
    """
        This function takes a list of dictionaries as input and returns the total hours worked by all the events in the list.

        Parameters:
            dictlist (list): A list of dictionaries, where each dictionary represents an event. The dictionary must contain a "hours" key with the number of hours worked.

        Returns:
            float: The total number of hours worked by all the events in the input list.

        """
    total = 0
    for event in dictlist:
        total += int(event["hours"])
    return total

def sorted_future_events(dictlist: list):
    """
        Sorts a list of events by date and returns the three most recent events.

        Parameters:
            dictlist (list): A list of dictionaries, where each dictionary represents an event. The dictionary must contain a "datetime" key with the event date and time in the format specified by the config.datetime_format variable. Other keys may also be included, such as "hours" for the number of hours worked, "affiliation" for the employee's department or company, etc.

        Returns:
            list: A list of three dictionaries, where each dictionary represents an event, in chronological order from the most recent to the least recent.

        """
    addendlist = {}
    for event in dictlist:
        date = datetime.datetime.strptime(event['datetime'], config.datetime_format)
        addendlist[date] = event
    sorted_events = dict(sorted(addendlist.items(), key=lambda item: item[0]))
    sorted_events = list(sorted_events.items())
    sorted_events.reverse()
    return [sorted_events[0], sorted_events[1], sorted_events[2]]


def most_recent_events(dictlist: list):
    """
        This function sorts a list of events by date and returns the three most recent events.

        Parameters:
            dictlist (list): A list of dictionaries, where each dictionary represents an event. The dictionary must contain a "datetime" key with the event date and time in the format specified by the config.datetime_format variable. Other keys may also be included, such as "hours" for the number of hours worked, "affiliation" for the employee's department or company, etc.

        Returns:
            list: A list of three dictionaries, where each dictionary represents an event, in chronological order from the most recent to the least recent.

        """
    addendlist = {}
    for event in dictlist:
        date = datetime.datetime.strptime(event['datetime'], config.datetime_format)
        addendlist[date] = event
    sorted_events = dict(sorted(addendlist.items(), key=lambda item: item[0]))
    sorted_events = list(sorted_events.items())
    return [sorted_events[0], sorted_events[1], sorted_events[2]]


def affiliation_leaderboard(dictlist: list):
    """
    This function takes a list of dictionaries as input and returns a list of tuples, where each tuple represents an affiliation and its total hours worked.

    Parameters:
        dictlist (list): A list of dictionaries, where each dictionary represents an event. The dictionary must contain a "hours" key with the number of hours worked.

    Returns:
        list: A list of tuples, where each tuple represents an affiliation and its total hours worked. The list is sorted in descending order, with the top three affiliations being the first three elements of the list.

    """
    addendlist = {}
    for event in dictlist:
        affiliation = event["affiliation"]
        if affiliation is not None:
            addendlist[affiliation] = addendlist[affiliation] + event["hours"] if affiliation in addendlist else event["hours"]
    sorted_hours = dict(sorted(addendlist.items(), key=lambda item: item[1]))
    sorted_hours = list(sorted_hours.items())
    return [sorted_hours[0], sorted_hours[1], sorted_hours[2]]
