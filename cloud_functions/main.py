from env import *
def flip_lights(message, context):
    print("INFO - Flip Lights Called: ", message)
    device_id = message["attributes"]["device_id"]

    device_path = client.device_path(
        project_id, cloud_region, registry_id, device_id)

    command = 'toggle'

    # Send command
    data = command.encode('utf-8')

    client.send_command_to_device(device_path, data)


