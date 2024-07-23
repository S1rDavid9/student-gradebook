#!/usr/bin/python3
class Course:
    def __init__(self, course_id, name, trimester, credits):
        self.course_id = course_id
        self.name = name
        self.trimester = trimester
        self.credits = credits

    def to_string(self):
        return f'{self.course_id}|{self.name}|{self.trimester}|{self.credits}'

    @classmethod
    def from_string(cls, data):
        try:
            parts = data.strip().split('|')
            course_id = int(parts[0])
            name = parts[1]
            trimester = parts[2]
            credits = int(parts[3])
            return cls(course_id, name, trimester, credits)
        except (IndexError, ValueError) as e:
            print(f"Error parsing course data: {data}. Error: {e}")
            return None
