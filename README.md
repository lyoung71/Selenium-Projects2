Users will need to install Selenium and the driver of their choice. I prefer Chrome, so I used Chromedriver.

Path to driver will need to be updated to the path of the user's driver file if using older version of Selenium.

ClassReminder.py
    What it does: uses MacOS's crontab to automatically send me a Whatsapp message every morning with my teaching schedule for that day.

    How it does it: Uses datetime module to retrieve today's date and formats it in a way that matches the HTML. This allows Selenium to return only the students' names and class times that are scheduled for the current day. It then saves this information in a list, redirects to Whatsapp, finds my contact, and sends me a message.

email_bot.py
    What it does: automatically sends an email to the recipient of your choice.

    How it does it: uses Selenium to take user's inputs and automatically fill out the "to", "subject", and "message" sections and then simulates the ENTER key to send the email.

happy_girlfriend.py
    What it does: automatically sends a sweet message to my girlfriend that changes depending on the time of day that I run the script.

    How it does it: uses datetime module to find current time and choose the corresponding message. Then uses Selenium to open up Whatsapp, find the chat with my girlfriend, and send her the message with an additional kissy face emoji.

twitter_bot.py
    What it does: automatically tweets a different emoji every minute for 10 minutes.

    How it does it: Uses a while loop to iterate through a list containing the names of the emojis on Twitter's website as they appear in the HTML. It then uses an f-string to insert the emoji's name into the Selenium command, select the emoji, and tweet it. After each tweet, the program increments a count variable which allows the selection of the next emoji in the list. Finally, the program sleeps for one minute before starting the next iteration. 
