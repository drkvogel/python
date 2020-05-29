

# does a string with continuation include the leading spaces when indented?

get_jobs_sql = 'SELECT\
j.type AS type, j.report_type AS reporttype, us.name AS username, us.email, \
co.updated_at AS checkoutupdated, iv.updated_at AS inventoryupdated, \
tp.postcode, tp.line_1, tp.line_2, tp.city,\
n.name AS nodename, n.level AS nodelevel\
FROM jobs j\
INNER JOIN checkouts co ON co.id = j.report_id\
INNER JOIN inventories iv ON iv.id = j.report_id\
INNER JOIN users us ON us.id = j.clerk_id\
INNER JOIN tenant_properties tp ON tp.id = j.tenant_property_id\
LEFT JOIN customer_organisation_nodes n ON n.id = j.customer_id'

print(get_jobs_sql)
# yes

# indented:
# SELECT    j.type AS type

# not indented
# SELECTj.type AS type

# so beware!
