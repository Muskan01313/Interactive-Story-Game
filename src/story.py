class Story:
    def __init__(self):
        self.current_scene = "start"

    def get_scene(self):
        scenes = {
            "start": {
                "text": "You find yourself in a dark forest. Do you want to go left or right?",
                "choices": {"left": "bear_encounter", "right": "find_treasure"},
            },
            "bear_encounter": {
                "text": "You encounter a bear! Do you want to run or fight?",
                "choices": {"run": "run_away", "fight": "fight_bear"},
            },
            "run_away": {
                "text": "You run away safely. You win!",
                "choices": {},
            },
            "fight_bear": {
                "text": "The bear is too strong. You lose.",
                "choices": {},
            },
            "find_treasure": {
                "text": "You find a treasure chest! Do you want to open it?",
                "choices": {"yes": "open_chest", "no": "leave_chest"},
            },
            "open_chest": {
                "text": "You open the chest and find gold! You win!",
                "choices": {},
            },
            "leave_chest": {
                "text": "You leave the chest untouched. You lose.",
                "choices": {},
            },
        }
        return scenes[self.current_scene]

    def make_choice(self, choice):
        scene = self.get_scene()
        if choice in scene["choices"]:
            self.current_scene = scene["choices"][choice]
        else:
            self.current_scene = "start"

