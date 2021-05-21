
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

    parser.add_argument('-b', '--beautiful', type=bool,
                        default=True,
                        help='ignore some data default is True')

    parser.add_argument('-n', '--network', type=str,
                        help='generate docker composer from contaners that \
                        join to the network. enter name or ID of Network ')

    args = parser.parse_args()

    return args


def main():

    args = init()
    print(args)
    yml = ''

    if args.container:

        services, networks = collect.collect(args.container)

        yml = generate.process(services=services, args=args, networks=networks)

    elif (args.network):

        containers = collect.find_container_by_network(args.network)

        services, networks = collect.collect(containers)

        yml = generate.process(services=services, args=args, networks=networks)

    else:
        print('-n or -c required')
        sys.exit(1)

    if (args.output):
        generate.write(yml, args.output)
    else:
        print(yml)


if __name__ == '__main__':
    main()
