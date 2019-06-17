#author:yzh
#email:yang_create@163.com
#date:2019/06/17
#usage:json file opera

import json
params = {
	'symbol': '123456',
	'type': 'limit',
	'price': 123.4,
	'amount': 23
}
  with open('params.json','w') as fout:
       params_str = json.dump(params, fout)
  with open('params.json', 'r') as fin:
       original_params = json.load(fin)

