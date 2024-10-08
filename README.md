# Weather Data Pipeline

## Overview
This project implements a simple data pipeline that fetches weather data from the OpenWeather API, processes it using Pandas, and stores it locally or in Amazon S3. The script is designed to be run periodically to collect and store weather information.

## Features
- Fetches real-time weather data for a specified city
- Processes and cleans data using Pandas
- Saves data locally as CSV files
- Optionally uploads data to Amazon S3
- Configurable via environment variables
- Logging for easy debugging and monitoring

## Requirements
- Python 3.x
- OpenWeather API key
- (Optional) AWS account with S3 access

## Installation
1. Clone the repository:
  
2. Install required packages:

3. Set up environment variables:
- `OPENWEATHER_API_KEY`: Your OpenWeather API key
- `AWS_ACCESS_KEY_ID`: Your AWS access key (if using S3)
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret key (if using S3)
- `CITY`: The city for weather data (default: Teresina)
- `S3_BUCKET`: S3 bucket name (if using S3)

## Usage
Run the script manually:


For automated execution, set up a cron job or use Windows Task Scheduler.

## Configuration
Edit the `.env` file or set environment variables to configure the script:

## Output
- CSV files are saved in the `data/` directory
- Logs are written to `weather_data.log`
