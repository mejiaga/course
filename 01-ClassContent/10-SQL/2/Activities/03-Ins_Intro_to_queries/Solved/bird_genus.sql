-- Select everything
SELECT * FROM birdsong;

-- One condition
SELECT * FROM birdsong WHERE genus = "Acanthis";

-- Two conditions with "and"
SELECT * FROM birdsong WHERE genus = "Acanthis" AND country = "Netherlands";

-- Either condition with "or"
SELECT * FROM birdsong WHERE genus = "Acanthis" OR genus = "Acrocephalus";

-- Where condition is not met
SELECT * FROM birdsong WHERE NOT genus = "Anthus";