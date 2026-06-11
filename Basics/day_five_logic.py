#Just messing around with floats and ints and such

commander_name = "Glenn"
target_body = "Mars"

dry_mass = 5000.0
prop_mass = 25000.0

total_mass = prop_mass + dry_mass

prop_mass_fraction = (prop_mass / total_mass) * 100

print(f"LAUNCH COMMANDER: {commander_name}")
print(f"MISSION TARGET:   {target_body}")
print(f"TOTAL WET MASS:   {total_mass} kg")
print(f"PROP FRACTION:    {prop_mass_fraction}%")
