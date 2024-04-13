from fastapi import Depends
from fastapi.routing import APIRouter
import database
from users import manager
import datetime
import uuid
import api_util
from models import User


def create_new_UUID():
    return str(uuid.uuid4())


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


@api_router.get("/input")
async def input_create(location, hours, description, affiliation=None, user=Depends(manager)):
    database.store_event(user, location, hours, description, affiliation)

