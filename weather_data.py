import requests

import pandas as pd
import datetime
import os
import boto3
import logging
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv

load_dotenv()

# Configure Logging
logging.basicConfig(
    filename='weather_data.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Definir variáveis de ambiente
API_KEY = os.getenv('OPENWEATHER_API_KEY')
CITY = os.getenv('CITY')
S3_BUCKET = os.getenv('S3_BUCKET')



def fetch_weather_data(api_key, city):
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(URL)
    data = response.json()
    if response.status_code != 200:
        raise Exception(f"Error fetching data from OpenWeather API: {data.get('message', '')}")
    return data

def process(data):
    weather_info = {
    'city': data['name'],
    'date': datetime.datetime.now(),
    'weather': data['weather'][0]['main'],
    'description': data['weather'][0]['description'],
    'temperature': data['main']['temp'] - 273.15,
    'humidity': data['main']['humidity'],
    'pressure': data['main']['pressure'],
    'wind_speed': data['wind']['speed']
}
    df = pd.DataFrame([weather_info])   # Create DataFrame
    return df

def save_data(df, city):
    filename = f"weather_data_{CITY}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"  # Define filename with current date 
    df.to_csv(filename, index=False) # Save to CSV
    return filename

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print(f"Upload Suceessful: {s3_file}")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
    

def main():
    data = fetch_weather_data(API_KEY, CITY)
    df = process(data)
    filename = save_data(df, CITY)
    uploaded  = upload_to_aws(filename, S3_BUCKET, filename)
        # Fazer upload para o AWS S3
    uploaded = upload_to_aws(filename, S3_BUCKET, filename)
    if uploaded:
        print(f"Arquivo enviado com sucesso para o S3: {filename}")
    else:
        print("Falha ao enviar o arquivo para o S3")

if __name__ == "__main__":
    main()

