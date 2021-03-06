import roslibpy

client = roslibpy.Ros(host='136.25.185.6', port=9090)
client.run()

print(client.is_connected)

service = roslibpy.Service(client, 'isaacs_server/register_drone', 'isaacs_server/RegisterDrone')
request = roslibpy.ServiceRequest({'drone_name': "tester1", "drone_type":"MavrosDrone"})

print('Calling register_drone service...')
result = service.call(request)
print('Service response: {}'.format(result))
drone_id = result.data['drone_id']
topics_published = [{'name': 'test_name', 'type':
    'std_msgs/String'}]
topics_service = roslibpy.Service(client, 'isaacs_server/save_drone_topics', 'isaacs_server/SaveDroneTopics')
topics_request = roslibpy.ServiceRequest({'id': drone_id, 'publishes': [{'name': 'test_name', 'type':
    'std_msgs/String'}]})

print('Calling topics_service')
result = topics_service.call(topics_request)
print('Topics_service repsponse{}'.format(result))

'''shutdown_service = roslibpy.Service(client, 'isaacs_server/shutdown_drone', 'issacs_server/ShutdownDrone')
shutdown_request = roslibpy.ServiceRequest({'id': drone_id, 'publishes': topics_published})

print('shutdown')
print('shutdown response{}'.format(shutdown_service.call(shutdown_request)))'''

#land_service = roslibpy.Service(client, '/control_drone', 'isaacs_server/control_drone')
#land_request = roslibpy.ServiceRequest({"id": 0, "control_task":"land_drone"})

#print('Calling land_drone service...')
#result = land_service.call(land_request)
#print('Service response: {}'.format(result))

client.terminate()
