import demos.demo_lib
demos.demo_lib.func()

from demos import demo_lib
demo_lib.func()

import demos.demo_lib as dl
dl.func()


from datetime import datetime
datetime()



network = get_network()

if network:
    import local_cache as service
else:
    import ws_util as service

service.save(data)










