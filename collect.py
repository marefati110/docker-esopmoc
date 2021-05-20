import docker
import utils


client = docker.from_env()


def collect_Container_data(c):

    data = {
        'image': '',
        'container_name': '',
        'restart': '',
        'command': '',
        'labels': {},
        'environment': [],
        'ports': []
    }

    attributes = c.attrs

    # set image
    utils.find_and_set(attributes, 'Config.Image', data, 'image')

    # set container name
    data['container_name'] = c.name

    # restart policy
    utils.find_and_set(
        attributes, 'HostConfig.RestartPolicy.Name', data, 'restart')
    if data['restart'] == 'no':
        data['restart'] = None

    # set container labels
    c_labels: dict = attributes['Config']['Labels']
    if c_labels:
        for key in c_labels.keys():
            if key not in utils.ignoreLables:
                data['labels'][key] = c_labels[key]

    # set container CMD
    if utils.find(attributes, 'Config.Cmd'):
        data['command'] = " ".join(
            attributes['Config']['Cmd'])

    # set environments
    c_env = utils.find(attributes, 'Config.Env')
    if c_env:
        for env in c_env:
            for ignore in utils.ignoreEvn:
                if ignore not in env:
                    key, value = env.split('=')
                    data['environment'].append({key: value})

    # set exposed port
    exposed_port = utils.find(attributes, 'HostConfig.PortBindings')
    if exposed_port:
        for port in exposed_port:
            container_port = port
            item = exposed_port[port]
            host_port = item[0]['HostIp'] + item[0]['HostPort']
            data['ports'].append(f'{host_port}:{container_port}')

    # filter truthy value
    filtered_data = data.copy()
    for key in data:
        if not data[key]:
            del filtered_data[key]

    return filtered_data


def collect(container_identifier):

    exist = False
    data = None

    containers = client.containers.list()

    for container in containers:

        found = container.name == container_identifier or \
            container_identifier in container.id

        if found:
            exist = True
            c = client.containers.get(container.id)

            data = collect_Container_data(c)

    return exist, data
