import roslibpy

client = roslibpy.Ros(host='136.25.185.6', port=9090)
client.run()

service = roslibpy.Service(client, '/set_ludicrous_speed', 'std_srvs/SetBool')
request = roslibpy.ServiceRequest({'data': True})

print('Calling service...')
result = service.call(request)
print('Service response: {}'.format(result))

client.terminate()
