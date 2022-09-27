

class URLs:

    def __init__(self):
        self.base_url = 'https://api.oireachtas.ie/v1'

        #endpoints
        self.legislation = "/legislation"
        self.debates = '/debates'
        self.constituencies = '/constituencies'
        self.parties = '/parties'
        self.divisions = '/divisions'
        self.questions = '/questions'
        self.houses = '/houses'
        self.members = '/members'

    #Merges all the base urls with the relevant endpoints
    #Does not access any parameters on its own
    def base_url(self):
        return self.base_url

    def legislation_url(self):
        return self.base_url + self.legislation

    def debate_url(self):
        return self.base_url + self.debates

    def constituencies_url(self):
        return self.base_url + self.constituencies

    def parties_url(self):
        return self.base_url + self.parties

    def divisions_url(self):
        return self.base_url + self.divisions

    def questions_url(self):
        return self.base_url + self.questions

    def houses_url(self):
        return self.base_url + self.houses

    def members_url(self):
        return self.base_url + self.members
