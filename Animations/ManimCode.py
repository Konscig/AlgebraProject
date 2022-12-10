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

        
        
class Scene_5(MovingCameraScene):
    def construct(self):
        self.wait(1)
        str_1 = Text("5x + 2y = 9")
        str_2 = Text("2x + 2y = 6")
        str_2.shift(DOWN)
        eq_group = VGroup(str_1, str_2)
        bracket = Brace(eq_group, LEFT)
        equation_0 = VGroup(str_1, str_2, bracket)
        equation_0.shift(2 * UP)

        mtx0 = IntegerMatrix([[5, 2, 9], [2, 2, 6]], left_bracket="(", right_bracket=")",).shift(DOWN)
        line = Line(start=(0, 0, 0), end=(0, -1.4, 0)).next_to(mtx0).shift(1.5 * LEFT)
        matrix0 = VGroup(mtx0, line)

        self.play(Write(equation_0), Write(matrix0, run_time=2))

        self.wait(1)
        q2 = SurroundingRectangle(mtx0.get_rows()[0])
        q1 = SurroundingRectangle(str_1)
        self.play(Create(q1), Create(q2))
        self.wait(1)
        self.play(q1.animate.move_to(str_2), q2.animate.move_to(mtx0.get_rows()[1]))
        self.wait(1)
        self.play(Uncreate(q1), Uncreate(q2))
        self.wait(1)

        self.play(self.camera.frame.animate.shift(DOWN))

        self.play(Unwrite(equation_0, run_time=0.75))

        q3 = ArrowCircleTip().next_to(mtx0.get_rows()[0])
        q3.scale(1.4)
        q3.shift(0.4*RIGHT)

        q4 = Text("/5").move_to(q3)
        q4.scale(0.5)


        self.play(Create(q3), Create(q4))
        self.wait(1)
        mtx1 = Matrix([[1, 2/5, 9/5], [2, 2, 6]], left_bracket="(", right_bracket=")", ).shift(DOWN)
        self.play(Transform(mtx0, mtx1))

        self.play(FadeOut(q3), FadeOut(q4))


        q3 = ArrowCircleTip(color=GREEN).next_to(mtx0.get_rows()[0])
        q3.scale(1.4)
        q3.shift(0.4 * RIGHT)

        q4 = Text("-2").move_to(q3).scale(0.5)
        self.play(Create(q3), Create(q4))


        angle = ValueTracker()
        arc = always_redraw(lambda:
                            Arc(
                                start_angle=PI/2,
                                angle=angle.get_value(),
                                stroke_width=2,
                                radius=0.5,
                            ).next_to(matrix0).add_tip(tip_length=0.15, tip_width=0.1).shift(0.3*RIGHT)
                            )


        self.add(arc)
        self.play(angle.animate.set_value(-PI))
        self.wait(1)
        mtx1 = Matrix([[1, 0.4, 1.8], [0, 0.2, 0.4]], left_bracket="(", right_bracket=")", ).shift(DOWN)
        self.play(Transform(mtx0, mtx1))


        self.play(FadeOut(q3), FadeOut(q4), FadeOut(arc))


        q3 = ArrowCircleTip().next_to(mtx0.get_rows()[1])
        q3.scale(1.4)
        q3.shift(0.4 * RIGHT)

        q4 = Text("*5").move_to(q3)
        q4.scale(0.5)

        self.play(Create(q3), Create(q4))

        self.wait(1)
        mtx1 = Matrix([[1, 2 / 5, 9 / 5], [0, 1, 2]], left_bracket="(", right_bracket=")", ).shift(DOWN)
        self.play(Transform(mtx0, mtx1))
        self.wait(1)

        self.play(FadeOut(q3), FadeOut(q4))


        str_1 = Text("x + 0.4y = 1.8")
        str_2 = Text("y = 2")
        str_2.shift(DOWN)
        eq_group = VGroup(str_1, str_2)
        bracket = Brace(eq_group, LEFT)
        equation_0 = VGroup(str_1, str_2, bracket)
        equation_0.shift(2 * UP)


        self.play(self.camera.frame.animate.shift(UP))
        self.play(Write(equation_0))

        self.wait(3)
        self.play(Unwrite(equation_0), Unwrite(matrix0, run_time=0.5))

