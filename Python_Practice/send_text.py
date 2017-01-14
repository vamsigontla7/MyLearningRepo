from twilio.rest import TwilioRestClient

account_sid = "AC0fb15704356a131207798cdae88dceee"      # Your Account SID from www.twilio.com/console
auth_token = "2a8d5aee78bdd8ab4f0fb49141540943"         # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(body="Vamsy !!!!",
                                 to="+19728857413",    # Replace with your phone number
                                 from_="+13257540691") # Replace with your Twilio number
print(message.sid)
