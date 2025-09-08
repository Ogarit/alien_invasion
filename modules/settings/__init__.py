class Settings():
    """Uma classe para armazenar todas as configurações da Invasão Alienígena.
    """

    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 23, 41)

        # Configurações da espaçonave
        self.ship_speed_factor = 1.25

        # Configurações dos projéteis
        self.bullet_speed_factor = 2
        self.bullet_width = 2
        self.bullet_height = 20
        self.bullet_color = (186, 55, 0)
        self.bullets_allowed = 3
