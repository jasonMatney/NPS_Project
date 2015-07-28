/* backup the database to a .bak and then create a new database from a .bak restore. */
BACKUP DATABASE [Map] TO DISK = 'C:\Users\jamatney\Map.bak'

/*Then check the logical names and locations for the current files in the .bak:*/
RESTORE FILELISTONLY FROM DISK ='C:\Users\jamatney\Map.bak'

/*And finally restore the database, renaming the files to make sure you don't overwrite your existing database*/
RESTORE DATABASE Map_new    
FROM disk = 'C:\Users\jamatney\Map.bak'
WITH replace,
MOVE 'Map' TO 'C:\Users\jamatney\Map_new.MDF',
MOVE 'Map_log' TO 'C:\Users\jamatney\Map_new.LDF',
recovery --force
