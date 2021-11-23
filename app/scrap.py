import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http.cookies import CookieJar
from scrapy.settings import default_settings
import logging
from scrapy.utils.project import get_project_settings
from datetime import timedelta, datetime
from twisted.internet import reactor
import config
import psycopg2
import json



logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.ERROR
)
logger = logging.getLogger("Default")


class BilloflandingSpider(scrapy.Spider):
    name = 'billoflandingclass'
    
    def start_requests(self):
        
        r = scrapy.Request(url = config.url,
                           meta={'cookiejar':1},
                           callback=self.final_res)
        yield r
    
    def final_res(self,response):
        t = config.formdata
        vs = response.css('input#__VIEWSTATE::attr(value)').get() #extract_first()
        ev = response.css('input#__EVENTVALIDATION::attr(value)').get() #extract_first()
        
        t['__VIEWSTATE']=vs
        t['__EVENTVALIDATION']=ev
        t['ctl00$ctl00$plcMain$plcMain$TrackSearch$txtBolSearch$TextField'] = self.bofl
        
        r = scrapy.FormRequest(url = config.url,method="POST",
                           formdata = t,
                           callback=self.parse)
        yield r
        

    def parse(self, response):
        error_txt = response.xpath(config.h3id).extract_first()
        if error_txt is not None and 'not found' in error_txt:
            logger.info ("H3 text ::"+str(error_txt))
            return
        
        bol = True
        #number of containers
        num_cont_str = response.xpath(config.bol_num_cont).extract_first()
        if num_cont_str is not None:
            print (num_cont_str)
            num_cont = int(num_cont_str[num_cont_str.index("(")+1:].split()[0])
            print ("Num containers :",num_cont)
        else:
            num_cont = 1
            bol = False
        
        s = []
        bhd = ["Departure_Date",'Vessel','pol','pod','transhipment','pcd']
        for th in response.xpath(config.bol_info):
            
            for tr in th.xpath('tr'):
                for td in tr.xpath('td'):
                    t = td.xpath('text()').get()
                    s.append(t.strip() if t else '')
                
        bcd = dict(zip(bhd,s))

        con = psycopg2.connect("dbname=admin user=admin password=admin host=db")
        cur = con.cursor()
                
        
        for i in range(1,num_cont+1):
            s = []
            hdr_xpath = config.bol_cont_hdr_ptrn%(i)
            for th in response.xpath(hdr_xpath):
                for tr in th.xpath('tr'):
                    for td in tr.xpath('td'):
                        t = td.xpath('text()').get() #extract_first()
                        s.append(t.strip() if t else '')

            hd = ['type','finalpod','shippedto','pcd'] if len(s) == 4 else ['type','finalpod','finalpodeta','shippedto','pcd','etablank']
                    
            cd = dict(zip(hd,s))

            s = []
            cm = []
            rh = ["location",'description','date','vessel','voyage']
            mv_xpath = config.bol_cont_mov_ptrn%(i)
            for tr in response.xpath(mv_xpath):
                for td in tr.xpath('td'):
                    t = td.xpath('text()').get() #extract_first()
                    s.append(t.strip())
                cm.append(dict(zip(rh,s)))            
            logger.info (','.join(s))
            cmd = {}
            for index,r in enumerate(cm):
                cmd[index]=r

            if not bol:
                ins_query = """insert into container (cid, type, finalpod, finalpodeta, shippedto, pcd, movement) values (%s,%s,%s,%s,%s,%s,%s) on conflict (cid) do update set
                            type = %s, finalpod = %s, finalpodeta = %s, shippedto = %s, pcd = %s, movement = %s;"""
                try:
                    cur.execute(ins_query,(self.bofl,cd['type'],cd['finalpod'],cd.get('finalpodeta',''),cd['shippedto'],cd['pcd'],json.dumps(cmd),cd['type'],cd['finalpod'],cd.get('finalpodeta',''),cd['shippedto'],cd['pcd'],json.dumps(cmd)))
                    #con.commit()
                    cur.execute("insert into req_type (id, type) values (%s,%s) on conflict(id) do nothing",(self.bofl,"CONT"))
                    con.commit()
                except Exception as e:
                    print ("Failed to persist container details to db",file=sys.stderr)
                    print (str(e),file=sys.stderr)
                    break
                
            else:
                cont_name = response.xpath(config.bol_con_name_ptrn%(i)).extract_first().split(':')[-1].strip()
                td = {}
                for k,v in cd.items():
                    td[k]=v
                td['movement'] = cmd
                bcd[cont_name]=td
                
        if bol:
            ins_query = """insert into bol (bid, depdate, vessel, pol, pod, transhipment, pcd, containers) values (%s,%s,%s,%s,%s,%s,%s,%s) on conflict (bid) do update set
                        depdate = %s, vessel = %s, pol = %s, pod = %s, transhipment = %s, pcd = %s, containers = %s;"""
            try:
                cur.execute(ins_query,(self.bofl,bcd['Departure_Date'],bcd['Vessel'],bcd['pol'],bcd['pod'],bcd['transhipment'],bcd['pcd'],json.dumps(bcd),bcd['Departure_Date'],bcd['Vessel'],bcd['pol'],bcd['pod'],bcd['transhipment'],bcd['pcd'],json.dumps(bcd)))
                #con.commit()
                cur.execute("insert into req_type (id, type) values (%s,%s) on conflict(id) do nothing;",(self.bofl,"BOL"))
                con.commit()
            except Exception as e:
                print ("Failed to persist bol details to db",file=sys.stderr)
                print (str(e),file=sys.stderr)

        con.close()
        logger.info ("done")

if __name__ == '__main__':
    print ("In main process")

    
    #get list of containers to crawl
    con = psycopg2.connect("dbname=admin user=admin password=admin host=db")
    cur = con.cursor()
    cur.execute("select * from container_bol_requests;")
    l = cur.fetchall()
    con.close()
    process = CrawlerProcess()
    for c in l:
        process.crawl(BilloflandingSpider,bofl=c)
    process.start()
    
