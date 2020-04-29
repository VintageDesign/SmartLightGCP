
import sys
import os
import time
import json
import base64
import sqlalchemy
from google.cloud import pubsub_v1
from google.cloud import iot_v1
from decouple import config

project_id = 'kronos-272918'
subscription_name = 'light-sub'
registry_id = 'iotcore-registry'
cloud_region = 'us-central1'

subscriber = pubsub_v1.subscriberclient()
client = iot_v1.devicemanagerclient()

subscription_path = subscriber.subscription_path(project_id, subscription_name)
