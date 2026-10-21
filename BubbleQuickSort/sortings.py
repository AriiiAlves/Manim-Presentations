# ManimGL: vídeo contínuo, sem dependência de manim-slides.
# Renderizar: manimgl sorting_video.py QuickSort -w --video_dir ./videos
# Outra cena: manimgl sorting_video.py BubbleSort -w --video_dir ./videos
# SPEED controla a velocidade; WAIT_TAX controla as pausas de leitura.
from manimlib import *

SPEED = 1.0
INTERNAL_SPEED = 1.0 / SPEED

WRITE_TAX = 2.0
FADEIN_TAX = 1.0
FADEOUT_TAX = 1.0
DRAW_SQUARES_TAX = 2.0
SWAP_SQUARES_TAX = 1.0
PAINT_SQUARES_TAX = 1.0
WAIT_TAX = 3.0

class BubbleSort(Scene):
    def construct(self):
        # 1. Title and description
        title = Text("Bubble Sort", font_size=72)
        subtitle = Text(
            """
            O bubble sort consiste em verificar dois itens consecutivos de uma lista (vetor).\n
            Se o primeiro item for maior que o segundo, eles são trocados.\n
            Isso se repete até que nenhuma troca seja feita ao percorrer a lista por inteiro.
            """,
            font_size=24,
            t2c={"consecutivos": BLUE, "trocados": ORANGE}
        )
        subtitle.next_to(title, DOWN, buff=1)
        self.play(Write(title), run_time=WRITE_TAX*INTERNAL_SPEED)
        self.play(FadeIn(subtitle, UP), run_time=FADEIN_TAX*INTERNAL_SPEED)
        #self.wait(WAIT_TAX * INTERNAL_SPEED)
        self.wait(WAIT_TAX * INTERNAL_SPEED)

        # 2. Array Visualization
        vector = ["3","1","7","5","6"]
        squares = VGroup()

        for x in vector:
            square = Square(side_length=1)
            text = Text(x, font_size=24)
            text.move_to(square.get_center())
            squares.add(VGroup(square, text))

        squares.arrange(RIGHT, buff=0) # Arrange squares horizontally
        self.play(FadeOut(title), FadeOut(subtitle), run_time=FADEOUT_TAX*INTERNAL_SPEED)
        self.play(ShowCreation(squares), run_time=DRAW_SQUARES_TAX*INTERNAL_SPEED)

        text = Text("Este é um vetor de inteiros aleatórios. Utilizaremos Bubble Sort para ordená-lo.", font_size=24)
        text.next_to(squares, DOWN, buff=1)
        self.play(Write(text), run_time=WRITE_TAX*INTERNAL_SPEED)
        #self.wait(WAIT_TAX*INTERNAL_SPEED)
        self.wait(WAIT_TAX * INTERNAL_SPEED)
        self.play(FadeOut(text), run_time=FADEOUT_TAX*INTERNAL_SPEED)

        # Complete sorting
        swapFlag = True
        while(swapFlag):
            swapFlag = False
            upper_text = None
            for i in range(0, len(vector)-1):
                if(int(vector[i]) > int(vector[i+1])):
                    self.play(
                        squares[i][0].animate.set_fill(RED, opacity=0.5),
                        squares[i+1][0].animate.set_fill(RED, opacity=0.5),
                        run_time=PAINT_SQUARES_TAX*INTERNAL_SPEED
                    )
                    text = Text("O primeiro item é maior que o segundo. Trocamos.", font_size=24)
                    upper_text = Tex(rf"{vector[i]} > {vector[i+1]}")
                    text.next_to(squares,DOWN,buff=1)
                    upper_text.next_to(squares,UP,buff=1)
                    self.play(FadeIn(text), FadeIn(upper_text), run_time=FADEIN_TAX*INTERNAL_SPEED)
                    #self.wait(WAIT_TAX*INTERNAL_SPEED)
                    self.wait(WAIT_TAX * INTERNAL_SPEED)
                    self.play(FadeOut(text), run_time=FADEOUT_TAX*INTERNAL_SPEED)

                    vector[i], vector[i+1] = vector[i+1], vector[i]

                    self.wait(WAIT_TAX * INTERNAL_SPEED)
                    self.play(
                        ApplyMethod(squares[i].move_to, squares[i+1].get_center()),
                        ApplyMethod(squares[i+1].move_to, squares[i].get_center()),
                        run_time=SWAP_SQUARES_TAX*INTERNAL_SPEED
                    )
                    squares.submobjects[i], squares.submobjects[i+1] = (
                        squares.submobjects[i+1],
                        squares.submobjects[i]
                    )

                    self.wait(WAIT_TAX * INTERNAL_SPEED)
                    self.play(
                        squares[i][0].animate.set_fill(GREEN, opacity=0.5),
                        squares[i+1][0].animate.set_fill(GREEN, opacity=0.5),
                        run_time=PAINT_SQUARES_TAX*INTERNAL_SPEED
                    )

                    text = Text("Ordenados. Próximo.", font_size=24)
                    text.next_to(squares,DOWN,buff=1)
                    new_upper_text = Tex(rf"{vector[i]} < {vector[i+1]}")
                    new_upper_text.next_to(squares,UP,buff=1)
                    self.play(Transform(upper_text, new_upper_text), run_time=WRITE_TAX*INTERNAL_SPEED)
                    self.play(FadeIn(text))
                    #self.wait(WAIT_TAX*INTERNAL_SPEED)
                    self.wait(WAIT_TAX * INTERNAL_SPEED)
                    self.play(FadeOut(new_upper_text), FadeOut(upper_text), FadeOut(text), run_time=FADEOUT_TAX*INTERNAL_SPEED)

                    swapFlag = True

                elif int(vector[i]) == int(vector[i+1]):
                    self.play(
                        squares[i][0].animate.set_fill(GREEN, opacity=0.5),
                        squares[i+1][0].animate.set_fill(GREEN, opacity=0.5),
                        run_time=PAINT_SQUARES_TAX*INTERNAL_SPEED
                    )

                    text = Text("Os itens são iguais. Não há troca.", font_size=24)
                    text.next_to(squares,DOWN,buff=1)
                    upper_text = Tex(rf"{vector[i]} = {vector[i+1]}")
                    upper_text.next_to(squares,UP,buff=1)
                    self.play(FadeIn(text), FadeIn(upper_text), run_time=FADEIN_TAX*INTERNAL_SPEED)
                    #self.wait(WAIT_TAX*INTERNAL_SPEED)
                    self.wait(WAIT_TAX * INTERNAL_SPEED)
                    self.play(FadeOut(upper_text), FadeOut(text), run_time=FADEOUT_TAX*INTERNAL_SPEED)
                else:
                    self.play(
                        squares[i][0].animate.set_fill(GREEN, opacity=0.5),
                        squares[i+1][0].animate.set_fill(GREEN, opacity=0.5),
                        run_time=PAINT_SQUARES_TAX*INTERNAL_SPEED
                    )
                    text = Text("Os itens já estão ordenados. Não há troca.", font_size=24)
                    text.next_to(squares,DOWN,buff=1)
                    upper_text = Tex(rf"{vector[i]} < {vector[i+1]}")
                    upper_text.next_to(squares,UP,buff=1)
                    self.play(FadeIn(text), FadeIn(upper_text), run_time=FADEIN_TAX*INTERNAL_SPEED)
                    #self.wait(WAIT_TAX*INTERNAL_SPEED)
                    self.wait(WAIT_TAX * INTERNAL_SPEED)
                    self.play(FadeOut(upper_text), FadeOut(text), run_time=FADEOUT_TAX*INTERNAL_SPEED)

                self.play(
                    squares[i][0].animate.set_fill(opacity=0),
                    squares[i+1][0].animate.set_fill(opacity=0),
                    run_time=PAINT_SQUARES_TAX*INTERNAL_SPEED
                )

            if(swapFlag):
                text = Text("Como no mínimo uma troca foi feita, teremos que percorrer o vetor novamente.", font_size=24)
                text.next_to(squares,DOWN,buff=1)
                self.play(FadeIn(text), run_time=FADEIN_TAX*INTERNAL_SPEED)
                #self.wait(WAIT_TAX*INTERNAL_SPEED)
                self.wait(WAIT_TAX * INTERNAL_SPEED)
                self.play(FadeOut(text), run_time=FADEOUT_TAX*INTERNAL_SPEED)
            else:
                text = Text("Como nenhuma troca foi feita, o vetor está ordenado.", font_size=24)
                text.next_to(squares,DOWN,buff=1)
                self.play(FadeIn(text), run_time=FADEIN_TAX*INTERNAL_SPEED)
                #self.wait(WAIT_TAX*INTERNAL_SPEED)
                self.wait(WAIT_TAX * INTERNAL_SPEED)
                self.play(FadeOut(text), run_time=FADEOUT_TAX*INTERNAL_SPEED)

