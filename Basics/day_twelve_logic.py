def check_system_readiness():
  systems = ["Propulsion", "Avionics", "Telemetry", "Payload"
  print("Running pre-flight check-list")

  for system in systems:
    print("Checking " + system + "Good to go")


  print("All systems GO for launch")
  return True

def run_launch_simulation(burn_time):
  altitude = 0
  velocity = 0
  current_time = 0

  altitude = altitude + velocity
  velocity = velocity + 50
  current_time = current_time + 1

  while current_time <= burn_time:
    print("T+" + str(current_time) + "s | Altitude: " + str(altitude) + "m | Velocity: " + str(velocity) + "m/s")

  print("Main engine cutoff. Burn Complete")

if __name__ = "__main__":
  ready = check_system_readiness
  if ready:
    run_launch_simulation(5)
