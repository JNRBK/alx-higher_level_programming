-- creates a table second_table in the databases
-- hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256));
INSERT INTO second_table(id, name, score)
VALUES 
    (1, 'John', 10),
    (2, 'ALex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);