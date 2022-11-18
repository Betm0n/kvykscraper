# kvykscraper
Automated price scraper which responds to emails with price comparison list.

Requirements:

  Microsoft Outlook application.
  
How it works:

  The code looks for unread emails in the outlook application.
  
  Downloads the excel attachments which contains the list of product names whose prices need to scraped for the sake of price comparison.
  
  Reads the excel file and starts scraping 3 different e-commerce websites - Amazon, Flipkart, and Snapdeal.
  
  Appends the prices to the excel file accordingly 
  
  Automatically replies to the sender of the email with the modified file as an attachment.
