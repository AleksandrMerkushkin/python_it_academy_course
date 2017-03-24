def get_currency_rate(Demanding_list):
    import urllib2
    import json

    link = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%3D%22USDBYR%2C' \
    'EURBYR%2C%20RUBBYR%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
    URL = urllib2.urlopen(link)
    parsed_data = json.load(URL)


    new_list = {}

    for keys_value in parsed_data['query']['results']['rate']:
        if keys_value['id'] in Demanding_list:

            new_list[str(keys_value['id'])] = float(keys_value['Rate'])

    return new_list


print get_currency_rate(['USDBYR','EURBYR'])





#print u'{}:{}'.format(i['id'],int(float(i['Rate'])))
# BYRUSD = int(float(parsed_data['query']['results']['rate'][0]['Ask'])) #Convert from float to integer 18180.0000 ~ 18180
# BYREUR = int(float(parsed_data['query']['results']['rate'][1]['Ask'])) #Convert from float to integer19263.0000 ~ 19263
# BYRRUB = int(float(parsed_data['query']['results']['rate'][2]['Ask'])) #Convert from float to integer274.0469 ~ 274