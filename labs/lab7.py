from datetime import datetime
data = [
    ("Post code", "Cost, thousands USD", "Country", "City", "Street", "Build.", "App.", "Date"),
    (33022, 543.67, 'USA', 'New York', '53rd street', 44, 345, datetime(2020, 1, 30, 11, 45, 33, 654357).isoformat("T", "microseconds")),
    (33145, 9563214.67555478, 'UK', 'London', '45 yard av.', 3, 210, datetime(1985, 4, 2, 22, 45, 45, 45385).isoformat("T", "microseconds")),
    (33658, 85543, 'Australia', 'Sidney', 'Cristmess eve str.', 235, 3, datetime(2010, 10, 10, 10).isoformat("T", "microseconds")),
    (33854, 10, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, datetime(2008, 2, 28, 23, 33, 33).isoformat("T", "microseconds")),
    (33698, 1000000000.01, 'USA', 'Washington', 'Columbia str.', 25, 222, datetime(2021, 9, 29, 7, 34, 1, 143).isoformat("T", "microseconds"))]

for i, line in enumerate(data):
    if i == 0: 
        (post_code, cost, country, city, street, build, app, dt) = line
        txt =  f"|{post_code:^11} | {cost:^22}| {country:^11} | {city:^12} | {street:^20} | {build:^8} | {app:^6} | {dt:^28} |"
        strip = '-'
        txt2 = f"|{strip*12}+{strip*23}+{strip*13}+{strip*14}+{strip*22}+{strip*10}+{strip*8}+{strip*30}|"
        print(txt)
        print(txt2)
    if i > 0:
        (post_code, cost, country, city, street, build, app, dt) = line
        txt =  f"| {post_code:<11}| {cost/1000:>21.3f} | {country:<11} | {city:<12} | {street:<20} | {build:>8} | {app:>6} | {dt:^28} |"
        print(txt)


