# Telephone Number Data Generator

This utility script generates **synthetic phone number datasets** in CSV format.  
It creates random E.164-compliant numbers for multiple countries, along with country code, region, and phone type.  
Useful for **testing data pipelines, Kafka ingestion, or database validation**.

---

## 🚀 Features
- Generates **random phone numbers** in valid E.164 format.
- Supports multiple countries:
  - 🇮🇳 India (`IN`) → States: MH, DL, KA, TN  
  - 🇺🇸 USA (`US`) → States: CA, NY, TX, FL  
  - 🇬🇧 UK (`UK`) → Regions: LDN, MAN, BIR  
  - 🇦🇺 Australia (`AU`) → Regions: SYD, MEL
- Phone types: `MOBILE`, `FIXED`, `TOLLFREE`, `PREMIUM`, `VOIP`, `M2M`, `SHORTCODE`.
- Writes output directly to a **CSV file**.

---

## 📊 Sample Output (CSV)
```csv
+919876543210,IN,KA,MOBILE
+14125551234,US,NY,FIXED
+447911223344,UK,LDN,VOIP
+61412345678,AU,SYD,TOLLFREE
