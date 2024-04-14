from fastapi import Depends
from fastapi.routing import APIRouter
import database
from users import manager
import datetime
import uuid
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
    soon_events = api_util.sorted_future_events(event_store)
    affiliate_leaderboard = api_util.affiliation_leaderboard(event_store)
    return {
        "total_hours": total_hours,
        "recent_events": recent_events,
        "soon_events": soon_events,
        "affiliate_leaderboard": affiliate_leaderboard
    }


# create an event
@api_router.post("/submit-event")
async def input_create(location, hours, description, date: str, time: str, affiliation=None, user=Depends(manager)):
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
async def get_all_locations():
    locations = database.get_locations()
    location_store = []
    for location in locations:
        location = dict(location)
        location.pop("_id")
        location_store.append(location)
    return location_store


@api_router.get("/add-location")
async def add_loc(name: str, address: str, city: str, state: str, zipcode: int):
    database.store_location(name, address, city, state, zipcode)
    locations = database.get_locations()
    location_store = []
    # remove IDs from each
    for location in locations:
        location = dict(location)
        location.pop("_id")
        location_store.append(location)
    return location_store
