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

            
            
class Scene_2(MovingCameraScene):
    def construct(self):


        str_1 = Text("5x + 2y = 9")
        str_2 = Text("2x + 2y = 6")

        str_2.shift(DOWN)

        eq_group = VGroup(str_1, str_2)
        bracket = Brace(eq_group, LEFT)
        equation_0 = VGroup(str_1, str_2, bracket)
        equation_0.shift(2*UP)
        self.play(Write(equation_0))
        self.wait(5)

        str_1 = Text("5x + 2y = 9")
        str_2 = Text("x + y = 3")
        str_2.shift(DOWN)

        eq_group = VGroup(str_1, str_2)
        bracket = Brace(eq_group, LEFT)
        equation_1 = VGroup(str_1, str_2, bracket)


        self.play(Write(equation_1))
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(equation_1))
        self.wait(1)

        str_1 = Text("Вычитаем из второй строки")
        str_2 = Text("первую, разделенную на 5.")
        str_2.shift(DOWN)
        equation_2 = VGroup(str_1, str_2)
        equation_2.shift(2 * DOWN)

        self.play(Write(equation_2))
        self.wait(4)
        self.play(self.camera.frame.animate.move_to(equation_2))
        self.wait(1)

        str_1 = Text("5x + 2y = 9")
        str_2 = Text("0x + 0.6y = 1.2")
        str_2.shift(DOWN)
        eq_group = VGroup(str_1, str_2)
        bracket = Brace(eq_group, LEFT)
        equation_3 = VGroup(str_1, str_2, bracket)
        equation_3.shift(4 * DOWN)

        self.play(Write(equation_3))
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(equation_3))
        self.wait(1)

        str_1 = Text("5x + 2y = 9")
        str_2 = Text("y = 2")
        str_2.shift(DOWN)
        eq_group = VGroup(str_1, str_2)
        bracket = Brace(eq_group, LEFT)
        equation_4 = VGroup(str_1, str_2, bracket)
        equation_4.shift(6 * DOWN)

        self.play(Write(equation_4))
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(equation_4))
        self.wait(1)

        str_1 = Text("5x = 5")
        str_2 = Text("y = 2")
        str_2.shift(DOWN)
        eq_group = VGroup(str_1, str_2)
        bracket = Brace(eq_group, LEFT)
        equation_5 = VGroup(str_1, str_2, bracket)
        equation_5.shift(8 * DOWN)

        self.play(Write(equation_5))
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(equation_5))
        self.wait(1)

        str_1 = Text("x = 1")
        str_2 = Text("y = 2")
        str_2.shift(DOWN)
        eq_group = VGroup(str_1, str_2)
        bracket = Brace(eq_group, LEFT)
        equation_6 = VGroup(str_1, str_2, bracket)
        equation_6.shift(10 * DOWN)

        self.play(Write(equation_6))
        self.wait(2)
        self.play(self.camera.frame.animate.move_to(equation_6))
        self.wait(1)



        vector = IntegerMatrix([[1], [2]], left_bracket="(", right_bracket=")")
        vector.shift(13 * DOWN)
        self.play(Write(vector))
        self.wait(5)
