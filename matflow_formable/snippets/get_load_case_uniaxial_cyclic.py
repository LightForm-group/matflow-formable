from formable import load_cases
from matflow.scripting import main_func


@main_func
def get_load_case_uniaxial_cyclic(max_stresses, min_stresses, cycle_frequencies,
                               num_increments_per_cycle, num_cycles, directions, 
                               waveforms, dump_frequency):

    if waveforms is None:
        waveforms = ['sine'] * len(max_stresses)

    if dump_frequency is None:
        dump_frequency = [1] * len(max_stresses)

    all_load_cases = []
    for max_stress, min_stress, cycle_freq, num_incs, num_cyc, d, w, f in zip(
        max_stresses,
        min_stresses,
        cycle_frequencies,
        num_increments_per_cycle,
        num_cycles,
        directions,
        waveforms,
        dump_frequency,
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
                dump_frequency=f,
            )
        )

    load_case = all_load_cases
    return load_case
