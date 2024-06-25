import pywhatkit as kit
import time

# Function to read phone numbers from a text file
def read_phone_numbers(file_path):
    with open(file_path, 'r') as file:
        phone_numbers = ['+91' + line.strip() for line in file.readlines()]
    return phone_numbers

# Read phone numbers from the file
phone_numbers = read_phone_numbers('phone_numbers.txt')

# Path to the photo you want to send
photo_path = r'enter path to img.png'

# Message you want to send after the photo
message = ''' ENTER YOUR CUSTOM MESSAGE '''

# Function to send photo
def send_photo(phone, photo_path, caption):
    try:
        kit.sendwhats_image(phone,photo_path, message, 10)
        print(f"Photo sent to {phone}")
    except Exception as e:
        print(f"Failed to send photo to {phone}: {e}")

# Function to send message
def send_message(phone, message):
    # Schedule message to be sent 1 minutes from now
    current_hour = time.localtime().tm_hour
    current_minute = time.localtime().tm_min + 1

    try:
        kit.sendwhatmsg(phone, message, current_hour, current_minute)
        print(f"Message scheduled to {phone}")
    except Exception as e:
        print(f"Failed to schedule message to {phone}: {e}")

# Iterate over the list of phone numbers and send the photo followed by the message
for phone in phone_numbers:
    #sending message with the photo(not seperate)
    send_photo(phone, photo_path, caption="")
    time.sleep(5)  # Wait before scheduling the message to ensure the photo is sent
    #use this if you want to send message after sending photo
    #send_message(phone, message)
    #time.sleep(60)  # Wait to avoid sending messages at the exact same time
