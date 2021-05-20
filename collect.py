import docker

import utils


client = docker.from_env()


def collect_Container_data(c):

    data = {
        'image': '',
        'container_name': '',
        'command': '',
        'labels': {},
        'environment': []
    }

    attributes = c.attrs

    # set image
    utils.find_and_set(attributes, 'Config.Image', data, 'image')

    # set container name
    data['container_name'] = c.name

    # set container labels
    c_labels: dict = attributes['Config']['Labels']
    for key in c_labels.keys():
        if key not in utils.ignoreLables:
            data['labels'][key] = c_labels[key]

    # set container CMD
    if utils.find(attributes, 'Config.Cmd') != None:
        data['command'] = " ".join(
            attributes['Config']['Cmd'])

    # set environments
    c_env = utils.find(attributes, 'Config.Env')
    for env in c_env:
        for ignore in utils.ignoreEvn:
            if ignore not in env:
                data['environment'].append(env)

    return data


def collect(container_identifier):

    exist = False
    data = None

    containers = client.containers.list()

    for container in containers:

        found = container.name == container_identifier or container_identifier in container.id

        if found:
            exist = True
            c = client.containers.get(container.id)

            data = collect_Container_data(c)

    return exist, data
