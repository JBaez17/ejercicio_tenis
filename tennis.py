class Tennis():
    score = []

    def score(self):
        return score

    def iniciar_juego(self):
        global score
        score = []
        score.append(0)
        score.append(0)

    def nueva_jugada(self, jugador):
        global score
        # cada que hay una nueva jugada se verifica que aun no haya ganador
        if(self.obtener_ganador(score, jugador)):
            pass
        else:
            # guardar score antes de una nueva anotacion
            old_score = score
            score_j1 = old_score[0]
            score_j2 = old_score[1]
            # Turno para el jugador 1
            if(jugador == 1):
                if (score_j2 == "adv"):
                    self.empatar()
                elif (score_j1 == "deuce"):
                    score[0] = "adv"
                    score[1] = "-"
                elif(score_j1 == 30):
                    score[0] = old_score[0] + 10
                    score[1] = old_score[1]
                else:
                    score[0] = old_score[0] + 15
                    score[1] = old_score[1]
            # turno jugador 2
            else:
                if (score_j1 == "adv"):
                    self.empatar()
                elif(score_j2 == "deuce"):
                    score[0] = "-"
                    score[1] = "adv"
                elif(score_j2 == 30):
                    score[0] = old_score[0]
                    score[1] = old_score[1] + 10
                else:
                    score[0] = old_score[0]
                    score[1] = old_score[1] + 15
            # Marcadores igualados al terminar un turno
            if (score[0] == 40 and score[1] == 40):
                self.empatar()

    def obtener_ganador(self, scores, jugador):
        # jugador 1 gana si lleva ventaja o lleva una racha perfecta y es su
        # turno
        if ((scores[0] == "adv" or score[0] == 40) and jugador == 1):
            scores[0] = "win"
            scores[1] = "lose"
            return True
        # jugador 2 gana si lleva ventaja o lleva una racha perfecta y es su
        # turno
        elif ((scores[1] == "adv" or score[1] == 40) and jugador == 2):
            scores[1] = "win"
            scores[0] = "lose"
            return True
        return False

    def empatar(self):
        global score
        score[0] = "deuce"
        score[1] = "deuce"
