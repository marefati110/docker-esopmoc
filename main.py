
import docker
import argparse
import sys
import pyaml

import utils
import collect

from collections import OrderedDict


def init():

    parser = argparse.ArgumentParser(
        prog='docker-composer',
        usage='%(prog)s command [options] args',
        description='Generate docker-compose from running container.',
        epilog="give star on git hub :) https://github.com/marefati110/docker-composer ")

    parser.add_argument('-v', '--version', type=str, default='3',
                        help='Docker compose file version')

    parser.add_argument('-c', '--container', nargs='*', type=str,
                        help='The name or ID of the container')

    parser.add_argument('-n', '--network', type=str, default='default',
                        help='generate docker composer from contaners that join to the network. enter name or ID of Network ')

    args = parser.parse_args()

    return args


def main():

    args = init()

    for container in args.container:
        exist, config = collect.collect(container)

    if exist:
        config = {config['container_name'] + '_service': config}
        final_config = OrderedDict({'version': '"3"', 'services': config})

    file = open('./ali.yml', 'w')

    stream = pyaml.dump(final_config)

    stream = stream.replace('version: "3"\n', 'version: "3"\n\n')

    file.write(stream)


if __name__ == '__main__':

    main()
