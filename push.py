from pushover import PushOver

user_key = 'user_key'
app_token = "app_token"
alert = PushOver(app_token,user_key)

alert.title = 'Welcome'
alert.sound = 'tugboat'
alert.msg = 'Hello!!! Welcome to push notification'
alert.show_message()

alert.send()