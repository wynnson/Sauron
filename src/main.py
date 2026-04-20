from pymavlink import mavutil

master = mavutil.mavlink_connection('/dev/serial0', baud=921600)
master.wait_heartbeat()
print("Connected")

msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
print(msg)

lat = msg.lat / 1e7
lon = msg.lon / 1e7
alt_m = msg.alt / 1000.0          # altitude above mean sea level
rel_alt_m = msg.relative_alt / 1000.0

print("lat:", lat)
print("lon:", lon)
print("alt_m:", alt_m)
print("relative_alt_m:", rel_alt_m)
