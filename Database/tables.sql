CREATE DATABASE NFT_System;
USE nft_system;
CREATE TABLE TRADER (t_id varchar(10), t_name varchar(50),pass varchar(50),fiat_amt DOUBLE(10,3),Ph_no int(10),cell_no int(10),email varchar(50),mem_type varchar(10),eth_add varchar(50),eth_cnt int(10),Primary key (t_id));
CREATE TABLE CLASSIFICATION (mem_id varchar(10), com_rate DOUBLE(5,3), Primary Key (mem_id));
CREATE TABLE ADDRESS (t_id varchar(10),city varchar(10),state VARCHAR(10),zipcode int(6),st_add varchar(20), FOREIGN KEY (t_id) REFERENCES TRADER(t_id));
CREATE TABLE FIAT_TRANSACTIONS (t_id varchar(10),ft_id varchar(10),t_date_time DATETIME,amount DOUBLE(10,3),status varchar(10),type varchar(10), Primary KEY (ft_id), FOREIGN KEY (t_id) REFERENCES TRADER(t_id));
CREATE TABLE NFT (t_id varchar(10),NFT_id varchar(10),NFT_add VARCHAR(50),NFT_value DOUBLE(10,3),name varchar(50),sell_add varchar(50), Primary KEY (NFT_id), FOREIGN KEY (t_id) REFERENCES TRADER(t_id));
CREATE TABLE NFT_TRANSACTION (t_id varchar(10),NFT_id varchar(10),t_date_time DATETIME,com_rate DOUBLE(5,3),status varchar(10),buyer_eth_add varchar(50),seller_eth_add varchar(50),mem_type varchar(10),nft_add varchar(50),t_value DOUBLE(10,3),nft_trans_id varchar(10), Primary KEY (nft_trans_id), FOREIGN KEY (t_id) REFERENCES TRADER(t_id),FOREIGN KEY (NFT_id) REFERENCES NFT(NFT_id));
CREATE TABLE MANANGER (M_id varchar(10),NAME varchar(10),password varchar(10), Primary KEY (m_id));