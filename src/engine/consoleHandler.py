import pygame

from src import ung_globals


class ConsoleHandler:
    font = pygame.font
    messages = list
    permanent_messages = dict
    offset_base = 100
    offset = 0

    def __init__(self):
        self.font = pygame.font.SysFont(ung_globals.font, ung_globals.fontSize)
        self.permanent_messages = dict()
        self.messages = list()

    def put_permanent_msg(self, msg_id: str, val: str):
        self.permanent_messages[msg_id] = val

    def del_permanent_msg(self, msg_id: str, val: str):
        del self.permanent_messages[msg_id]

    def put_msg(self, msg: str):
        self.messages.append(msg)

    def draw_console(self, screen: pygame.display, msg: str):
        offset = 5
        for k, v in self.permanent_messages.items():
            val = self.font.render(str(k) + ": " + str(v), True, pygame.Color('white'))
            screen.blit(val, (5, offset))
            offset += 10
