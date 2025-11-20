# Spells example file

spells = [# (Spell, Damange, Energy)
    ("Fireball", 50, 40),
    ("Ice Spike", 40,30),
    ("Lightning Strike", 60,50),
    ("Wind Gust", 20, 10),
    ("Earthquake", 60, 60),
    ("Water Blast", 30, 20),
    ("Dark Matter", 70, 80)]

def dmg_per_energy(s):
    # handle zero energy to avoid ZeroDivisionError
    return s[1] / s[2] if s[2] != 0 else float('inf')

# Used lamba function to sort spells based on efficiency (damage per energy)
# Lambda function is an anonymous function defined with the lambda keyword
# Orginal sorting code commented out
efficient_spells = sorted(
        spells,
        # key = dmg_per_energy,
        key = lambda s: dmg_per_energy(s),
        reverse = True)

for s in efficient_spells:
    print(f'{s[0]}: {s[1]/s[2]:.2f}')
# thinking where to go from here