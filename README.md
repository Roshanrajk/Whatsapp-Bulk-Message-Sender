# WhatsApp Bulk Message Sender

Automate sending messages via WhatsApp Web! This tool allows you to send WhatsApp messages in bulk. It reads a list of numbers from numbers.txt and sends a defined message and image to each number.
This program is created with the help of PywhatKit Module

NOTE : Only Working In Windows

## Features

- Send both image and text messages.
- Easily customizable for different country codes (currently set for Indian numbers).

## Setup

1. *Install Python*: Make sure Python is installed on your machine.
2. *Install required packages*: Run the following commands to install necessary libraries.
3. RUN 'pip install selenium'
4. RUN 'pip install pywin32'
4. RUN 'pip install webdriver-manager'
5. RUN 'pip install pywhatkit'
	

## How to Use

1. *Open WhatsApp Web*: Open your default browser and visit [web.whatsapp.com](https://web.whatsapp.com).
2. *Login*: Scan the QR code to log in to your WhatsApp account.
3. *Prepare numbers*: Enter the list of numbers in numbers.txt, each on a new line.
4. *Set image path*: Add the path of the image you want to send in the script.
5. *Run the script*: Execute Sender.py.
6. *Relax*: Watch the tool do its magic!

## Files Required

- *numbers.txt*: A text file containing phone numbers.
- 
    for example :- 98XXXXXXXX
                   78XXXXXXXX
                   87XXXXXXXX
    phone_numbers in txt file should be in this format

## Customization

- *Change Country Code*: Modify the numbers in numbers.txt to match the desired country code.
- *Update Message and Image*: Edit the message and image_path variables in Sender.py to customize the content.

## Contributions

Feel free to fork this repository and submit pull requests. Your contributions are welcome!


*GitHub Repository*: [WhatsApp Bulk Message Sender](https://github.com/roshanrajk/Whatsapp-Bulk-Message-Sender)

By following these steps and using the provided script, you can efficiently send bulk WhatsApp messages. Enjoy automating your messaging tasks!
