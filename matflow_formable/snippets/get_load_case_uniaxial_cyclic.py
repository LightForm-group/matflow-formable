from formable import load_cases
from matflow.scripting import main_func


@main_func
def get_load_case_uniaxial_cyclic(max_stresses, min_stresses, cycle_frequencies,
                               num_increments_per_cycle, num_cycles, directions, 
                               waveforms):

    all_load_cases = []
    for max_stress, min_stress, cycle_freq, num_incs, num_cyc, d, w in zip(
        max_stresses,
        min_stresses,
        cycle_frequencies,
        num_increments_per_cycle,
        num_cycles,
        directions,
        waveforms,
    ):
        all_load_cases.extend(
            load_cases.get_load_case_uniaxial_cyclic(
                max_stress=max_stress,
                min_stress=min_stress,
                cycle_frequency=cycle_freq,
                num_increments_per_cycle=num_incs,
                num_cycles=num_cyc,
                direction=d,
                waveform=w,
            )
        )

    load_case = all_load_cases
    return load_case
