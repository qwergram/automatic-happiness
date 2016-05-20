EMAIL_CONTENTS = """
From: {from_addr}\r\nTo: {to_addr}\r\nSubject: Article #{article_number}\r\n\r\nHey {admin},;
\n\n;
Within the last hour, you submitted the article ({title}). Due to company policy at;
Qwergram Entertainment Industries, we ask all writers to think about what they wrote;
for {wait_period} hours after submission. Please review what you wrote, and if you still;
feel that it is acceptable at communities such as Tumblr, Medium, Wordpress and other;abs
various sites in addition to Qwergram (After all, that's where this going to published as well),;
great! Thanks for writing another awesome article! You can ignore this email if that's the case.;
\n\n;
If you feel that you want to re-adjust the article, please delete the article here: {link} and;
send us another email.;
\n\n;
Stay awesome, {admin}. The Qwergram Bots are always here for you.;
\n\n;
With lots of <3,\n;
Hydrogen Bot & Lithium Bot;
\n\n;
The article you wrote:\n\n;
================================================================================\n\n;
{content}\n\n;
================================================================================\n\n;
""".replace(';\n', ' ')
