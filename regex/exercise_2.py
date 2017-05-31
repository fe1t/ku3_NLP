#!/usr/bin/python
# - *da - coding: utf-8 - * -

import re

with open('./price_2013-01-28_3.htm', 'rb') as f:
    data_lines = f.read().splitlines()

content = "".join(data_lines)
main_table_re = re.compile('<table width="100%" border="0" cellpadding="4" cellspacing="1">.*<\/table>')
content = main_table_re.search(content).group(0)
detail = re.findall('<td.+?class="txt_12nor">(.*?)<\/td>', content)

name = ""
output_format = "ประเภทสินค้า: {product_type}\nรายละเอียด: {product_detail}\nราคา: {product_price} {product_unit}\nจุดรับซื้อ: {product_place}\nวันที่: {product_date}\n"
for i in range(0, len(detail), 6):
    if detail[i] == '':
        detail[i] = name
    name = detail[i]
    print output_format.format(product_type=detail[i], product_detail=detail[i+1], product_price=detail[i+2], product_unit=detail[i+3], product_place=detail[i+4], product_date=detail[i+5])

