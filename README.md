# Simple Vehicle Dynamics Calculator

A small Python calculator for four basic vehicle dynamics calculations: speed conversion, lateral acceleration, braking distance and longitudinal load transfer.

Enter the vehicle mass, speed, corner radius, braking deceleration, CG height and wheelbase. The program prints the results in the terminal. No external libraries are required.

## Quick start

Requires **Python 3**. Open a terminal in the project directory and run:

```bash
python3 main.py
```

On Windows, use `py -3 main.py`. No packages or additional setup are required.

## Inputs

| Parameter | Unit | Accepted values |
| --- | --- | --- |
| Vehicle mass | kg | Greater than zero |
| Speed | km/h | Zero or greater |
| Corner radius | m | Greater than zero |
| Braking deceleration | m/s² | Positive magnitude |
| Center of gravity (CG) height | m | Greater than zero |
| Wheelbase | m | Greater than zero |

Use a dot for decimals, for example `0.3`. Invalid inputs, infinity, and NaN are rejected; the calculator asks for the value again.

## Calculations

### Speed conversion

`v = V / 3.6`

- `V`: speed in km/h
- `v`: speed in m/s

### Lateral acceleration

`a_y = v² / R`

- `a_y`: lateral acceleration in m/s²
- `v`: speed in m/s
- `R`: corner radius in m

This gives the acceleration needed to follow a corner at a constant speed and radius. To express it in g, the program divides the result by 9.81 m/s².

### Braking distance

`s = v² / (2a)`

- `s`: ideal distance to stop in m
- `v`: initial speed in m/s
- `a`: constant braking deceleration, entered as a positive magnitude in m/s²

This gives the stopping distance if deceleration stays constant. Driver reaction time is not included.

### Longitudinal load transfer

`ΔF = m a h / L`

- `ΔF`: vertical load transferred from the rear axle to the front axle in N
- `m`: vehicle mass in kg
- `a`: braking deceleration magnitude in m/s²
- `h`: center of gravity (CG) height in m
- `L`: wheelbase in m

During braking, the front axle gains this amount of vertical load and the rear axle loses the same amount. The equation assumes level ground.

Cornering and braking are calculated separately. The calculator does not model tire grip, aerodynamics or suspension behaviour.

## Example

Input:

```text
Vehicle mass [kg]: 300
Speed [km/h]: 60
Corner radius [m]: 25
Braking deceleration [m/s²]: 8
CG height [m]: 0.3
Wheelbase [m]: 1.6
```

Output:

```text
----------------------------------------
VEHICLE DYNAMICS RESULTS
----------------------------------------

Speed:
16.67 m/s

Lateral acceleration:
11.11 m/s²
1.13 g

Ideal braking distance:
17.36 m

Longitudinal load transfer:
450.00 N

----------------------------------------
```

## Project structure

```text
.
├── main.py       # Interactive calculator and input validation
├── README.md     # Usage, formulas, and model assumptions
└── .gitignore    # Local files excluded from version control
```
