import Configs
seed_row = {
	"mode_data": {
		"hrefs": {
			"field_name": "hrefs",
			"rule_type": "re",
			"field_type": "dynamic_url",
			"source_type": "url",
			"field_rule": "",
			"replace": [".*", "[res.group(0)+'&page=%s' % i for i in range(10)]"]
		}
	},
	"result_type": "dynamic_url",
	"url_list": ["http://weixin.sogou.com/weixin?query=ç«ç¾&type=2&ie=utf8page=0", "http://weixin.sogou.com/weixin?query=ç«ç¾&type=2&ie=utf8page=1", "http://weixin.sogou.com/weixin?query=ç«ç¾&type=2&ie=utf8page=2", "http://weixin.sogou.com/weixin?query=ç«ç¾&type=2&ie=utf8page=3", "http://weixin.sogou.com/weixin?query=ç«ç¾&type=2&ie=utf8page=4", "http://weixin.sogou.com/weixin?query=ç«ç¾&type=2&ie=utf8page=5", "http://weixin.sogou.com/weixin?query=ç«ç¾&type=2&ie=utf8page=6", "http://weixin.sogou.com/weixin?query=ç«ç¾&type=2&ie=utf8page=7", "http://weixin.sogou.com/weixin?query=ç«ç¾&type=2&ie=utf8page=8", "http://weixin.sogou.com/weixin?query=ç«ç¾&type=2&ie=utf8page=9"],
	"son_modes": [{
		"mode_data": {
			"hrefs-level2": {
				"field_name": "hrefs-level2",
				"rule_type": "xpath",
				"field_type": "dynamic_url",
				"source_type": "html",
				"field_rule": "//h3//a/@href",
				"replace": ["", ""]
			}
		},
		"result_type": "dynamic_url",
		"url_list": ["http://mp.weixin.qq.com/s?src=11&timestamp=1519356986&ver=715&signature=ufgf2CMobTj9bJje01pWXHM4NdtyoUm2wyjpEyhm838fDoXlH2M37clqzED9LOUL5gBuzOToH*NYZdXzoM3ZzquoL6x7XZZ5R--Yiro-yRSRGKff*PSXMFWtpGF1haVo&new=1", "http://mp.weixin.qq.com/s?src=11&timestamp=1519356986&ver=715&signature=uNu2zSgHHAb8*gUwXmoW6L5kANkc3g3Xfxn3cME6zAXbPgmIJ2J0cRfh1cpLiTIVoSX6q8FuaGnSAPUQ7Q*3r7PONkk*50tIJD4woTZGtWWv3TGRg*czutF254Mktd33&new=1", "http://mp.weixin.qq.com/s?src=11&timestamp=1519356986&ver=715&signature=5*apXiQwi0iwM1ak6tM8yhHM1pubRihOhTyNz6hjB*E1ARHLBzMMOcqlEJLcI-32fFS0UuNnV1lCRYeQCAVA6uZsSmE-evqmHDrQ6I7hPqAc2tXeoxtzQNJENJMuAsj0&new=1", "http://mp.weixin.qq.com/s?src=11&timestamp=1519356986&ver=715&signature=J79e5Q9mFOEPEfiAKxxftwKtPLawbGcLFAefnpV2fReseAK0*tTHD5nZpzRSRiCxXMc-qJvyPsIktN5rw54uqXbjn5uRn3VESQialsQU0gUinkPh0DS6ggD1LGFJxvH2&new=1", "http://mp.weixin.qq.com/s?src=11&timestamp=1519356986&ver=715&signature=cW*1OY3EIZ0lIxY09jFwD*JTybs4TaveeHguo824lgOaQWG4so7RX62NdvELB8xQ-qCkZ65ABzuaqT*VnuYSs6RCOP1NnWerCye8pfQzhfA2WzXxF6h6WiCFoS8MxVUH&new=1", "http://mp.weixin.qq.com/s?src=11&timestamp=1519356986&ver=715&signature=Qcny9G-wlAWWBYS85OZg52iJQPlg5cxzXmAa4ab-sC7OZkLEnd0xyxK6*XmSTUGjdFcGqjXCH7oWVNKQVjOeDMHnB6WXx5CusAnqqtRQRWvRVDnW6cuYlywMLwon6NWr&new=1", "http://mp.weixin.qq.com/s?src=11&timestamp=1519356986&ver=715&signature=we9cHgPOdbzKtknKuvs1rU1twXoW17*yPwCcDhy12fQlPkUOcDHosERaQ*ONxanDPMz24h1v1pIF7bs3Qp0rzulIiOrfu5mWTboqAe7YKXdos4cxIj1swHLgHQ2zXOGt&new=1", "http://mp.weixin.qq.com/s?src=11&timestamp=1519356986&ver=715&signature=Crh7jGxMB66fQql9*p9szKu4aItBfPRHSI9clWa2KGmb7uUIfczSboIAwsL9Se7ojMPvgu6zq75kWYEZBqI7m9KcyzdH*ZXgkaARkTU2-*5xXGM33Cr25a6L*3HpPAHM&new=1", "http://mp.weixin.qq.com/s?src=11&timestamp=1519356986&ver=715&signature=2vyYDlW8hkey8dgmgvenMcP3gBEMYFdk-vaWgCR0D*nosFqHpm04kVrEpj70kUaskALpVCuPJNAPr1QrxuZc2BMCR1gYiikk0rxjsL1bo9HboTIrU8OPFlgPgLGcCHgT&new=1", "http://mp.weixin.qq.com/s?src=11&timestamp=1519356986&ver=715&signature=-Dfqw6hIpeXcF0vYph7hG6CCnHVZHR4BOM*7zd7eSNij9P8HDQ28PEbzQol1c6iLM8QxG6*MH1WEwzjMUAYk4kB9Qj-3EYPxaBuBkzYWx60fPeDhIDFcFG2Kd8BtHHLf&new=1"],
		"son_modes": [{
			"mode_data": {
				"title": {
					"field_name": "title",
					"rule_type": "xpath",
					"field_type": "other",
					"source_type": "html",
					"field_rule": "//h2[@id='activity-name']/text()",
					"replace": ["", ""]
				},
				"create_time": {
					"field_name": "create_time",
					"rule_type": "xpath",
					"field_type": "other",
					"source_type": "html",
					"field_rule": "//*[@id='post-date']/text()",
					"replace": ["", ""]
				}
			},
			"result_type": "end"
		}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
	}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
}
base_url = "http://weixin.sogou.com/weixin?type=2&ie=utf8&query=%s"
res = Configs.ToolClassManage.SearchTools.get_key()
base_url_with_keys = [base_url % keyword for keyword in res]
for base_url in base_url_with_keys:
	Configs.ToolObjMange.extract_tool.parse_row_seed(base_url, seed_row)
