from levrt import ctx, annot, Concurrent
from . import host_scan
from lev.maimai.oneforall import oneforall

@annot.meta(
    desc = "获取域名数据 host",
    params = [
        annot.Param("domain", "目标域名", holder = "baidu.com"),
        annot.Param("ipNum", "高频ip数据", holder = 10)
    ]
)
async def getDomainHost(domain: str, ipNum: int):
    """
    my first asset
    ```
    await getDomainHost('baidu.com', 10)
    ```
    """

    import logging
    logging.basicConfig()
    logger = logging.getLogger("lev")
    logger.setLevel(logging.DEBUG)
    logger.debug("[lev app - getDomainHost] log from asset - start point")

    
    doc = await oneforall.raw(domain)
    data = await doc.get()
    domins = data['data']
    logger.debug(f"[lev app - oneforall] handle")
    hosts = []
    ips = []
    ipcount = {}
    for domain in domins: #Iterate through the loop to read line by line
        # 取错误域名
        if domain['status'] != '200':
            hosts.append(domain['subdomain'])
        if domain['cdn'] != 1 :
            mip =  domain['ip']
            for ip in mip.split(','):
                ipcount[ip] = ipcount.get(ip, 0) + 1
    ipcount = sorted(ipcount.items(), key=lambda x:x[1], reverse=True)
    if len(ipcount) < ipNum:
        ipNum = len(ipcount)
    for i in range(ipNum):
        ips.append(ipcount[i][0])
    hosts = list(set(hosts))
    print(hosts)
    print(ips)
    
    logger.debug("[lev app - getDomainHost] log from asset - end point")
    
