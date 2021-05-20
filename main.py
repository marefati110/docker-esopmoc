
import argparse
import generate
import collect
import sys


def init():

    parser = argparse.ArgumentParser(
        prog='docker-composer',
        usage='%(prog)s command [options] args',
        description='Generate docker-compose from running container.',
        epilog="give star on git hub :)")

    parser.add_argument('-v', '--version', type=str, default='3',
                        help='Docker compose file version')

    parser.add_argument('-c', '--container', nargs='*', type=str,
                        help='The name or ID of the container')

    parser.add_argument('-o', '--output', type=str,
                        help='output path ')

    parser.add_argument('-n', '--network', type=str,
                        help='generate docker composer from contaners that \
                        join to the network. enter name or ID of Network ')

    args = parser.parse_args()

    return args


def main():

    args = init()

    services = []
    # networks = []
    # volumes = []

    for container in args.container:
        exist, service = collect.collect(container)

        if exist:
            services.append(service)

    if not service:
        print('container notfound')
        sys.exit(1)

    generate.generate(services=services, args=args)


if __name__ == '__main__':
    main()
