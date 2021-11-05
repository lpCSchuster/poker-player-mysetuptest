
class Player:
    VERSION = "Far away from beeing good :)"

    def betRequest(self, game_state):
        current_buy_in = game_state["current_buy_in"]
        in_action = game_state["in_action"]
        players = game_state["players"]

        # just check everything
        check_value = current_buy_in - players[in_action]["bet"]
        return check_value

    def showdown(self, game_state):
        pass

