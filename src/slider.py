import pygame
pygame.init()

# ---------- Klasa prostego pionowego suwaka ----------
class VerticalSlider:
    def __init__(self, x, y, width, height, name, min_val=0, max_val=100, initial=50, step=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.name = name
        self.min = float(min_val)
        self.max = float(max_val)
        self.value = float(initial)
        self.step = step
        self.dragging = False
        self.handle_size = width + 6  # kwadratowy uchwyt nieco większy
        self.value = max(self.min, min(self.value, self.max))

    def _val_to_y(self, v):
        t = (v - self.min) / (self.max - self.min)
        return int(self.rect.bottom - t * self.rect.height)

    def _y_to_val(self, y):
        t = (self.rect.bottom - y) / self.rect.height
        v = self.min + t * (self.max - self.min)
        if self.step:
            k = round((v - self.min) / self.step)
            v = self.min + k * self.step
        return max(self.min, min(v, self.max))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            hx, hy = self.rect.centerx, self._val_to_y(self.value)
            handle_rect = pygame.Rect(hx - self.handle_size // 2, hy - self.handle_size // 2,
                                      self.handle_size, self.handle_size)
            if handle_rect.collidepoint(mx, my) or self.rect.collidepoint(mx, my):
                self.dragging = True
                self.value = self._y_to_val(my)
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            _, my = event.pos
            self.value = self._y_to_val(my)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False

    def draw(self, surf, font):
        # tor
        pygame.draw.rect(surf, (150, 150, 150), self.rect)
        pygame.draw.rect(surf, (255, 255, 255), self.rect, 2)

        # uchwyt
        hy = self._val_to_y(self.value)
        hx = self.rect.centerx
        handle_rect = pygame.Rect(hx - self.handle_size // 2, hy - self.handle_size // 2,
                                  self.handle_size, self.handle_size)
        pygame.draw.rect(surf, (200, 200, 200), handle_rect)
        pygame.draw.rect(surf, (255, 255, 255), handle_rect, 2)

        # napisy
        name_text = font.render(self.name, True, (255, 255, 255))
        val_text = font.render(f"{self.value:.0f}", True, (255, 255, 255))
        surf.blit(name_text, (self.rect.centerx - name_text.get_width() // 2, self.rect.top - 45))
        surf.blit(val_text, (self.rect.centerx - val_text.get_width() // 2, self.rect.top - 25))

    def get_value(self):
        return self.value

# ---------- Główna pętla ----------
def main():
    W, H = 400, 320
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Trzy pionowe suwaki (ciemny motyw)")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    sliders = [
        VerticalSlider(80, 80, 30, 200, name="A", min_val=0, max_val=100, initial=50, step=1),
        VerticalSlider(180, 80, 30, 200, name="B", min_val=0, max_val=100, initial=25, step=1),
        VerticalSlider(280, 80, 30, 200, name="C", min_val=0, max_val=100, initial=75, step=1),
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for s in sliders:
                s.handle_event(event)

        screen.fill((0, 0, 0))

        for s in sliders:
            s.draw(screen, font)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
