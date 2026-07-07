import math
import time

def calculate_stage_performance(isp, total_mass, dry_mass):
    """Isolates the Tsiolkovsky Rocket Equation to calculate Delta-V."""
    g0 = 9.80665
    return isp * g0 * math.log(total_mass / dry_mass)

def run_flight_simulation():
    print("=== INITIALIZING INTEGRATED ORBITAL DEPLOYMENT SIMULATION ===")
    
    # 1. Variables & Architecture setup
    payload_mass = 1200       # kg
    stage_1_prop = 38000      # kg
    stage_1_dry = 9000        # kg
    stage_1_isp = 285         # seconds
    
    # Calculate mass boundaries
    m_initial = stage_1_prop + stage_1_dry + payload_mass
    m_burnout = stage_1_dry + payload_mass
    
    # Calculate absolute target metric
    target_dv = calculate_stage_performance(stage_1_isp, m_initial, m_burnout)
    
    # 2. File I/O: Open a live telemetry file to log structural performance
    print("[LOG] Creating local file: flight_telemetry_report.csv...")
    with open("flight_telemetry_report.csv", "w") as log_file:
        log_file.write("Timestamp_s,CurrentMass_kg,VelocityDelta_ms,Status\n")
        
        current_propellant = stage_1_prop
        time_step = 0
        burn_rate = 3800 # kg of fuel burned per second over a 10-second window
        
        # 3. Simulation Loop (Combining loops, variables, and math updates)
        while current_propellant >= 0:
            current_mass = m_dry = (stage_1_dry + payload_mass) + current_propellant
            elapsed_dv = calculate_stage_performance(stage_1_isp, m_initial, current_mass)
            
            # 4. Conditional logic tracking structural thresholds
            if current_propellant > (stage_1_prop * 0.5):
                status_flag = "MAX_THRUST"
            elif current_propellant > 0:
                status_flag = "LOW_FUEL"
            else:
                status_flag = "MECO_BURNOUT" # Main Engine Cutoff
                
            # Write structured parameters to disk
            log_file.write(f"{time_step},{current_mass:.1f},{elapsed_dv:.1f},{status_flag}\n")
            print(f"[T+{time_step}s] Mass: {current_mass:<8.1f}kg | Delta-V: {elapsed_dv:<6.1f}m/s | Status: {status_flag}")
            
            current_propellant -= burn_rate
            time_step += 1

    # 5. Final Evaluation Boundary
    print("-" * 65)
    print(f"Simulation Complete. Total Delta-V Generated: {target_dv:.2f} m/s")
    if target_dv >= 2500:
        print("[STATUS] CRITICAL VERIFICATION: Functional logic perfectly encapsulated.")
    else:
        print("[STATUS] WARNING: Review mass equations before deployment.")
    print("-" * 65)

# Execute the master program
if __name__ == "__main__":
    run_flight_simulation()
