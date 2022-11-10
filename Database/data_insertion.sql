USE nft_system;
INSERT INTO MANAGER (M_id ,Email ,password) VALUES ('22224','admin@gmail.com','admin@123');
INSERT INTO MANAGER (M_id ,Email ,password) VALUES ('22225','admin1@gmail.com','admin@123');
INSERT INTO TRADER (t_id, t_name,t_lastname,pass,fiat_amt,Ph_no,cell_no,email,mem_type,eth_add,eth_cnt) VALUES('12346','Varun','Potluri','user@123','100.000','7372802224','7372802224','user@gmail.com','Gold','0x3db763bbbb1ac900eb2eb8b106218f85f9f64a13','5');
INSERT INTO CLASSIFICATION (mem_id , com_rate) VALUES('GOLD','5.25');
INSERT INTO CLASSIFICATION (mem_id , com_rate) VALUES('SILVER','7.25');
INSERT INTO ADDRESS (t_id,city,state,zipcode,st_add) VALUES('12346','Plano','TX','75075','120 Collier Dr');