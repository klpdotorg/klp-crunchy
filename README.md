klp-crunchy
===========

klp-crunchy cleans up specific KML files. Picks up the School code from the HTML markup, dumps it back as an XML tag. Nothing much really.

Pipeline
_________
1. Run crunchy, python crunchy.py *.kml
2. Run kml2pgsql, python kml2pgsql *.<cleaned_kml_files>
3. Perform psql -d <dbname> -f operations.sql
