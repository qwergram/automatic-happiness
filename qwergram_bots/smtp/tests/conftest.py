"""Test Hydrogen mockers"""
import pytest
from smtp.get_articles import Hydrogen


class MockMail(object):

    def __init__(self):
        self.login_count = 0
        self.select_count = 0
        self.search_count = 0
        self.fetch_count = 0

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

    def fetch(self, a, b):
        self.fetch_count += 1
        assert b == '(RFC822)'
        return ('OK', [[None, b"""Delivered-To: pengrabot@gmail.com
Received: by 10.237.44.135 with SMTP id g7csp785660qtd;
        Mon, 16 May 2016 16:14:40 -0700 (PDT)
X-Received: by 10.50.37.147 with SMTP id y19mr12398194igj.42.1463440480335;
        Mon, 16 May 2016 16:14:40 -0700 (PDT)
Return-Path: <npengra317@gmail.com>
Received: from mail-io0-f182.google.com (mail-io0-f182.google.com. [209.85.223.182])
        by mx.google.com with ESMTPS id q10si21957itc.2.2016.05.16.16.14.40
        for <pengrabot@gmail.com>
        (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);
        Mon, 16 May 2016 16:14:40 -0700 (PDT)
Received-SPF: pass (google.com: domain of npengra317@gmail.com designates 209.85.223.182 as permitted sender) client-ip=209.85.223.182;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com;
       spf=pass (google.com: domain of npengra317@gmail.com designates 209.85.223.182 as permitted sender) smtp.mailfrom=npengra317@gmail.com;
       dmarc=pass (p=NONE dis=NONE) header.from=gmail.com
Received: by mail-io0-f182.google.com with SMTP id i75so1074ioa.3
        for <pengrabot@gmail.com>; Mon, 16 May 2016 16:14:40 -0700 (PDT)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20120113;
        h=mime-version:from:date:message-id:subject:to;
        bh=01OBxpty28kmJr3zBNVQJYkHvdpPtA5xl4trVtkmExY=;
        b=Kh7LVeJzX1eXHE2AGOtxX18+FVCGYe9B/WJszT8ciZRWe0Tgpfk3oWcxQtKd0WWZw4
         +s/Gx/G/7+L6ttmWDXlFrpLz6R5sum8NzuZLbE8keBTCEqyRLkQHgjSRPlZR10D4T/Td
         a1zpQ80QRLFJG4jbleLf7WFXLXzbIc1dyFhacgydzYsmkbWgFmBkss5u+XmhE+GigL/9
         svvKUxPZKf3ACQJi/GlNjqO72mjEYn0Pqu/tYiwo7inZU9+dkXe4I4/n7E8jbAYSJoAi
         RdvoqIytRVKQEkJ/PUyhKdGXbE2KlDGS0HE8Hw30NclEncdvGx05cTdqTiV594UJkMJv
         ByHA==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20130820;
        h=x-gm-message-state:mime-version:from:date:message-id:subject:to;
        bh=01OBxpty28kmJr3zBNVQJYkHvdpPtA5xl4trVtkmExY=;
        b=TWxBOHynl8nSGlmOurRWDOqPZRzthhpIRWCJnWARzAVW6PrwUKyNr+dzBPAllntuzW
         3Bavd+0oawRXg3zuIxweIhGKeF4AIt32+aSuj5NRzwGpIXF1fq4aenguf3RV0l2OYxvs
         wkDXHXhdzg79eWeVKYI+QdcYeu+qBLAAtZH2fx5fgNO+U3ni/hHnYT9+wsShLwKTHoto
         7szOAJi2h/XCMlqrd68EVoiupGwweGL6V+IoyAhwOpdzRBnWXWWi6sOOpo9kg0X3Ovkv
         nZwjzdTRk8TnVJwpFK21wam6qGRqA2JwJIi288iPf1iskWGwnd3VO5zVLYE0E8JrJpoH
         wYbg==
X-Gm-Message-State: AOPr4FVHBigf0qjtT1nY9j4eq0BVpknehv+ViLzw26Uae4xnQ3mj3jMuNgS8zdd+mv+UUmkFnaG03Y/kRMjRHw==
X-Received: by 10.107.175.67 with SMTP id y64mr11359849ioe.113.1463440480203;
 Mon, 16 May 2016 16:14:40 -0700 (PDT)
MIME-Version: 1.0
From: Norton Pengra <npengra317@gmail.com>
Date: Mon, 16 May 2016 23:14:30 +0000
Message-ID: <CAE+EAkyV9f6Y8AwA26jbdccqFVbisFtVLOUY7NVUyDoyZ9DnEg@mail.gmail.com>
Subject: share.sjson
To: "pengrabot@gmail.com" <pengrabot@gmail.com>
Content-Type: multipart/alternative; boundary=001a114464fef8fb100532fdc913

--001a114464fef8fb100532fdc913
Content-Type: text/plain; charset=UTF-8

url..https://www.youtube.com/watch?v=1DJZHFwWjqU;
title..Zella Day is such an amazing artist;
short_description..Title says it all.;

--001a114464fef8fb100532fdc913
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr"><span style=3D"font-size:13px;color:rgb(33,33,33);font-fam=
ily:&#39;helvetica neue&#39;,helvetica,arial,sans-serif">url..</span><a hre=
f=3D"https://www.youtube.com/watch?v=3D1DJZHFwWjqU" style=3D"font-size:13px=
;font-family:&#39;helvetica neue&#39;,helvetica,arial,sans-serif">https://w=
ww.youtube.com/watch?v=3D1DJZHFwWjqU</a>;<div style=3D"font-size:13px;color=
:rgb(33,33,33);font-family:&#39;helvetica neue&#39;,helvetica,arial,sans-se=
rif">title..Zella Day is such an amazing artist;</div><div style=3D"font-si=
ze:13px;color:rgb(33,33,33);font-family:&#39;helvetica neue&#39;,helvetica,=
arial,sans-serif">short_description..Title says it all.;</div></div>

--001a114464fef8fb100532fdc913--"""]])


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
