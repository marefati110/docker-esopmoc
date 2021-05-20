
from collections import OrderedDict
import utils

import pyaml


def generate(services, networks=[], volumes=[], args=[]):

    # print(services)

    agg_services = OrderedDict()

    for service in services:
        service = utils.customOrder(service, utils.serviceOrder)
        agg_services[service['container_name'] + '_service'] = service

    config = OrderedDict({'version': args.version, 'services': agg_services})

    yml = pyaml.dump(config)

    if (args.output):
        file = open(args.output, 'w')
        file.write(yml)
    else:
        print(yml)
