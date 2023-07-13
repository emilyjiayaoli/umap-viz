CREATE TABLE IF NOT EXISTS TrackLog (
    logtime integer,
    mmsi integer,
    latitude float,
    longitude float,
    PRIMARY KEY (logtime, mmsi)
);

CREATE TABLE VesselStaticData (
    mmsi integer PRIMARY KEY,
    name text,
    callsign text
);

INSERT INTO TrackLog (logtime, mmsi, latitude, longitude)
VALUES
    (1670055179, 311000274, 31.74212, -75.55503),
    (1670065059, 538007278, 31.50451, -75.88419),
    (1670069482, 636020354, 31.94118, -74.99293),
    (1670416874, 636019990, 33.59915, -73.76806),
    (1670472175, 338179794, 31.7121, -74.96736),
    (1670564716, 215354000, 33.35099, -74.13815),
    (1670820972, 367781000, 32.76343, -74.2345);

INSERT INTO VesselStaticData (mmsi, name, callsign)
VALUES
    (311000274, 'LARRY B WHIPPLE', 'WDK7401'),
    (538007278, 'TWISTED ANGEL', 'WDL5339'),
    (636020354, 'SAN PATRICIO', 'WCX6675'),
    (636019990, 'BEVERLY M I', 'CFP2004'),
    (338179794, 'ADANAC III', 'VCLT'),
    (215354000, 'MASHOMACK', 'WDA9320'),
    (367781000, 'FROLIC', 'WDL3075');