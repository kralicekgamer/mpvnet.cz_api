# MPVNET.CZ API
API pro get dat z odjezdové tabule z mpvnet.cz

## Instalace
```bash
pip install mpvnet_cz_api
```

## Example
```py
from mpvnet_cz_api import Api

api = Api(53289, "idol")
print(api.sync())
```
- První číslo je číslo zastávky.
- Druhé pole je dopravce (pid, idol, odis, zlin, jikord)

```py
from mpvnet_cz_api import Stop

print(Stop.get_num("Janův Důl", "idol"))
```
- Kód pro get jsonu, který obsahuje číslo zastávek.

## Verze
| Verze | Stav | Poznámka |
| --- | --- | --- |
| **1.0.X** | ✅ | Bez custom dopravce. Bez dependencies. |
| **1.1** | ⭐ ||
