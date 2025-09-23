import demos.demo_lib
print(demos.demo_lib.multiply(5))

from demos import demo_lib
print(demo_lib.multiply(8))

import demos.demo_lib as dl
print(dl.multiply(7))

from demos.demo_lib import multiply
print(multiply(2))



# Exemple import "dynamique"
# network = get_network()
#
# if network:
#     import ws_helper as service
# else:
#     import local_cache as service
#
# service.save(data)

