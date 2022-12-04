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
 

class Scene_3(Scene):
    def construct(self):
        ellipse = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        )
        ellipse.shift(2.5*RIGHT)

        str_1 = Text("x + y + 4z = 52")
        str_2 = Text("x = 3y")

        str_2.shift(DOWN)

        eq_group = VGroup(str_1, str_2)
        bracket = Brace(eq_group, LEFT)
        equation_0 = VGroup(str_1, str_2, bracket)
        equation_0.shift(2.5 * LEFT)
        equation_0.shift(0.5 * UP)



        vector0 = Matrix([["39 - 3z"], ["13 - z"], ["z"]], left_bracket="(", right_bracket=")")
        vector0.shift(2.5*RIGHT)
        self.add(equation_0, ellipse, vector0)


        self.wait(5)


        vector1 = Matrix([["39"], ["13"], ["0"]], left_bracket="(", right_bracket=")")
        vector1.shift(2.5 * RIGHT)
        self.play(Transform(vector0, vector1))

        self.play(vector0.animate.shift(RIGHT), ellipse.animate.shift(RIGHT).scale(1.5))

        vector2 = Matrix([["36"], ["12"], ["1"]], left_bracket="(", right_bracket=")")
        vector2.shift(1.5 * RIGHT)
        self.play(FadeIn(vector2))

        vector3 = Matrix([["33"], ["11"], ["2"]], left_bracket="(", right_bracket=")")
        vector3.shift(5.5 * RIGHT)
        self.play(FadeIn(vector3))


        self.wait(5)

        vector4 = Matrix([["39 - 3z"], ["13 - z"], ["z"]], left_bracket="(", right_bracket=")")
        vector4.shift(2.5 * RIGHT)
        self.add(equation_0, ellipse, vector0)

        self.play(FadeOut(vector2), FadeOut(vector3))
        self.play(vector0.animate.shift(LEFT), ellipse.animate.shift(LEFT).scale(2/3))
        self.play(Transform(vector0, vector4))

class Scene_4(Scene):
    def construct(self):

        str_1 = Text("5x + 2y = 9")
        str_2 = Text("2x + 2y = 6")

        str_2.shift(DOWN)

        eq_group_0 = VGroup(str_1, str_2)
        eq_group_0.shift(0.5*LEFT)
        bracket_0 = Brace(eq_group_0, LEFT)


        str_3 = Text("x = 1")

        str_4 = Text("y = 2")
        str_4.shift(DOWN)
        eq_group_1 = VGroup(str_3, str_4)
        eq_group_1.next_to(eq_group_0)
        eq_group_1.shift(RIGHT)
        bracket_1 = Brace(eq_group_1, LEFT)

        equation_0 = VGroup(str_1, str_2, bracket_0, str_3, str_4, bracket_1)
        equation_0.shift(2 * UP)
        equation_0.shift(LEFT)

        self.play(Write(equation_0))

        mtx = IntegerMatrix([[5, 2], [2, 2]],  left_bracket="(", right_bracket=")")
        mtx.shift(2*LEFT)
        mtx.shift(DOWN)
        radikal = IntegerMatrix([[1], [2]], left_bracket="(", right_bracket=")")
        radikal.next_to(mtx)
        txt = Text(" = ")
        txt.next_to(radikal)
        ans = IntegerMatrix([[9], [6]], left_bracket="(", right_bracket=")")
        ans.next_to(txt)

        equation_1 = VGroup(mtx, radikal, txt, ans)

        self.play(Write(equation_1))

        self.wait(10)

        self.play(Unwrite(equation_0))
        self.play(Unwrite(equation_1))

        self.wait(3)
