import requests

# pip install requests

auth = ('guest', 'guest')
url = 'http://localhost:15672/api/'
vhost = '%2F'
queue_name = 'final_queue'
url_queue = f'http://localhost:15672/api/queues/{vhost}/{queue_name}'


def get_queues():
    response = requests.get(f'{url}queues', auth=auth)
    queues = response.json()
    for queue in queues:
        print(queue['name'])


def get_queue_info():
    response = requests.get(url_queue, auth=auth)
    queue_info = response.json()
    print(queue_info)
    print(f"Number of messages in the queue '{queue_name}' {queue_info.get('messages', 0)}")
    # Number of messages in the queue 'final_queue' 3


get_queues()
# EducationQ
# HealthQ
# SportsQ
# ae_queue
# final_queue
# headers_queue
# main-queue
# task_queue
# test
get_queue_info()
# {'consumer_details': [], 'arguments': {}, 'auto_delete': False, 'consumer_capacity': 0, 'consumer_utilisation': 0,
#  'consumers': 0, 'deliveries': [], 'durable': True, 'effective_policy_definition': {}, 'exclusive': False,
#  'exclusive_consumer_tag': None,
#  'garbage_collection': {'fullsweep_after': 65535, 'max_heap_size': 0, 'min_bin_vheap_size': 46422, 'min_heap_size': 233,
#                         'minor_gcs': 2}, 'head_message_timestamp': None, 'idle_since': '2024-04-23T14:51:54.534+02:00',
#  'incoming': [], 'memory': 15216, 'message_bytes': 81, 'message_bytes_paged_out': 0, 'message_bytes_persistent': 0,
#  'message_bytes_ram': 81, 'message_bytes_ready': 81, 'message_bytes_unacknowledged': 0,
#  'message_stats': {'ack': 0, 'ack_details': {'rate': 0.0}, 'deliver': 0, 'deliver_details': {'rate': 0.0},
#                    'deliver_get': 6, 'deliver_get_details': {'rate': 0.0}, 'deliver_no_ack': 4,
#                    'deliver_no_ack_details': {'rate': 0.0}, 'get': 2, 'get_details': {'rate': 0.0}, 'get_empty': 0,
#                    'get_empty_details': {'rate': 0.0}, 'get_no_ack': 0, 'get_no_ack_details': {'rate': 0.0},
#                    'publish': 7, 'publish_details': {'rate': 0.0}, 'redeliver': 0, 'redeliver_details': {'rate': 0.0}},
#  'messages': 3, 'messages_details': {'rate': 0.0}, 'messages_paged_out': 0, 'messages_persistent': 0, 'messages_ram': 3,
#  'messages_ready': 3, 'messages_ready_details': {'rate': 0.0}, 'messages_ready_ram': 3, 'messages_unacknowledged': 0,
#  'messages_unacknowledged_details': {'rate': 0.0}, 'messages_unacknowledged_ram': 0, 'name': 'final_queue',
#  'node': 'rabbit@0853-OFFICE-103', 'operator_policy': None, 'policy': None, 'recoverable_slaves': None,
#  'reductions': 38228, 'reductions_details': {'rate': 0.0}, 'single_active_consumer_tag': None, 'state': 'running',
#  'storage_version': 1, 'type': 'classic', 'vhost': '/'}
