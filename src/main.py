from pymavlink import mavutil

master = mavutil.mavlink_connection('/dev/serial0', baud=921600)
master.wait_heartbeat()
print("Connected")