import os, arcpy


# Set workspace environment to geodatabase
arcpy.env.workspace = r"C:\Users\jamatney\Desktop\Domains\domains.gdb"
arcpy.overwriteOutput = True

out_dir = r"C:\Users\jamatney\Desktop\Domains"

tables = arcpy.ListTables()

for table in tables:
    print 'Exporting %s Table to Excel File in %s' % (table, out_dir)
    out_xls = os.path.join(out_dir, table + ".xlsx")
    print out_xls
    arcpy.TableToExcel_conversion(table, out_xls)
