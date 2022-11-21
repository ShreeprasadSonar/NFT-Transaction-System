USE nft_system;
/*DROP TABLE FIAT_TRANSACTIONS;*/
DROP TABLE NFT_TRANSACTION;
CREATE TABLE NFT_TRANSACTION (t_id varchar(10),NFT_id varchar(10),name varchar(50),t_date_time DATETIME,com_rate DOUBLE(5,3),status varchar(10),buyer_eth_add varchar(50),seller_eth_add varchar(50),mem_type varchar(10),nft_add varchar(50),t_value DOUBLE(10,3),nft_trans_id varchar(10),URL VARCHAR(2083),com_type varchar(10), Primary KEY (nft_trans_id), FOREIGN KEY (t_id) REFERENCES TRADER(t_id),FOREIGN KEY (NFT_id) REFERENCES NFT(NFT_id));
/*INSERT INTO NFT_TRANSACTION (t_id ,NFT_id,name,t_date_time,com_rate,status,buyer_eth_add ,seller_eth_add,mem_type ,comm_type,nft_add ,t_value,nft_trans_id ,URL) VALUES('12346','7870524649','zenledger','2022-11-20 19:30:20','7.25','success','0x3db763bbbb1ac900eb2eb8b106218f85f9f64a13','E7B674F3C31E28DA6BE6BA56AEC47D6D425C008C1C','SILVER','ETH','301980cc06603301980cc0660330241925943fffd9','7.2','1234567892','https://drive.google.com/file/d/1FzrupPBSOREATAGmhZXtMQF5oZ2jcotE/view?usp=sharing');
UPDATE NFT SET t_id = '12346' WHERE NFT_id = 7870524649;
INSERT INTO NFT_TRANSACTION (t_id ,NFT_id,name,t_date_time,com_rate,status,buyer_eth_add ,seller_eth_add,mem_type ,comm_type,nft_add ,t_value,nft_trans_id ,URL) VALUES('12346','7870524649','zenledger','2022-11-20 18:55:20','7.25','success','0x3db763bbbb1ac900eb2eb8b106218f85f9f64a13','E7B674F3C31E28DA6BE6BA56AEC47D6D425C008C1C','SILVER','ETH','301980cc06603301980cc0660330241925943fffd9','7.2','1234567892','https://drive.google.com/file/d/1FzrupPBSOREATAGmhZXtMQF5oZ2jcotE/view?usp=sharing');

CREATE TABLE FIAT_TRANSACTIONS (t_id varchar(10),ft_id varchar(10),t_date_time DATETIME,amount DOUBLE(10,3),status varchar(10),type varchar(10), Primary KEY (ft_id), FOREIGN KEY (t_id) REFERENCES TRADER(t_id));
INSERT INTO FIAT_TRANSACTIONS (t_id,ft_id,t_date_time,amount,status,type ) VALUES('12346','9705396277','2022-11-20 20:31:20','100','success','USD');
INSERT INTO FIAT_TRANSACTIONS (t_id,ft_id,t_date_time,amount,status,type ) VALUES('12346','9705396299','2022-11-20 20:31:20','100','success','USD');
*/