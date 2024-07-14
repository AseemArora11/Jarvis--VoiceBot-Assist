from requests_html import HTMLSession

def weather():
    s = HTMLSession()
    query = "Delhi"
    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'})
    temp_element = r.html.find('span#wob_tm', first=True)
    if temp_element:
        temp = temp_element.text
    unit_element = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
    if unit_element:
        unit = unit_element.text
    desc_element = r.html.find('span#wob_dc', first=True)
    if desc_element:
        desc = desc_element.text

    return temp+" "+unit+" "+desc
