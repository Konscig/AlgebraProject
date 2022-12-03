from manim import *
from random import randint


class Scene_1(Scene):
    def construct(self):

        T = 4
        matrix_list = []

        for k in range(T):
            N = randint(2, 3)
            M = randint(2, 3)
            matrix_list.append([])
            for i in range(N):
                matrix_list[k].append([])
                for j in range(M):
                    matrix_list[k][i].append(randint(-9, 9))

            matrix_list[k] = VGroup(IntegerMatrix(matrix_list[k], include_background_rectangle=True))

        matrix_list[0].to_edge(UP)
        matrix_list[0].to_edge(LEFT)

        matrix_list[1].to_edge(DOWN)
        matrix_list[1].to_edge(RIGHT)

        matrix_list[2].to_edge(UP)
        matrix_list[2].to_edge(RIGHT)

        matrix_list[3].to_edge(DOWN)
        matrix_list[3].to_edge(LEFT)



        for k in range(T):
            self.play(FadeIn(matrix_list[k]))
            self.wait(1)

        for k in range(T):
            self.play(FadeOut(matrix_list[k]))
            self.wait(0.5)
