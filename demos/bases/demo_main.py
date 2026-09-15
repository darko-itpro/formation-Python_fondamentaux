natwork = get_network()

if network:
    import ws_utils as service
else:
    import local_cache as service


service.save(data)

