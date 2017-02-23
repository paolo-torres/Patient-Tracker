from twilio.rest import TwilioRestClient

ACCOUNT_SID = "**********************************"
AUTH_TOKEN = "********************************"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create
(
	to = "+1**********",
	from = "+1**********",
	body = "Hello! This is your community health worker and here are your updates for the week...",
	media_url = "https://c1.staticflickr.com/6/5536/10519774073_296682697a_z.jpg",
)