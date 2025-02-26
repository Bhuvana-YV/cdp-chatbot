 
# Zeotap CDP Chatbot (Assignment 2)

##  Overview
This is a chatbot built using **Flask** that answers **"How-to"** questions about **Segment, mParticle, Lytics, and Zeotap** Customer Data Platforms (CDPs).  
It fetches documentation from official websites and returns relevant answers.

## Features
 Fetches and searches official documentation.  
 Handles "How-to" questions for multiple CDPs.  
 Returns structured JSON responses.  
 Prevents bot-blocking using **User-Agent headers**.  
 Error handling for missing documentation.  

##  Tech Stack
- **Backend:** Flask (Python)  
- **Web Scraping:** BeautifulSoup4  
- **API Requests:** Requests  

##  Installation & Setup
### 1️ Clone the Repository
```bash
git clone https://github.com/Bhuvana-YV/cdp-chatbot.git
cd cdp-chatbot
