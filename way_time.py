from tosamara_api import list_of_arriving_buses_post

from config import EXCLUDED_NEXT_STOP_IDS

async def should_go_out():
    arrival = await list_of_arriving_buses_post()

    if not arrival:
        return False

    target_min_wait = 180
    target_max_wait = 300

    for bus in arrival:
        wait_time = float(bus['timeInSeconds']) - 210
        if target_min_wait <= wait_time <= target_max_wait and bus['nextStopId'] not in EXCLUDED_NEXT_STOP_IDS:
            return True
    return False
