SELECT c.caseref, d.devil_text, d.devil_type, a.accusedref
FROM wdb_accused AS a
INNER JOIN wdb_case AS c ON a.accusedref = c.accusedref
INNER JOIN wdb_devilappearance AS d ON d.caseref = c.caseref
WHERE d.devil_text > ' ';
