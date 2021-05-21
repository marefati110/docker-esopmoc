
from collections import OrderedDict
import utils

import pyaml


def process(services, networks=[], volumes=[], args=[]):

    agg_services = OrderedDict()

    for service in services:
        service = utils.customOrder(service, utils.serviceOrder)
        agg_services[service['container_name'] + '_service'] = service

    config = OrderedDict(
        {'version': f"'{args.version}'",
         'services': agg_services,
         'networks': networks
         }
    )

    yml = pyaml.dump(config)

    return yml


def write(yml, output):
    file = open(output, 'w')
    file.write(yml)
