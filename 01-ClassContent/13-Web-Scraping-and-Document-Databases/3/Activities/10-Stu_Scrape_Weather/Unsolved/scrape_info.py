import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime


# Initialize browser
def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# Function to scrape for weather in Cost Rica
def scrape_weather():

    # Initialize browser
    browser = init_browser()

    # Visit the Costa Rica climate site
    url = "https://weather-and-climate.com/average-monthly-Rainfall-Temperature-Sunshine-fahrenheit,san-jose,Costa-Rica"

    # Scrape page into soup

    # Find today's forecast

    # Get the max temp

    # Print the min temp

    # Get current time stamp

    # Store in dictionary

    # Return results
    return weather


# Function to scrape surf info
def scrape_surf():

    # Initialize browser
    browser = init_browser()

    # Visit Costa Rica surf site
    url = "https://www.surfline.com/surf-reports-forecasts-cams/costa-rica/3624060"

    # Scrape page into soup

    # Find today's surf conditions

    # Store in dictionary

    # Return results
    return surf
