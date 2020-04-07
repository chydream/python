from pygameDemo import constants


class PlayRest(object):
    __score = 0
    __lift = 3
    __blood = 1000

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value < 0:
            return None
        self.__score = value

    def set_history(self):
        if int(self.get_max_core()) < self.score:
            with open(constants.PLAY_RESULT_STORE_FILE, 'w', encoding='utf-8') as f:
                f.write('{0}'.format(self.score))

    def get_max_core(self):
        rest = 0
        with open(constants.PLAY_RESULT_STORE_FILE, 'r', encoding='utf-8') as f:
            r = f.read()
            if r:
                rest = r
            return rest
