# db-hackathon

## Pre-reqs

Create venv with:
```commandline
./create_venv.sh
source .venv/bin/activate
```
or in PyCharm.

Then:
```commandline
pip install -r requirements.txt
./postgres.sh build
./postgres.sh configure
```

## Database Demo

```commandline
./postgres.sh shell
```

```sql
SELECT * FROM VesselStaticData;

SELECT * FROM TrackLog
JOIN VesselStaticData ON TrackLog.mmsi = VesselStaticData.mmsi;

UPDATE VesselStaticData
SET name = 'THIS OLD BOAT', callsign = 'FREEFALL'
WHERE mmsi = 367781000;
```

## UI Demo

```commandline
streamlit run ui.py 
```