# -*- coding: utf-8 -*-

import sys, os

files = sys.argv[1:]
operations = open('operations.sql', 'a')

for file in files:
    table_name = file.split("_")[4].split(".")[0]
    command = 'ogr2ogr -f \"PostgreSQL\" PG:\"host=localhost user= password= dbname=\" '+file+' -nln '+'"'+table_name+'"\n'
    print command
    alter = 'ALTER TABLE '+'"'+table_name+'" '+'RENAME COLUMN description TO code;\n'
    cluster_table = '"'+'cluster_'+table_name[:-1]+'"'
    create = 'CREATE TABLE '+cluster_table+' (code BIGINT NOT NULL PRIMARY KEY,name varchar(150), centroid geometry);\n'
    insert = 'INSERT INTO '+cluster_table+' SELECT CAST(code AS BIGINT), name, ST_CENTROID(ST_COLLECT(wkb_geometry))  from '+'"'+table_name+'" '+'GROUP BY code, name;\n'
    drop = 'DROP TABLE '+'"'+table_name+'";\n'
    os.popen(command)
    operations.write(alter)
    operations.write(create)
    operations.write(insert)
    operations.write(drop)
