# -*- coding: utf-8 -*-

from module.plugins.Account import Account


class PremiumTo(Account):
    __name__    = "PremiumTo"
    __type__    = "account"
    __version__ = "0.06"

    __description__ = """Premium.to account plugin"""
    __license__     = "GPLv3"
    __authors__     = [("RaNaN", "RaNaN@pyload.org"),
                       ("zoidberg", "zoidberg@mujmail.cz"),
                       ("stickell", "l.stickell@yahoo.it")]


    def loadAccountInfo(self, user, req):
        traffic = req.load("http://premium.to/api/traffic.php",
                           get={'username': self.username, 'password': self.password})

        if "wrong username" not in traffic:
            trafficleft = float(traffic.strip()) / 1024  #@TODO: Remove `/ 1024` in 0.4.10
            return {'premium': True, 'trafficleft': trafficleft, 'validuntil': -1}
        else:
            return {'premium': False, 'trafficleft': None, 'validuntil': None}


    def login(self, user, data, req):
        self.username = user
        self.password = data['password']
        authcode = req.load("http://premium.to/api/getauthcode.php",
                            get={'username': user, 'password': self.password}).strip()

        if "wrong username" in authcode:
            self.wrongPassword()
