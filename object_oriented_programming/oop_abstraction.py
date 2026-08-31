class EmailService:
    # note used protected method so that while using send method the user should not worry about the actual connection, authentication and disconnection of the server he/she can send email using only send_email method
    def _connect(self):
        print("Connecting to server")

    def _disconnect(self):
        print("Disconneting from server")

    def _auth(self, username, password):
        self.username = username
        self.password = password
        print("Logging in using username and password")
        print("Authenticated using", self.username, self.password)

    def send_email(self, username, password):
        self._connect()
        self._auth(username, password)
        print("Email has been sent")
        self._disconnect()


email = EmailService()

# note so to send email we only call send email method and all other methods are abstracted from user
email.send_email("pavan@gmail.com", "pavan@123")
