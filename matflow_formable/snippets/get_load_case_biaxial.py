from formable import load_cases
from matflow.scripting import main_func


@main_func
def get_load_case_biaxial(total_times, num_increments, directions, target_strain_rates,
                          target_strains, rotations, dump_frequency):

    if target_strains is None:
        target_strains = [None] * len(total_times)
    elif target_strain_rates is None:
        target_strain_rates = [None] * len(total_times)

    if dump_frequency is None:
        dump_frequency = [1] * len(total_times)

    if rotations is None:
        rotations = [None] * len(total_times)

    all_load_cases = []
    for t, n, eps_dot, eps, d, rot, freq in zip(
        total_times,
        num_increments,
        target_strain_rates,
        target_strains,
        directions,
        rotations,
        dump_frequency,
    ):
        all_load_cases.append(
            load_cases.get_load_case_biaxial(
                total_time=t,
                num_increments=n,
                direction=d,
                target_strain_rate=eps_dot,
                target_strain=eps,
                rotation=rot,
                dump_frequency=freq,
            )
        )
    load_case = all_load_cases
    return load_case
