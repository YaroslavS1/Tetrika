def appearance(intervals):
    pupil_sessions = list(zip(intervals["pupil"][::2], intervals["pupil"][1::2]))
    tutor_sessions = list(zip(intervals["tutor"][::2], intervals["tutor"][1::2]))

    result = 0

    for second_lesson in range(intervals["lesson"][0], intervals["lesson"][1] + 1):
        for p_session in pupil_sessions:
            for t_session in tutor_sessions:
                if second_lesson in range(*p_session) and second_lesson in range(
                    *t_session
                ):
                    result += 1

    return result


if __name__ == "__main__":
    print(
        appearance(
            {
                "lesson": [1594663200, 1594666800],
                "pupil": [
                    1594663340,
                    1594663389,
                    1594663390,
                    1594663395,
                    1594663396,
                    1594666472,
                ],
                "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
            }
        )
    )
