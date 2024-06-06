import imaplib
import email

app_password = 'yvqcresgbkdcpthm'
# Connect to the IMAP server
mail = imaplib.IMAP4_SSL('imap.gmail.com')

# Login with credentials
mail.login('sheena.lu@ui.com', app_password)

# Select a mailbox
mail.select('INBOX')

# Search for emails with the specified title
search_criteria = '(SUBJECT "Verify Your UI SSO Account Email")'
result, data = mail.search(None, search_criteria)

# Process the search results
if result == 'OK':
    email_ids = data[0].split()
    for email_id in email_ids:
        # Fetch the email using its ID
        result, email_data = mail.fetch(email_id, '(RFC822)')
        if result == 'OK':
            raw_email = email_data[0][1]
            # Parse the raw email data into an email object
            msg = email.message_from_bytes(raw_email)
            # Print or process the email object as needed
            print(f"Subject: {msg['Subject']}")
            print(f"From: {msg['From']}")
            # Get email body
            email_body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == 'text/plain':
                        email_body += part.get_payload(decode=True).decode()
            else:
                email_body = msg.get_payload(decode=True).decode()
            # Print email body
            print("Body:")
            print(email_body)
            print("\n---\n")  # Separator between emails
else:
    print("Failed to search for emails.")

# Logout from the mailbox
mail.logout()