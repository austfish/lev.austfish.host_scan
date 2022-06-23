from levrt import ctx, annot, Concurrent
from . import host_scan
from lev.maimai.oneforall import oneforall

@annot.meta(
    desc = "获取域名数据",
    params = [annot.Param("domain", "目标域名", holder = "baidu.com")]
)
async def getDomain(domain: str):
    """
    my first asset
    ```
    await hello_world(9)
    ```
    """

    import logging
    logging.basicConfig()
    logger = logging.getLogger("lev")
    logger.setLevel(logging.DEBUG)
    logger.debug("[lev app - getDomain] log from asset - start point")

    
    doc = await oneforall.raw(domain)
    data = await doc.get()
    logger.debug(f"[lev app - oneforall] {data}")

    logger.debug("[lev app - getDomain] log from asset - end point")
