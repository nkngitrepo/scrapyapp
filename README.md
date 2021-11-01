## Introduction

Repository for creating set of services for scrapping msc.com for getting container information.

#Services
	scrapy based application (app) for getting container/bol information and storing it in postgre db.
	prefect based scheduler to run the scrapy script every 5 mins and retry twice on failure.
	fastapi based service (fast) for getting the data stored in postgre db.

# Commands:
		docker-compose up -d

# Testing:
		Once the containers are up, check http://localhost:8080 for list of container/BOL being scrapped.
		http://localhost:8080/request/{contORBol}
		The fast service and the scrapy based scripts starts 30s after the containers are up.


* The list of container/BOL can be updated in the create_fixtures.sh script.
