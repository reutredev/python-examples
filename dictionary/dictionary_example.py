import yaml

output_data = {
    'resources': [{
        'type': 'compute.v1.instance',
        'name': 'vm-created-by-deployment-manager',
        'properties': {
            'disks': [{
                'deviceName': '$disks_deviceName$',
                'boot': '$disks_boot$',
                'initializeParams': {
                    'sourceImage': '$disks_initializeParams_sourceImage$'
                },
                'autoDelete': '$disks_autoDelete$',
                'type': '$disks_type$'
            }],
            'machineType': '$machineType$',
            'zone': '$zone$',
            'networkInterfaces': [{
                'network': '$networkInterfaces_network$'
            }]
        }
    }]
}

# ff = open('meta.yaml', 'w+')
# output = yaml.dump(output_data, stream=None, allow_unicode=True, default_flow_style=False)
# print(output)


def dict_to_yaml_str(data, indent=0):
    """
    Converts a dictionary to a string in YAML file format.

    Args:
        data (dict): The dictionary to be converted to YAML string.
        indent (int, optional): The number of spaces to use for indentation. Defaults to 0.

    Returns:
        str: The YAML string representation of the dictionary.
    """
    lines = []
    for key, value in data.items():
        if isinstance(value, dict):
            # Recursively convert nested dictionaries
            lines.append(f"{' ' * indent}{key}:")
            lines.append(dict_to_yaml_str(value, indent + 2))
        else:
            # Convert primitive values to YAML format
            lines.append(f"{' ' * indent}{key}: {value}")
    return '\n'.join(lines)

result = dict_to_yaml_str(output_data, indent=2)
print(result)