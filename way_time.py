from tosamara_api import list_of_arriving_buses_post

from config import EXCLUDED_NEXT_STOP_IDS, MIN_WAIT_SECONDS, MAX_WAIT_SECONDS, WALKING_TIME_SECONDS


async def should_go_out():
    arrival = await list_of_arriving_buses_post()

    if not arrival:
        return False

    target_min_wait = MIN_WAIT_SECONDS
    target_max_wait = MAX_WAIT_SECONDS

    for bus in arrival:
        walking_time = WALKING_TIME_SECONDS
        wait_time = float(bus['timeInSeconds']) - walking_time
        if target_min_wait <= wait_time <= target_max_wait and bus['nextStopId'] not in EXCLUDED_NEXT_STOP_IDS:
            return True
    return False
