USE nft_system;
UPDATE NFT SET t_id = '12346' WHERE NFT_id = 7870524649;
INSERT INTO NFT_TRANSACTION (t_id ,NFT_id,name,t_date_time,com_rate,status,buyer_eth_add ,seller_eth_add,mem_type ,comm_type,nft_add ,t_value,nft_trans_id ,URL) VALUES('12346','7870524649','zenledger','2022-11-20 18:55:20','7.25','success','0x3db763bbbb1ac900eb2eb8b106218f85f9f64a13','E7B674F3C31E28DA6BE6BA56AEC47D6D425C008C1C','SILVER','ETH','301980cc06603301980cc0660330241925943fffd9','7.2','1234567892','https://drive.google.com/file/d/1FzrupPBSOREATAGmhZXtMQF5oZ2jcotE/view?usp=sharing');
