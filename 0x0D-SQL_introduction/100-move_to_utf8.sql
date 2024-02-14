-- converts hbtn_0c_0 database to 
-- utf8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0
SET utf8mb4
collate utf8mb4_unicode_ci;

ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
collate utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0
MODIFY name VARCHAR(256)
CHARACTER SET utf8mb4
collate utf8mb4_unicode_ci;