from mysite.settings import PM_API_KEY

from postmarker.core import PostmarkClient
postmark = PostmarkClient(server_token=PM_API_KEY)
postmark.emails.send(
    From='xayil89442@obxstorm.com',
    To='xayil89442@obxstorm.com',
    Subject='Postmark test',
    HtmlBody='HTML body goes here'
)