-- Remove left-most quote:
UPDATE MyTable
SET FieldName = SUBSTRING(FieldName, 2, LEN(FieldName))
WHERE LEFT(FieldName, 1) = '"'

-- Remove right-most quote:
UPDATE MyTable
SET FieldName = SUBSTRING(FieldName, 1, LEN(FieldName)-1)
WHERE RIGHT(FieldName, 1) = '"'
