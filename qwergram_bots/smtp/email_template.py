email_contents = """
From: {from_addr}\r\nTo: {to_addr}\r\nSubject: Article #{article_number}\r\n\r\n
Hey {admin},

Within the last hour, you submitted the article ({title}). Due to company policy at
Qwergram Entertainment Industries, we ask all writers to think about what they wrote
for {wait_period} hours after submission. Please review what you wrote, and if you still
feel that it is acceptable at communities such as Tumblr, Medium, Wordpress and other
various sites in addition to Qwergram (After all, that's where this going to published as well),
great! Thanks for writing another awesome article! You can ignore this email if that's the case.

If you feel that you want to re-adjust the article, please delete the article here: {link} and
send us another email.

Stay awesome, {admin}. The Qwergram Bots are always here for you.

With lots of <3,
Hydrogen Bot & Lithium Bot

The article you wrote:
================================================================================
{content}
================================================================================
"""
