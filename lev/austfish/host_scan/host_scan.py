"""
我的第一个潮汐平台工具
利用HOSTS碰撞突破边界
Homepage: austfish
GitHub: -
Type: IMAGE-BASED
Version: v1.0.0
"""
import levrt
from levrt import Cr, ctx, remote, annot
from levrt.annot.cats import Attck, BlackArch

@annot.meta(
    desc="hostScan",
    params=[
        annot.Param("hosts", "400 404 相关域名",holder=['baidu.com']),
        annot.Param("ips", "高频率 IP",holder=['127.0.0.1']),
    ],
    cats=[Attck.Reconnaissance],
)
def hostScan(hosts: list = ["world.cn"], ips: list = ["127.0.0.1"]) -> Cr:
    """
    Host Scan的唯一工具模式
    ```
    await hostScan(["world.cn"], ["127.0.0.1"])
    ```
    """
    @levrt.remote
    def entry():
        import logging
        logging.basicConfig()
        logger = logging.getLogger("lev")
        logger.setLevel(logging.DEBUG)
        import sys
        sys.path.append('/usr/local/lib/python3.10/site-packages')
        import requests
        logger.debug("[lev app - hello world] log from container")
        logger.info('run')
        #读取host地址
        results = []
        for ip in ips:
            http_s = ['http','https']
            for h in http_s :
                for host in hosts:
                    headers = {'Host':host,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
                    try:
                        r = requests.session()
                        requests.packages.urllib3.disable_warnings()
                        rhost = r.get(h + '://' + ip,verify=False,headers=headers,timeout=5)
                        rhost.encoding='utf-8'
                        title = re.search('<title>(.*)</title>', rhost.text).group(1) #获取标题
                        info = (ip,host,h,len(rhost.text),title)
                        results.append(info)
                        logger.info(info)
                    except Exception :
                        error = ip + " --- " + host + " --- 访问失败！~"
                        logger.debug(error)
        ctx.set(msg=f"Get count, {len(results)}!")
        

    return Cr("4c2376401edc", entry=entry())


__lev__ = annot.meta([hostScan],
                     desc = "host scan", # name of tool
                     cats = {
                        Attck: [Attck.Reconnaissance] # ATT&CK
                     })
