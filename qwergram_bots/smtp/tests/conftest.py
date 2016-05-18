"""Test Hydrogen mockers"""
import pytest
from smtp.get_articles import Hydrogen


class MockMail(object):

    def __init__(self):
        self.login_count = 0
        self.select_count = 0
        self.search_count = 0
        self.fetch_count = 0
        self.copy_count = 0

    def login(self, email_addr, email_pass):
        self.login_count += 1
        return True

    def select(self, inbox):
        self.select_count += 1
        return True

    def search(self, a, b):
        self.search_count += 1
        assert a is None
        assert b == 'ALL'
        return [None, [b'0 1']]

    def copy(self, a, b):
        self.copy_count += 1
        return True

    def fetch(self, a, b):
        self.fetch_count += 1
        assert b == '(RFC822)'
        return ('OK', [[None, b"""Delivered-To: pengrabot@gmail.com
Received: by 10.237.44.135 with SMTP id g7csp1250230qtd;
        Wed, 18 May 2016 10:55:05 -0700 (PDT)
X-Received: by 10.50.180.200 with SMTP id dq8mr6560410igc.88.1463594105008;
        Wed, 18 May 2016 10:55:05 -0700 (PDT)
Return-Path: <npengra317@gmail.com>
Received: from mail-ig0-x229.google.com (mail-ig0-x229.google.com. [2607:f8b0:4001:c05::229])
        by mx.google.com with ESMTPS id 20si8590203ioe.191.2016.05.18.10.55.04
        for <pengrabot@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);
        Wed, 18 May 2016 10:55:04 -0700 (PDT)
Received-SPF: pass (google.com: domain of npengra317@gmail.com designates 2607:f8b0:4001:c05::229 as permitted sender) client-ip=2607:f8b0:4001:c05::229;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com;
       spf=pass (google.com: domain of npengra317@gmail.com designates 2607:f8b0:4001:c05::229 as permitted sender) smtp.mailfrom=npengra317@gmail.com;
       dmarc=pass (p=NONE dis=NONE) header.from=gmail.com
Received: by mail-ig0-x229.google.com with SMTP id bi2so99203692igb.0
        for <pengrabot@gmail.com>; Wed, 18 May 2016 10:55:04 -0700 (PDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20120113;
        h=mime-version:from:date:message-id:subject:to;
        bh=e/YVea2oeyv/G6kLzQkTTO89qDSOo+JKKF3wjLPgnKo=;
        b=Wd8AbANf7rZh005aG0sckJ7VF3CtcqRvaqtYVmfNytuAboo6a/hxn91G5cS5eUjpWc
         JdCNlEoQpUE9DDfjVjzsZ88CmhWEJXCe9sS+vPfOADy0Xcen3PZZeOTlL1ElMPQyoJAW
         Aiih2RLLo1ZcxjMVdIaiH0eFjwuGhlNDV02XDTFKm7bydh+33kFHyv5HyIho+Oilt2SL
         zJasatA0JxNl47QcXauGWTpPFx7DOZRWRx2BZo9eCbb5xgOi30y1pHV9qgZpZO7YZYFu
         Nq8iIvSstx4MphjpxQWZcD9Fo2gW3rCDebgh/TuCKD/wzrP/MKgxpK6Co89rf+/fob3T
         ovOQ==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20130820;
        h=x-gm-message-state:mime-version:from:date:message-id:subject:to;
        bh=e/YVea2oeyv/G6kLzQkTTO89qDSOo+JKKF3wjLPgnKo=;
        b=ezyknuvj6Bl7p+ennsCnv36teQCsJvHZZsCgHROufg1nKL9L6BhDdIyFvLYQj/yOqg
         1fFMz7HSDmNSsQUA8UijvMmpMV92mLOl53dB3KrDBhSK1cRDQNld/ZmcyD8x5YhN+ez2
         jEfrsK0rO1dmq9ktVMFRu00Y46JK+u3Y2g439puP6Ta6HvP/ae7LZ3bpiUxmhdhG/oYV
         gqiwnqMKqe5f8cn+BzJ0NgJCJWia64k2qHp53X4pTreoXbqHZQICgGyfscafMZIRK6+O
         GCipnkdETypWD9rnq9Zah+7YOZCfCn7W5QD+TdilitrhEq1VkOQ5BIXURh/5sC3VXgty
         Nb/w==
X-Gm-Message-State: AOPr4FXXlIx9+hG1bBBgnO4z+iW32qRFS3r0yKKpBAPPn62pFmGAzWL79xWPb2exVHdgeBd+iyI3/zwb3ieJsg==
X-Received: by 10.50.37.147 with SMTP id y19mr5368124igj.42.1463594103295;
 Wed, 18 May 2016 10:55:03 -0700 (PDT)
MIME-Version: 1.0
From: Norton Pengra <npengra317@gmail.com>
Date: Wed, 18 May 2016 17:54:54 +0000
Message-ID: <CAE+EAkw-VGPVdNPdctdmhEh8aRmcb5k4AwYn+TEbTiX3V_NL_Q@mail.gmail.com>
Subject: An introduction to this blog.draft.txt
To: "pengrabot@gmail.com" <pengrabot@gmail.com>
Content-Type: multipart/alternative; boundary=f46d0444006e9f7d3b0533218ef8

--f46d0444006e9f7d3b0533218ef8
Content-Type: text/plain; charset=UTF-8

I've been a coder for a lot of my life; I've been a writer for none of my
life. That'll change. I hope. At least that's the point of this new blog
I'm writing, to help me (and hopefully others) figure out how to not only
write code readable to machines, but to humans as well.

--f46d0444006e9f7d3b0533218ef8
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr">I&#39;ve been a coder for a lot of my life; I&#39;ve been =
a writer for none of my life. That&#39;ll change. I hope. At least that&#39=
;s the point of this new blog I&#39;m writing, to help me (and hopefully ot=
hers) figure out how to not only write code readable to machines, but to hu=
mans as well.</div>

--f46d0444006e9f7d3b0533218ef8--"""]])


class OfflineHydrogen(Hydrogen):

    def connect(self):
        self.connected = True
        self.mail = MockMail()


@pytest.fixture
def HydrogenBot():
    return OfflineHydrogen(
        email_addr="test@test.com",
        email_pass="amazing_password1",
        email_imap="imap.totally_valid_server.net",
    )