class QuickSort(Scene):
    def construct(self):
        T_MOVE = PAINT_SQUARES_TAX * INTERNAL_SPEED
        T_SWAP = SWAP_SQUARES_TAX * INTERNAL_SPEED
        T_FADE = FADEIN_TAX * INTERNAL_SPEED

        def pause():
            # Pausa de leitura no vídeo contínuo.
            self.wait(WAIT_TAX * INTERNAL_SPEED)

        # 1. Introdução
        title = Text("Quick Sort", font_size=72)
        intro = VGroup(
            Text(
                "Vamos ordenar números dividindo o problema em partes menores.",
                font_size=26,
            ),
            Text(
                "1. Escolhemos um número de referência: o pivô.",
                font_size=24,
            ),
            Text(
                "2. Separamos os menores ou iguais dos maiores.",
                font_size=24,
            ),
            Text(
                "3. Repetimos o processo nos dois grupos.",
                font_size=24,
            ),
        ).arrange(DOWN, buff=0.3)

        intro.next_to(title, DOWN, buff=0.7)

        self.play(Write(title), run_time=WRITE_TAX * INTERNAL_SPEED)
        self.play(FadeIn(intro), run_time=T_FADE)
        pause()

        self.play(
            FadeOut(title),
            FadeOut(intro),
            run_time=FADEOUT_TAX * INTERNAL_SPEED,
        )

        # 2. Vetor visual
        vector = [3, 1, 7, 5, 6]
        squares = VGroup()

        for value in vector:
            square = Square(side_length=1)
            number = Text(str(value), font_size=28)
            number.move_to(square.get_center())
            squares.add(VGroup(square, number))

        squares.arrange(RIGHT, buff=0).move_to(ORIGIN)

        # Posições fixas: textos e marcadores não dependem das peças em movimento.
        positions = [
            squares[k].get_center().copy()
            for k in range(len(vector))
        ]
        upper_position = squares.get_center() + UP * 1.8
        lower_position = squares.get_center() + DOWN * 1.8

        self.play(
            ShowCreation(squares),
            run_time=DRAW_SQUARES_TAX * INTERNAL_SPEED,
        )

        upper = None
        lower = None

        def message(text, above=False, size=23):
            nonlocal upper, lower

            old = upper if above else lower
            if old is not None:
                self.remove(old)

            new = Text(text, font_size=size)
            new.move_to(upper_position if above else lower_position)
            self.add(new)

            if above:
                upper = new
            else:
                lower = new

        def swap(a, b):
            if a == b:
                return

            self.play(
                ApplyMethod(squares[a].move_to, positions[b]),
                ApplyMethod(squares[b].move_to, positions[a]),
                run_time=T_SWAP,
            )

            squares.submobjects[a], squares.submobjects[b] = (
                squares.submobjects[b],
                squares.submobjects[a],
            )
            vector[a], vector[b] = vector[b], vector[a]

        fixed = set()

        def refresh(low, high):
            for k in range(len(vector)):
                square = squares[k][0]

                if k in fixed:
                    square.set_fill(GREEN, opacity=0.55)
                    square.set_stroke(GREEN, width=3)
                else:
                    square.set_fill(BLACK, opacity=0)
                    square.set_stroke(
                        WHITE if low <= k <= high else GREY,
                        width=2,
                    )

        message("Este é o vetor. Vamos organizá-lo do menor para o maior.")
        pause()

        def partition(low, high):
            refresh(low, high)

            pivot = vector[high]
            squares[high][0].set_fill(ORANGE, opacity=0.55)

            message(f"Pivô = {pivot}", above=True, size=27)
            message(f"Escolhemos {pivot} como referência nesta parte do vetor.")
            pause()

            i = low - 1
            i_label = Tex("i").set_color(BLUE)
            j_label = Tex("j").set_color(YELLOW)

            i_label.move_to(positions[low] + LEFT + DOWN * 0.85)
            j_label.move_to(positions[low] + UP * 0.85)

            self.play(
                FadeIn(i_label),
                FadeIn(j_label),
                run_time=T_FADE,
            )

            message("j analisa cada número; i marca o fim do grupo dos menores.")
            pause()

            for j in range(low, high):
                val = vector[j]
                squares[j][0].set_fill(YELLOW, opacity=0.35)

                self.play(
                    j_label.animate.move_to(positions[j] + UP * 0.85),
                    run_time=T_MOVE,
                )

                if val <= pivot:
                    message(f"{val} ≤ {pivot}", above=True, size=27)
                    i += 1

                    if i == j:
                        message(
                            f"{val} é menor ou igual a {pivot}: "
                            "já está no grupo da esquerda."
                        )
                    else:
                        message(
                            f"{val} é menor ou igual a {pivot}: "
                            f"trocamos com {vector[i]}."
                        )

                    pause()

                    self.play(
                        i_label.animate.move_to(
                            positions[i] + DOWN * 0.85
                        ),
                        run_time=T_MOVE,
                    )

                    swap(i, j)

                    # Azul significa grupo dos menores, ainda não ordenado.
                    squares[i][0].set_fill(BLUE, opacity=0.4)

                    if i != j:
                        squares[j][0].set_fill(BLACK, opacity=0)

                    # Registra o resultado da troca e a nova cor.
                    pause()

                else:
                    message(f"{val} > {pivot}", above=True, size=27)
                    message(
                        f"{val} é maior que {pivot}. "
                        "Deixamos onde está e seguimos procurando."
                    )
                    pause()
                    squares[j][0].set_fill(BLACK, opacity=0)

            position = i + 1

            message("Agora colocamos o pivô logo depois do grupo dos menores.")
            message(f"Vamos posicionar o pivô {pivot}", above=True, size=27)

            pause()

            self.play(
                FadeOut(i_label),
                FadeOut(j_label),
                run_time=T_FADE,
            )

            swap(position, high)

            fixed.add(position)
            refresh(low, high)

            message(
                f"{pivot} está na posição definitiva",
                above=True,
                size=27,
            )
            message(
                f"{pivot} está no lugar certo! Não precisará mais se mover."
            )

            pause()

            return position

        def quick_sort_rec(low, high):
            if low > high:
                return

            if low == high:
                fixed.add(low)
                refresh(low, high)

                message("Grupo com apenas um número", above=True, size=27)
                message(
                    f"O grupo com {vector[low]} tem só um número: "
                    "já está ordenado."
                )
                pause()
                return

            if low != 0 or high != len(vector) - 1:
                refresh(low, high)
                message("Vamos ordenar o trecho destacado", above=True, size=27)
                message(
                    "Repetimos a mesma ideia apenas nesta parte do vetor."
                )
                pause()

            pi = partition(low, high)
            quick_sort_rec(low, pi - 1)
            quick_sort_rec(pi + 1, high)

        quick_sort_rec(0, len(vector) - 1)

        refresh(0, len(vector) - 1)
        message("Quick Sort concluído!", above=True, size=27)
        message("Pronto! Todos os números estão em ordem crescente.")
        pause()
