-- Run after importing to confirm the data loaded correctly.
-- Expected (approx): active_listings ~228,410 | sold_comps ~439,167
SELECT
  (SELECT COUNT(*) FROM rets_property)  AS active_listings,
  (SELECT COUNT(*) FROM california_sold) AS sold_comps,
  (SELECT COUNT(*) FROM rets_openhouse) AS open_houses;
