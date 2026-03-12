# Notification Data Models

class Notification:
    def __init__(self, user_id, message, created_at):
        self.user_id = user_id  # ID of the user to whom the notification is sent
        self.message = message    # Notification message
        self.created_at = created_at  # Timestamp of when the notification was created

    def __repr__(self):
        return f"<Notification(user_id={self.user_id}, message='{self.message}', created_at='{self.created_at}')>"

class EmailNotification(Notification):
    def __init__(self, user_id, message, created_at, email_address):
        super().__init__(user_id, message, created_at)
        self.email_address = email_address  # Recipient's email address

    def __repr__(self):
        return f"<EmailNotification(user_id={self.user_id}, message='{self.message}', created_at='{self.created_at}', email_address='{self.email_address}')>"

class SMSNotification(Notification):
    def __init__(self, user_id, message, created_at, phone_number):
        super().__init__(user_id, message, created_at)
        self.phone_number = phone_number  # Recipient's phone number

    def __repr__(self):
        return f"<SMSNotification(user_id={self.user_id}, message='{self.message}', created_at='{self.created_at}', phone_number='{self.phone_number}')>"

class PushNotification(Notification):
    def __init__(self, user_id, message, created_at, device_id):
        super().__init__(user_id, message, created_at)
        self.device_id = device_id  # ID of the device to which the push notification is sent

    def __repr__(self):
        return f"<PushNotification(user_id={self.user_id}, message='{self.message}', created_at='{self.created_at}', device_id='{self.device_id}')>"