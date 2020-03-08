from twilio.rest import Client 
import os
 
account_sid = os.environ.get('twilio_account_sid') 
auth_token = os.environ.get('twilio_auth_token')  
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+14242709674',  
                              body='THIS IS MY SMS MESSAGE',      
                              to='+31614445071' 
                          ) 
 
print(message.sid)