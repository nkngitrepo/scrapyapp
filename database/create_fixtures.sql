CREATE TABLE IF NOT EXISTS container (
    cid char(50) primary key not null,
	type char(100),
	finalpod char(100),
	shippedto char(100),
	pcd       char(100),
	movement json
);

create table if not exists container_bol_requests (
	cid char(50) primary key not null
	);

CREATE TABLE IF NOT EXISTS bol (
    bid char(50) primary key not null,
	depdate char(100),
	vessel char(100),
	pol char(100),
	pod char(100),
	transhipment char(100),
	pcd       char(100),
	containers json
);

create table if not exists req_type (
	id char(50) PRIMARY key not null,
	type char(20) not NULL
);

insert into container_bol_requests(cid) values ('TGBU5600894'),('TRHU5131609'),('MEDUJ1656290'),('MEDUJ1656241'),('MEDUM5024051');