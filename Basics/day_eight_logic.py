def evaluate_launch_parameters(chamber_pressure, target_pressure):
  deviation = (chamber_pressure - target_pressure) / target pressure

  if deviation > 0.15:
    print("Overpressure detected in combustion chamber")
  elif deviation < -0.2:
    print("Underpressure detected in combustion chamber")
  elif deviation < -0.05 or deviation > 0.05:
    print("Telemetry flucuating outside nominal bounds")
  else:
    print("System stable")

target_psi = 3000.0
current_telemetry = 3500.0

flight_status = evaluate launch parameters(current_telemetry, target_psi)
print("Current Flight Status is", flight_status)
