import requests
import pandas as pd

# تنظیمات اولیه
TOKEN = "b84b6d018f20c43049d96df7fc4be5badee65d9c"  # توکن خودت رو اینجا بزار
CITY = "bilbao"
url = f"https://api.waqi.info/feed/{CITY}/?token={TOKEN}"

def get_air_quality_data():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['data']
        
        # استخراج داده‌های اصلی
        extracted_data = {
            'timestamp': data['time']['s'],
            'city': data['city']['name'],
            'latitude': data['city']['geo'][0],
            'longitude': data['city']['geo'][1],
            'aqi': data['aqi'],
            'dominant_pollutant': data['dominantoppin']
        }
        
        # استخراج آلاینده‌ها و داده‌های هواشناسی (iaqi)
        # این بخش شامل پارامترهایی مثل دما (t) و سرعت باد (w) هم هست
        iaqi = data['iaqi']
        for param in iaqi:
            extracted_data[param] = iaqi[param]['v']
            
        return extracted_data
    else:
        print("Error fetching data:", response.status_code)
        return None

# ۱. دریافت داده
entry = get_air_quality_data()

if entry:
    # ۲. تبدیل به DataFrame
    df = pd.DataFrame([entry])
    
    # تغییر نام ستون‌های هواشناسی برای خوانایی بیشتر در EDA
    rename_dict = {
        't': 'temperature',
        'w': 'wind_speed',
        'h': 'humidity',
        'p': 'pressure'
    }
    df.rename(columns=rename_dict, inplace=True)
    
    # ۳. ذخیره در فایل CSV
    # اگر فایل از قبل باشد، داده جدید به آن اضافه می‌شود (مناسب برای جمع‌آوری داده روزانه)
    df.to_csv('bilbao_air_quality.csv', mode='a', index=False, header=not pd.io.common.file_exists('bilbao_air_quality.csv'))
    
    print("data saved to bilbao_air_quality.csv")
    print(df.head())