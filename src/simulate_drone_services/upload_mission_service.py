'''
Since we don't have the physical drone to advertise its services (land, takeoff, etc)
this script simulates advertising those services. This lets the server actually call them.
Instead of seeing the perform its action, we will get a print message.
'''

import roslibpy

client = roslibpy.Ros(host='54.161.15.175', port=9090)

'''
Simulates advertising the service upload_mission from the drone.
'''
def handler(request, response):
    print("Upload mission service is being simulated")
    print(request["waypoint_task"])
    response["result"] = True
    response["cmd_set"] = 0
    response["cmd_id"] = 0
    response["ack_data"] = 0
    return True

service = roslibpy.Service(client, 'isaacs_server/fake_mission_waypoint_upload', 'isaacs_server/FakeMissionWaypointUpload')
service.advertise(handler)

print("Upload mission service advertised...")

client.run_forever()
client.terminate()