class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict[str, int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills.keys():
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        return (
                f"Name: {self.name}\n"
                f"Guild: {self.guild}\n"
                f"HP: {self.hp}\n"
                f"MP: {self.mp}\n" +
                (f"\n".join(f"==={s_name} - {s_mana_cost}" for s_name, s_mana_cost in self.skills.items()) if self.skills else "")
        )
