# -*- coding: utf-8 -*-

from module.plugins.internal.MultiHoster import MultiHoster, create_getInfo


class ZeveraCom(MultiHoster):
    __name__    = "ZeveraCom"
    __type__    = "hoster"
    __version__ = "0.25"

    __pattern__ = r'http://(?:www\.)?zevera\.com/.+'

    __description__ = """Zevera.com hoster plugin"""
    __license__     = "GPLv3"
    __authors__     = [("zoidberg", "zoidberg@mujmail.cz")]


    def handlePremium(self):
        if self.account.getAPIData(self.req, cmd="checklink", olink=self.pyfile.url) != "Alive":
            self.fail(_("Offline or not downloadable"))

        header = self.account.getAPIData(self.req, just_header=True, cmd="generatedownloaddirect", olink=self.pyfile.url)
        if not "location" in header:
            self.fail(_("Unable to initialize download"))

        self.link = header['location']


    def checkFile(self):
        super(ZeveraCom, self).checkFile()

        if self.checkDownload({"error": 'action="ErrorDownload.aspx'}) is "error":
            self.fail(_("Error response received - contact Zevera support"))


getInfo = create_getInfo(ZeveraCom)
