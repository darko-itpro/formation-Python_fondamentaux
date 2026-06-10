import pyflix.datasource as ds

number_episodes = 6
EPISODE_DURATION = 23

def extract_time_from_str(str_time):
    hours, minutes = str_time.split("h")
    return int(hours), int(minutes)

hours, minutes = extract_time_from_str(ds.get_start_time())

start_time = hours * 60 + minutes

view_duration = number_episodes * EPISODE_DURATION

end_time = start_time + view_duration

print("J'irai au lit à {}h{:02}".format(end_time // 60, end_time % 60))

print("J'irai au lit à {}h{:02}".format(*divmod(end_time, 60)))