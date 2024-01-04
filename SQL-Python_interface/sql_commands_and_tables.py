
table_name = "movies"
column_name = "collection_in_mil"
new_data_type = "DECIMAL(4,1)"
condition = "> 300"
order_Desc = "DESC"
select_From = "table_name"
reference_id_from_x = "table_name"
x_data_base = "table_name"
id_from_x = "table_name"
primary_key = "PRIMARY KEY"
Auto_increment = "AUTO_INCREMENT  KEY"
data_base_content = ""
content_table_to_insert = "data_base_content"
content_values = "(Forrest Gump, 1994, Drama, 330.2)"


show_table_query = f"""DESCRIBE {table_name}""" # Showing a Table Schema

alter_table_query = f"""
ALTER TABLE {table_name}
MODIFY COLUMN {column_name} {new_data_type}
"""

drop_table_query = f"""DROP TABLE {table_name}"""

select_results = f"SELECT {table_name} FROM {table_name} LIMIT 5"

filter_results = f"""
SELECT title, collection_in_mil
FROM {table_name}
WHERE {column_name} {condition}
ORDER BY {column_name} {order_Desc}
"""

create_table = f"""
CREATE TABLE {table_name} (
{data_base_content}
)

"""
foreign_key = f"""
FOREIGN KEY({reference_id_from_x}) REFERENCES {x_data_base}({id_from_x})
"""

insert_table_query = f"""
INSERT INTO {table_name} ({content_table_to_insert})
VALUES
{content_values}
"""
