from formable import load_cases
from matflow.scripting import main_func


@main_func
def get_load_case_plane_strain(total_times, num_increments, directions,
                               target_strain_rates, target_strains, rotations,
                               dump_frequency, strain_rate_modes):

    if target_strains is None:
        target_strains = [None] * len(total_times)
    elif target_strain_rates is None:
        target_strain_rates = [None] * len(total_times)

    if strain_rate_modes is None:
        strain_rate_modes = [None] * len(total_times)

    if dump_frequency is None:
        dump_frequency = [1] * len(total_times)

    if rotations is None:
        rotations = [None] * len(total_times)

    all_load_cases = []
    for t, n, eps_dot, eps, d, rot, freq, mode in zip(
        total_times,
        num_increments,
        target_strain_rates,
        target_strains,
        directions,
        rotations,
        dump_frequency,
        strain_rate_modes,
    ):
        all_load_cases.append(
            load_cases.get_load_case_plane_strain(
                total_time=t,
                num_increments=n,
                direction=d,
                target_strain_rate=eps_dot,
                target_strain=eps,
                rotation=rot,
                dump_frequency=freq,
                strain_rate_mode=mode,
            )
        )

    load_case = all_load_cases
    return load_case
