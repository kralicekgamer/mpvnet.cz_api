# MPVNET.CZ API
API pro get dat z odjezdové tabule z mpvnet.cz

## Instalace
```bash
pip install mpvnet_cz_api
```

## Example
```py
from mpvnet_cz_api import Api

api = Api(53289)
print(api.sync())
```

## Stanice
Číslo stanice je nutné si vycucnout z webu vašeho dopravce případně inspektovat requesty na mpvnet.cz

Pro IDOL doporučuji https://dopravnimapy.kraj-lbc.cz/app/idol/zastavky.php
