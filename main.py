import levrt
from lev.austfish.host_scan import host_scan

async def main():
    domains = ['category-bgm.smzdm.com', 'dev-live-play.smzdm.com', 'union-bgm.smzdm.com', 'open-dcc.smzdm.com', 'union-api.smzdm.com', 'dev-open.smzdm.com', 'openapi.smzdm.com', 'ym.smzdm.com', 'comments.bgm.smzdm.com', 'qnz.smzdm.com', 'mp.m.smzdm.com', 'dev-h5.smzdm.com', 'article-bgm.smzdm.com', 'go.smzdm.com', 'live.smzdm.com', 'buy.bgm.smzdm.com', 'article-api.smzdm.com', 'jr-bgm.smzdm.com', 'youhui.bgm.smzdm.com', 'avatarimg.smzdm.com', 'tp-qna.smzdm.com', 'wx.bgm.smzdm.com', 'dingyue.bgm.smzdm.com', 'analytics-api-01.smzdm.com', 'pay.smzdm.com', 'eimg.smzdm.com', 'comment-api.smzdm.com', 'jinli-bgm.smzdm.com', 'common.m.smzdm.com', 'region-bgm.smzdm.com', 'dev-sso-bgm.smzdm.com', 'qncomment-img.smzdm.com', 'new-search-bgm.smzdm.com', 'post.bgm.smzdm.com', 'm.post.smzdm.com', 'ehr.smzdm.com', 'haojia-api.smzdm.com', 'newbrand.bgm.smzdm.com', 'dingyue-api.smzdm.com', 'qneimg.smzdm.com', 'a.smzdm.com', 'df-query-bgm.smzdm.com', 'tag.bgm.smzdm.com', 'dev01-union.smzdm.com', 'live-bgm.smzdm.com', 'jinli.m.smzdm.com', 'duihuan.m.smzdm.com', 'm.shaiwu.smzdm.com', 'ploy.bgm.smzdm.com', 'sqdsp-vod.smzdm.com', 'm.engine.smzdm.com', 'zdmfiles.smzdm.com', 'm.duihuan.smzdm.com', 'dev02-zhiyou.smzdm.com', 'm.news.smzdm.com', 'bi-bgm.smzdm.com', 'app-api.smzdm.com', 'cashier.smzdm.com', 'zhi.smzdm.com', 'fx.smzdm.com', 'm.faxian.smzdm.com', 'shence-bgm.smzdm.com', 'smtp.smzdm.com', 'abtest-bgm.smzdm.com', 'cc-bgm.smzdm.com', 'dev-zhiyou.m.smzdm.com', 'users.bgm.smzdm.com', 'users-bgm.smzdm.com', 'seo-content-bgm.smzdm.com', 'go.bgm.smzdm.com', 'reward.smzdm.com', 'shangjia-api.smzdm.com', 'brand-bgm.smzdm.com', 'fortress-bgm.smzdm.com', 'post-api.smzdm.com', 'test.bgm.smzdm.com', 'sso-bgm.smzdm.com', 'story.smzdm.com', 'shai.bgm.smzdm.com', 'l.smzdm.com', 'confluence-team.smzdm.com', 'imobile.smzdm.com', 'lipinka-bgm.smzdm.com', 'dnshostbak.smzdm.com', 'feed.smzdm.com', 'picture.bgm.smzdm.com', 'ship-bgm.smzdm.com', 'pop.smzdm.com', 'shaiwu.smzdm.com', 'bpm-bgm.smzdm.com', 'tag-api.smzdm.com', 'qianbao.smzdm.com', 'homepage-api.smzdm.com', 'article-cdn.smzdm.com', 'dev02-res.smzdm.com', 'garden.smzdm.com', 'qna.smzdm.com', 'reward-bgm.smzdm.com', 'live-service.smzdm.com', 'tuisong.smzdm.com', 'push-ios.smzdm.com', 'dev-zhiyou.smzdm.com', 'dev-shangjia.smzdm.com', 'tp-qneimg.smzdm.com', 'show.smzdm.com', 'qnym.smzdm.com', 'qnam.smzdm.com', 'zhanbao-bgm.smzdm.com', 'service-mail.smzdm.com', 'qny.smzdm.com', 'm.shai.smzdm.com', 'zximg.smzdm.com', 'searchapi.smzdm.com', 'new-product-bgm.smzdm.com', 'y.smzdm.com', 'jingyan.smzdm.com', 'nm-zximg.smzdm.com', 'm.lvyou.smzdm.com', 'bi-report-bgm.smzdm.com', 'common-api.smzdm.com', 'banner-bgm.smzdm.com', 'lm.smzdm.com', 'tools.smzdm.com', 'zapm-bgm.smzdm.com', 'baoliao.bgm.smzdm.com', 's-api.smzdm.com', 'live.m.smzdm.com', 'push-bgm.smzdm.com', 'res-card-beiwo.smzdm.com', 'i.smzdm.com', 'sso-ext-api.smzdm.com', 'dcc.smzdm.com', 'exchange.bgm.smzdm.com', 'jy.smzdm.com', 'sso2-bgm.smzdm.com', 'dev-pay.smzdm.com', 'list-bgm.smzdm.com', 'dev-cashier.smzdm.com', 'qnl.smzdm.com', 'logs-api.smzdm.com', 'openapi-bgm.smzdm.com', 'mt-vod.smzdm.com', 'res.smzdm.com', 'shai.m.smzdm.com', 'sqdsp-vod2.smzdm.com', 'test-zhiyou.smzdm.com', 'super-etl-canal-bgm.smzdm.com', 'analytics-api.smzdm.com', 'zhaiyao-bgm.smzdm.com', 'tp-qnam.smzdm.com', 'mail.smzdm.com', 'dev01-zhiyou.smzdm.com', 'cat-monitor.smzdm.com', 'hnair.card.smzdm.com', 'bgm.smzdm.com', 'm.haitao.smzdm.com', 'push.smzdm.com', 'res-ga.smzdm.com', 'olddcc.bgm.smzdm.com', 'bi-davinci-bgm.smzdm.com', 'commonservice-bgm.smzdm.com', 'crm-bgm.smzdm.com', 'dev01-open.smzdm.com', 'shangjia.bgm.smzdm.com', 'dev-cat-monitor.smzdm.com', 'jira-team.smzdm.com', 'mall-bgm.smzdm.com', 'auto-bgm.smzdm.com', 'baike-bgm.smzdm.com', 'logs-kibana-bgm.smzdm.com', 'imap.smzdm.com', 'test-pay.smzdm.com', 'huodong-bgm.smzdm.com', 'test.m.smzdm.com', 'res-beiwo.smzdm.com', 'ucc-bgm.smzdm.com', 'category.bgm.smzdm.com', 'ehr-bgm.smzdm.com', 'inet-health.smzdm.com', 'm.pinpai.smzdm.com', 'wikiapi.smzdm.com', 'plugin.smzdm.com', 'list-api.smzdm.com', 'm.haowu.smzdm.com', 'push-chrome.smzdm.com', 'df-bgm.smzdm.com', 'user-api.smzdm.com', 'push-1.smzdm.com', 'haojia-cdn.smzdm.com', 'shangjia-bgm.smzdm.com', 'engine.smzdm.com', 'dev01-h5.smzdm.com', 'jinli-api.smzdm.com', 'auth-bgm.smzdm.com', 'qnlm.smzdm.com', 'brand-api.smzdm.com', 'live-api.smzdm.com', 'mp.smzdm.com', 'td.smzdm.com', 'zhaiyao.m.smzdm.com', 'union-api-bgm.smzdm.com', 'dcc-bgm.smzdm.com', 'tp-qny.smzdm.com', 'edgerec-res.smzdm.com', 'homepage.bgm.smzdm.com', 'uactivity-bgm.smzdm.com', 'content-check-bgm.smzdm.com', 'm.jingyan.smzdm.com', 'am.smzdm.com', 'm.card.smzdm.com', 'dev-live.m.smzdm.com', 'tp-eimg.smzdm.com', 'ufile.smzdm.com', 'live-play.smzdm.com', 'm.wiki.smzdm.com', 'contributors.smzdm.com', 'wximg.smzdm.com', 'widget.bgm.smzdm.com', 'fusion-bgm.smzdm.com', 'biaodan.bgm.smzdm.com', 'new-lvyou-bgm.smzdm.com', 'recfeed-bgm.smzdm.com', 'uo-bgm.smzdm.com', 'dev02-union.smzdm.com', 'dev02-open.smzdm.com']
    data = await host_scan.hostScan(hosts = domains, ips =['106.75.10.185', '106.75.61.230', '106.75.107.38', '106.75.126.245', '101.206.162.61', '123.125.244.201', '36.25.254.122', '121.51.68.211', '36.25.254.84', '123.125.244.181'])

if __name__ == "__main__":
    import logging
    logging.basicConfig()
    logger = logging.getLogger("lev")
    logger.setLevel(logging.DEBUG)
    logger.debug("[lev app - hello world] debug test")
    levrt.run(main())