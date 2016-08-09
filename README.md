## OpeningHours (python)

This module is a parser between the excellent [OpenStreetMap Opening Hour format](https://wiki.openstreetmap.org/wiki/Key:opening_hours) and python datetime objects.


### Installation

```
pip install opening_hours
```

### Usage

```
from opening_hours import OpeningHours
from datetime import datetime
import pytz


oh = OpeningHours("2016 Mar: Mo-Sa 08:00-13:00,14:00-17:00")
oh.is_open(datetime.now(pytz.timezone('Europe/Paris')))

```
