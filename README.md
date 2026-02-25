# F1 Speed Track Visualization

A Python tool that visualizes an F1 driver's fastest lap telemetry data as a color-coded track map, where the color gradient represents speed throughout the lap.

## Overview

This script fetches real Formula 1 race data using the [FastF1](https://github.com/theOehrly/Fast-F1) library and plots a track map colored by speed using matplotlib. It's useful for analyzing how fast a driver is going through each section of a circuit during their fastest lap.

## Example Output

The visualization renders the full circuit layout with:
- A thick **black background** line representing the track
- A **plasma-colored overlay** where color = speed (purple = slow, yellow = fast)
- A **horizontal colorbar** at the bottom showing the speed scale in km/h

## Requirements

- Python 3.8+
- `fastf1`
- `matplotlib`
- `numpy`

Install dependencies with:

```bash
pip3 install fastf1 matplotlib numpy
```

## Usage

Run the script directly:

```bash
python3 f1_visualization.py
```

## Configuration

At the top of `f1_visualization.py`, edit the parameters section to customize the visualization:

```python
year   = 2025     # Season year
wknd   = 9        # Round number
ses    = 'R'      # Session type: 'R' = Race, 'Q' = Qualifying, 'FP1/FP2/FP3'
driver = 'HAM'    # Driver three-letter code
```

### 2025 Driver Codes

| Driver | Code | Team |
|---|---|---|
| Lando Norris | `NOR` | McLaren |
| Max Verstappen | `VER` | Red Bull Racing |
| Oscar Piastri | `PIA` | McLaren |
| George Russell | `RUS` | Mercedes |
| Charles Leclerc | `LEC` | Ferrari |
| Lewis Hamilton | `HAM` | Ferrari |
| Kimi Antonelli | `ANT` | Mercedes |
| Alexander Albon | `ALB` | Williams |
| Carlos Sainz | `SAI` | Williams |
| Fernando Alonso | `ALO` | Aston Martin |
| Nico Hulkenberg | `HUL` | Kick Sauber |
| Isack Hadjar | `HAD` | Racing Bulls |
| Oliver Bearman | `BEA` | Haas |
| Liam Lawson | `LAW` | Racing Bulls |
| Esteban Ocon | `OCO` | Haas |
| Lance Stroll | `STR` | Aston Martin |
| Yuki Tsunoda | `TSU` | Red Bull Racing |
| Pierre Gasly | `GAS` | Alpine |
| Gabriel Bortoleto | `BOR` | Kick Sauber |
| Franco Colapinto | `COL` | Alpine |
| Jack Doohan | `DOO` | Alpine |

> **Note:** Colapinto replaced Doohan at Alpine from Round 7 (Imola). Tsunoda replaced Lawson at Red Bull from Round 3, with Lawson moving to Racing Bulls.

## Caching

FastF1 automatically caches downloaded session data locally at:

```
~/Library/Caches/fastf1
```

This means subsequent runs for the same session will load much faster. To enable a custom cache directory, add this before `session.load()`:

```python
ff1.Cache.enable_cache('/path/to/your/cache')
```

## Project Structure

```
f1_speed_tracks/
├── f1_visualization.py   # Main script
└── README.md
```

## Professional Impact

This visualization technique is identical to what F1 engineers use in real-time during races. They analyze these patterns to optimize tire strategy, fuel consumption, and overtaking opportunities. Your analysis can reveal the same insights that drive million-dollar racing decisions.

## Data Source

All data is sourced from the official F1 timing API via the [FastF1](https://github.com/theOehrly/Fast-F1) library. Data availability depends on the session — historical data is available from the 2018 season onwards.
