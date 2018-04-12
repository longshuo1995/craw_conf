

class Eval(object):
    def reserve_eval(self, res, code):
        g = {
            'res': res
        }
        print(code)
        return eval(code, g)
