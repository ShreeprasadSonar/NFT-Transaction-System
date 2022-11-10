USE nft_system;
DROP TABLE MANANGER;
CREATE TABLE MANAGER(M_id varchar(10),Email varchar(50),password varchar(10), Primary KEY (m_id));
INSERT INTO MANAGER (M_id ,Email ,password) VALUES ('22224','admin@gmail.com','admin@123');
INSERT INTO MANAGER (M_id ,Email ,password) VALUES ('22225','admin1@gmail.com','admin@123');
