from formable import load_cases
from matflow.scripting import main_func


@main_func
def get_load_case_random_3D(total_times, num_increments, target_strains, rotation,
                            rotation_max_angle, rotation_load_case, non_random_rotation,
                            dump_frequency):

    if non_random_rotation is None:
        non_random_rotation = [None] * len(total_times)

    if dump_frequency is None:
        dump_frequency = [1] * len(total_times)

    all_load_cases = []
    for t, n, eps, rot, freq in zip(
        total_times,
        num_increments,
        target_strains,
        non_random_rotation,
        dump_frequency
    ):
        all_load_cases.append(
            load_cases.get_load_case_random_3D(
                total_time=t,
                num_increments=n,
                target_strain=eps,
                rotation=rotation,
                rotation_max_angle=rotation_max_angle,
                rotation_load_case=rotation_load_case,
                non_random_rotation=rot,
                dump_frequency=freq,
            )
        )

    load_case = all_load_cases
    return load_case
