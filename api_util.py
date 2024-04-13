import datetime
import uuid

import config


def total_hours_sort(dictlist: list):
    total = 0
    for event in dictlist:
        total += event["hours"]
    return total

def sorted_future_events(dictlist: list):
    addendlist = {}
    for event in dictlist:
        date = datetime.datetime.strptime(event['datetime'], config.datetime_format)
        addendlist[date] = event
    sorted_events = dict(sorted(addendlist.items(), key=lambda item: item[0]))
    sorted_events = list(sorted_events.items())
    sorted_events.reverse()
    return [sorted_events[0], sorted_events[1], sorted_events[2]]


def most_recent_events(dictlist: list):
    addendlist = {}
    for event in dictlist:
        date = datetime.datetime.strptime(event['datetime'], config.datetime_format)
        addendlist[date] = event
    sorted_events = dict(sorted(addendlist.items(), key=lambda item: item[0]))
    sorted_events = list(sorted_events.items())
    return [sorted_events[0], sorted_events[1], sorted_events[2]]


def affiliation_leaderboard(dictlist: list):
    """

    :rtype: object
    """
    addendlist = {}
    for event in dictlist:
        affiliation = event["affiliation"]
        if affiliation is not None:
            addendlist[affiliation] = addendlist[affiliation] + event["hours"] if affiliation in addendlist else event["hours"]
    sorted_hours = dict(sorted(addendlist.items(), key=lambda item: item[1]))
    sorted_hours = list(sorted_hours.items())
    return [sorted_hours[0], sorted_hours[1], sorted_hours[2]]