class Scene_6(ThreeDScene):

    def create_matrix(self, np_matrix):
        basis_i_color = GREEN
        basis_j_color = RED
        basis_k_color = GOLD

        m = Matrix(np_matrix)

        m.scale(0.5)
        m.set_column_colors(basis_i_color, basis_j_color, basis_k_color)

        m.to_corner(UP + LEFT)

        return m

    def construct(self):

        basis_i_color = GREEN
        basis_j_color = RED
        basis_k_color = GOLD

        M = np.array([
            [2, 2, -1],
            [-2, 1, 2],
            [3, 1, -0]
        ])

        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)


        Rang = Text("Rang = 3")

        Rang.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(Rang)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color=basis_i_color)
        j_vec = Vector(np.array([0, 1, 0]), color=basis_j_color)
        k_vec = Vector(np.array([0, 0, 1]), color=basis_k_color)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=basis_j_color)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=basis_k_color)

        self.play(
            Create(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(Rang)
        )

        self.wait()

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)




        Rang_new = Text("Rang = 2")
        Rang_new.to_corner(UP + RIGHT)

        M = np.array([
            [2, 2, -1],
            [-2, 1, 2],
            [-1, 0.5, 1]
        ])

        self.remove(matrix)
        matrix = self.create_matrix(M)
        self.add_fixed_in_frame_mobjects(matrix)


        matrix_anim = ApplyMatrix(M, cube)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=basis_j_color)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=basis_k_color)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(Rang, Rang_new)
        )

        self.wait()

        self.wait(7)




        Rang_new = Text("Rang = 1")
        Rang_new.to_corner(UP + RIGHT)

        M = np.array([
            [1, -0.5, -1],
            [-2, 1, 2],
            [-1, 0.5, 1]
        ])

        self.remove(matrix)
        matrix = self.create_matrix(M)
        self.add_fixed_in_frame_mobjects(matrix)

        matrix_anim = ApplyMatrix(M, cube)

        i_vec_new = Vector(M @ np.array([1, 0, 0]), color=basis_i_color)
        j_vec_new = Vector(M @ np.array([0, 1, 0]), color=basis_j_color)
        k_vec_new = Vector(M @ np.array([0, 0, 1]), color=basis_k_color)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(Rang, Rang_new)
        )

        self.wait()

        self.wait(7)

    
class Scene_7(Scene):
    def construct(self):
        self.wait(1)
        mtx0 = IntegerMatrix([[5, 2, 9], [2, 2, 6], [4, 5, 6]], left_bracket="(", right_bracket=")", ).shift(UP)
        self.play(Write(mtx0))
        line0 = Line(start=(0, 0, 0), end=(0, 2, 0))
        line1 = Line(start=(-1.5, 0.2, 0), end=(1.5, 0.2, 0))

        self.play(Create(line0), Create(line1))

        txt0 = Text("M32 = ").shift(DOWN + 2*LEFT)
        mtx1 = IntegerMatrix([[5, 9], [4, 6]], left_bracket="|", right_bracket="|", ).next_to(txt0)
        txt1 = Text(" = -6").next_to(mtx1)

        self.play(Write(txt0))
        self.play(Write(mtx1))
        self.play(Write(txt1))

        self.wait(3)

        self.play(FadeOut(txt0), FadeOut(mtx1), FadeOut(txt1))

        self.play(line0.animate.shift(1.3*RIGHT), line1.animate.shift(1.55*UP))
        self.wait(1)

        txt0 = Text("M13 = ").shift(DOWN + 2 * LEFT)
        mtx1 = IntegerMatrix([[2, 2], [4, 5]], left_bracket="|", right_bracket="|", ).next_to(txt0)
        txt1 = Text(" = 2").next_to(mtx1)

        self.play(Write(txt0))
        self.play(Write(mtx1))
        self.play(Write(txt1))
        self.wait(3)

        self.play(FadeOut(txt0), FadeOut(mtx1), FadeOut(txt1))

        self.play(line0.animate.shift(2.6 * LEFT), line1.animate.shift(1.55 * DOWN))
        self.wait(1)

        txt0 = Text("M31 = ").shift(DOWN + 2 * LEFT)
        mtx1 = IntegerMatrix([[2, 9], [4, 6]], left_bracket="|", right_bracket="|", ).next_to(txt0)
        txt1 = Text(" = -6").next_to(mtx1)

        self.play(Write(txt0))
        self.play(Write(mtx1))
        self.play(Write(txt1))
        self.wait(3)

        self.play(FadeOut(txt0), FadeOut(mtx1), FadeOut(txt1), Unwrite(mtx0), Uncreate(line0), Uncreate(line1))

