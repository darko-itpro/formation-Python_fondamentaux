
import pyflix.utils.templating as tp
import pyflix.datasource as ds
import exos_correction.media_utils as mu

EPISODE_DURATION = 23
episodes = 7

total_duration = EPISODE_DURATION * episodes

print(tp.TIME_REMAINING.format(*divmod(total_duration, 60)))

start_time = mu.to_minutes(*ds.get_start_time().split("h"))

end_time = start_time + total_duration
print(tp.END_HOUR.format(*divmod(end_time, 60)))


