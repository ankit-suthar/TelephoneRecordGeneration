import csv
import random

countries = [
    ("IN", ["MH", "DL", "KA", "TN"]),
    ("US", ["CA", "NY", "TX", "FL"]),
    ("UK", ["LDN", "MAN", "BIR"]),
    ("AU", ["SYD", "MEL"]),
]

phone_types = ["MOBILE", "FIXED", "TOLLFREE", "PREMIUM", "VOIP", "M2M", "SHORTCODE"]

def generate_number(cc):
    if cc == "IN":
        return "+91" + str(random.randint(6000000000, 9999999999))
    elif cc == "US":
        return "+1" + str(random.randint(2000000000, 9999999999))
    elif cc == "UK":
        return "+44" + str(random.randint(1000000000, 7999999999))
    elif cc == "AU":
        return "+61" + str(random.randint(200000000, 999999999))
    return "+999" + str(random.randint(1000000000, 9999999999))

with open("<path-to-csv>", "w", newline="") as f:
    writer = csv.writer(f)
    # writer.writerow(["E164_Number", "Country", "Region", "Type"])

    for _ in range(10):  # 1 lakh records
        country, regions = random.choice(countries)
        region = random.choice(regions)
        phone_type = random.choice(phone_types)  # pick type randomly, independent of country
        number = generate_number(country)
        writer.writerow([number, country, region, phone_type])
