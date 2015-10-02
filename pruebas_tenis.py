import unittest
from tennis import Tennis


class Test_Tennis(unittest.TestCase):

    # inicializar objeto de la clase
    def setUp(self):
        self.marcador = Tennis()

    # iniciar el juego con los marcadores en 0
    def test_iniciar_juego(self):
        self.marcador.iniciar_juego()
        self.assertEqual([0, 0], self.marcador.score())

    # Para cada partida se genera un nuevo juego
    # Incrementar el puntaje del jugador 1
    def test_marcador_15_0(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.assertEqual([15, 0], self.marcador.score())

    # Incrementar el puntaje del jugador 1 y 2
    def test_marcador_15_15(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.assertEqual([15, 15], self.marcador.score())

    # Incrementar el puntaje del jugador 1 2 veces, y del jugador 1 1 vez
    def test_marcador_30_15(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(1)
        self.assertEqual([30, 15], self.marcador.score())

    # Incrementar el puntaje del jugador 1 3 veces y el del jugador 2 1 vez
    def test_marcador_40_15(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.assertEqual([40, 15], self.marcador.score())

    # Incrementar el puntaje del jugador 1 3 veces y el del jugador 2 2 veces
    def test_marcador_40_30(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.assertEqual([40, 30], self.marcador.score())

    # Incrementar el puntaje del jugador 1 2 veces y el del jugador 2 3 veces
    def test_marcador_30_40(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.assertEqual([30, 40], self.marcador.score())

    # los marcadores se igual 40 a 40, entonces cambian a deuce
    def test_marcador_40_40_deuce(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.assertEqual(["deuce", "deuce"], self.marcador.score())

    # los marcadores estan en deuce y el jugador 1 hace otro punto, jugador 1
    # tiene ventaja (adv)
    def test_marcador_J1adv_J2dis(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(1)
        self.assertEqual(["adv", "-"], self.marcador.score())

    # los marcadores estan en deuce y el jugador 2 hace otro punto, jugador 2
    # tiene ventaja (adv)
    def test_marcador_J1dis_J2adv(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.assertEqual(["-", "adv"], self.marcador.score())

    # jugador 1 tiene ventaja y hace otro punto, jugador 1 gana
    def test_marcador_j1_win_with_adv(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.assertEqual(["win", "lose"], self.marcador.score())

    # jugador 2 tiene ventaja y hace otro punto, jugador 2 gana
    def test_marcador_j2_win_with_adv(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.assertEqual(["lose", "win"], self.marcador.score())

    # jugador 1 tiene 40 en el marcador y el jugador 2 menos de 40, el jugador
    # 1 obtiene otro punto, jugador 1 gana
    def test_marcador_j1_win_perfect(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(1)
        self.assertEqual(["win", "lose"], self.marcador.score())

    # jugador 2 tiene 40 en el marcador y el jugador 1 menos de 40, el jugador
    # 2 obtiene otro punto, jugador 2 gana
    def test_marcador_j2_win_perfect(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.assertEqual(["lose", "win"], self.marcador.score())

    # Jugador 2 obtiene ventaja sobre jugador 1, jugador obtiene otro punto,
    # el marcador vuelve a deuce
    def test_marcador_again_deuce(self):
        self.marcador.iniciar_juego()
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(1)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(2)
        self.marcador.nueva_jugada(1)
        self.assertEqual(["deuce", "deuce"], self.marcador.score())


if __name__ == '__main__':
    unittest.main()
