import pyflix.datasource as ds

if __name__ == "__main__":
    print('-----')
    print('Premier execice')

    distance = 19.7
    duration = 6.892

    print("Ma vitesse est de {:.2f} m/s".format(distance / duration))
    print(f"Ma vitesse est de {distance / duration:.2f} m/s")

    print('-----')
    print('Second exercices')

    n_episodes = 7
    EPISODE_DURATION = 23
    
    total_duration = n_episodes * EPISODE_DURATION
    
    start_hours, start_minutes = ds.get_start_time().split('h')
    start_hours = int(start_hours)
    start_minutes = int(start_minutes)
    
    start_time = start_hours * 60 + start_minutes
    end_time = start_time + total_duration
    
    print("dodo à {}h{:02}".format(end_time // 60, end_time % 60))
    print("dodo à {}h{:02}".format(*divmod(end_time, 60)))
