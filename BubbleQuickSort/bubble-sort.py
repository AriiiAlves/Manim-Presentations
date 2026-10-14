from cmath import e
from manimlib import *

SPEED = 1.0
INTERNAL_SPEED = 1.0 / SPEED

class Bubble1(Scene):
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
        self.play(Write(title))
        self.play(FadeIn(subtitle, UP))
        self.wait(3.0 * INTERNAL_SPEED)

        # 2. Array Visualization
        vector = ["3","1","7","5","6"]
        squares = VGroup()

        for x in vector:
            square = Square(side_length=1)
            text = Text(x, font_size=24)
            text.move_to(square.get_center())
            squares.add(VGroup(square, text))

        squares.arrange(RIGHT, buff=0) # Arrange squares horizontally
        self.play(FadeOut(title), FadeOut(subtitle))
        self.play(ShowCreation(squares))

        text = Text("Este é um vetor de inteiros aleatórios. Utilizaremos Bubble Sort para ordená-lo.", font_size=24)
        text.next_to(squares, DOWN, buff=1)
        self.play(Write(text))
        self.wait(3.0 * INTERNAL_SPEED)
        self.play(FadeOut(text))

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
                        run_time=1*INTERNAL_SPEED
                    )
                    text = Text("O primeiro item é maior que o segundo. Trocamos.", font_size=24)
                    upper_text = Tex(rf"{vector[i]} > {vector[i+1]}")
                    text.next_to(squares,DOWN,buff=1)
                    upper_text.next_to(squares,UP,buff=1)
                    self.play(FadeIn(text), FadeIn(upper_text))
                    self.wait(2*INTERNAL_SPEED)
                    self.play(FadeOut(text))

                    vector[i], vector[i+1] = vector[i+1], vector[i]

                    self.play(
                        ApplyMethod(squares[i].move_to, squares[i+1].get_center()),
                        ApplyMethod(squares[i+1].move_to, squares[i].get_center()),
                        run_time=1.5*INTERNAL_SPEED
                    )
                    squares.submobjects[i], squares.submobjects[i+1] = (
                        squares.submobjects[i+1],
                        squares.submobjects[i]
                    )
                    self.play(
                        squares[i][0].animate.set_fill(GREEN, opacity=0.5),
                        squares[i+1][0].animate.set_fill(GREEN, opacity=0.5),
                        run_time=1*INTERNAL_SPEED
                    )

                    text = Text("Ordenados. Próximo.", font_size=24)
                    text.next_to(squares,DOWN,buff=1)
                    new_upper_text = Tex(rf"{vector[i]} < {vector[i+1]}")
                    new_upper_text.next_to(squares,UP,buff=1)
                    self.play(Transform(upper_text, new_upper_text))
                    self.play(FadeIn(text))
                    self.wait(3.0*INTERNAL_SPEED)
                    self.play(FadeOut(new_upper_text), FadeOut(upper_text), FadeOut(text))

                    swapFlag = True

                elif(int(vector[i]==int(vector[i+1]))):
                    self.play(
                        squares[i][0].animate.set_fill(GREEN, opacity=0.5),
                        squares[i+1][0].animate.set_fill(GREEN, opacity=0.5),
                        run_time=1*INTERNAL_SPEED
                    )

                    text = Text("Os itens são iguais. Não há troca.", font_size=24)
                    text.next_to(squares,DOWN,buff=1)
                    upper_text = Tex(rf"{vector[i]} = {vector[i+1]}")
                    upper_text.next_to(squares,UP,buff=1)
                    self.play(FadeIn(text), FadeIn(upper_text))
                    self.wait(3.0*INTERNAL_SPEED)
                    self.play(FadeOut(upper_text), FadeOut(text))
                else:
                    self.play(
                        squares[i][0].animate.set_fill(GREEN, opacity=0.5),
                        squares[i+1][0].animate.set_fill(GREEN, opacity=0.5),
                        run_time=1*INTERNAL_SPEED
                    )
                    text = Text("Os itens já estão ordenados. Não há troca.", font_size=24)
                    text.next_to(squares,DOWN,buff=1)
                    upper_text = Tex(rf"{vector[i]} < {vector[i+1]}")
                    upper_text.next_to(squares,UP,buff=1)
                    self.play(FadeIn(text), FadeIn(upper_text))
                    self.wait(3.0*INTERNAL_SPEED)
                    self.play(FadeOut(upper_text), FadeOut(text))

                self.play(
                    squares[i][0].animate.set_fill(opacity=0),
                    squares[i+1][0].animate.set_fill(opacity=0),
                    run_time=1*INTERNAL_SPEED
                )

            if(swapFlag):
                text = Text("Como no mínimo uma troca foi feita, teremos que percorrer o vetor novamente.", font_size=24)
                text.next_to(squares,DOWN,buff=1)
                self.play(FadeIn(text))
                self.wait(3.0*INTERNAL_SPEED)
                self.play(FadeOut(text))
            else:
                text = Text("Como nenhuma troca foi feita, o vetor está ordenado.", font_size=24)
                text.next_to(squares,DOWN,buff=1)
                self.play(FadeIn(text))
                self.wait(3.0*INTERNAL_SPEED)
                self.play(FadeOut(text))
