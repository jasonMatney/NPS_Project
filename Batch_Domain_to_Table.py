import os, arcpy
# Set workspace environment to geodatabase
arcpy.env.workspace = r"C:\Users\jamatney\AppData\Roaming\Esri\Desktop10.2\ArcCatalog\rtca user connected to rtca_new database.sde"

arcpy.overwriteOutput = True

gdb = r"C:\Users\jamatney\AppData\Roaming\ESRI\Desktop10.4\ArcCatalog\Connection to CASCADES.cnr.ncsu.edu.sde"
gdb_domains = r"C:\Users\jamatney\Desktop\Domains\domains.gdb"

desc = arcpy.Describe(gdb)
domains = desc.domains

for domain in domains:
    print 'Exporting %s CV to table in %s' % (domain, gdb)
    out_table = os.path.join(gdb_domains, domain)
    arcpy.DomainToTable_management(gdb, domain, out_table, 'field','description', '#')
