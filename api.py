from fastapi import Depends
from fastapi.routing import APIRouter
import database
from users import manager
import api_util
from models import User


api_router = APIRouter(prefix="/api")


@api_router.get("/dashboard")
async def dashboard_getAll(user=Depends(manager)):
    """
    This function returns the dashboard for the given user.

    Args:
        user (User): the user for which to retrieve the dashboard

    Returns:
        dict: a dictionary containing the total hours, recent events, soon events, and affiliate leaderboard for the given user
    """
    event_store = []
    events = database.get_events(user)
    for event in events:
        event = dict(event)
        event.pop("_id")
        event_store.append(event)
    total_hours = api_util.total_hours_sort(event_store)
    recent_events = api_util.most_recent_events(event_store)
    affiliate_leaderboard = api_util.affiliation_leaderboard(event_store)
    return {
        "total_hours": total_hours,
        "recent_events": recent_events,
        "affiliate_leaderboard": affiliate_leaderboard
    }


# create an event
@api_router.post("/submit-event")
async def input_create(location, hours: int, description, date: str, time: str, affiliation=None, user=Depends(manager)):
    """
    This function creates a new event for the given user.

    Args:
        location (str): the location of the event
        hours (int): the number of hours worked at the event
        description (str): a description of the event
        date (str): the date of the event in the format "MM/DD/YYYY"
        time (str): the time of the event in the format "HH:MM AM/PM"
        affiliation (str, optional): the affiliation of the user at the event (e.g., "work", "school", etc.). Defaults to None.
        user (User): the user for which to create the event

    Returns:
        dict: a dictionary containing a "success" field indicating whether the event was created successfully, and an "error" field containing an error message if the event could not be created
    """
    try:
        database.store_event(user, location, hours, description, date, time, affiliation)
        return {
            "success": True,
            "redirect_url": "/view-events"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@api_router.get("/get-all-events")
async def get_all_events(user=Depends(manager)):
    """
        This function returns all events for the given user.

        Args:
            user (User): the user for which to retrieve the events

        Returns:
            list: a list of dictionaries containing the event information for the given user
        """
    events = database.get_events(user)
    event_store = []
    for event in events:
        event = dict(event)
        event.pop("_id")
        event_store.append(event)
    return event_store


@api_router.get("/get-all-locations")
async def get_all_locations(user=Depends(manager)):
    """
    This function returns all locations in the system.

    Args:
        user (User): the user for which to retrieve the locations

    Returns:
        list: a list of dictionaries containing the location information
    """
    locations = database.get_locations(user)
    location_store = []
    for location in locations:
        location = dict(location)
        location.pop("_id")
        location_store.append(location)
    return location_store


@api_router.get("/add-location")
async def add_loc(user: User, name: str, address: str, city: str, state: str, zipcode: int):
    """
        This function adds a new location to the system.

        Args:
            name (str): the name of the location
            address (str): the address of the location
            city (str): the city of the location
            state (str): the state of the location
            zipcode (int): the zipcode of the location
            user (User): the user for which to add the location

        Returns:
            list: a list of dictionaries containing the locations in the system
        """
    database.store_location(user, name, address, city, state, zipcode)
    locations = database.get_locations(user)
    location_store = []
    # remove IDs from each
    for location in locations:
        location = dict(location)
        location.pop("_id")
        location_store.append(location)
    return location_store
