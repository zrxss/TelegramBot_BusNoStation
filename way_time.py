from tosamara_api import list_of_arriving_buses_post

async def should_go_out():
    print('проверка')
    arrival = await list_of_arriving_buses_post()

    if not arrival:
        return False

    target_min_wait = 180
    target_max_wait = 300

    for bus in arrival:
        print(bus['timeInSeconds'])
        print(float(bus['timeInSeconds']) -210)
        print(bus['nextStopId'])
        walk_time = float(bus['timeInSeconds']) - 210
        if target_min_wait <= walk_time <= target_max_wait and bus['nextStopId'] != '1399':
            return True
    return False
