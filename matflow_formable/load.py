'`matflow_formable.load.py`'

import hickle
from matflow.scripting import get_wrapper_script

from matflow_formable import input_mapper, output_mapper, sources_mapper

@sources_mapper(task='generate_load_case', method='uniaxial', script='build_load_case')
@sources_mapper(task='generate_load_case', method='biaxial', script='build_load_case')
@sources_mapper(task='generate_load_case', method='plane_strain', script='build_load_case')
@sources_mapper(task='generate_load_case', method='planar_2D', script='build_load_case')
@sources_mapper(task='generate_load_case', method='random_2D', script='build_load_case')
@sources_mapper(task='generate_load_case', method='random_3D', script='build_load_case')
@sources_mapper(task='generate_load_case', method='cyclic_uniaxial', script='build_load_case')
@sources_mapper(task='generate_load_case', method='mixed', script='build_load_case')
def build_load_case():

    script_name = 'build_load_case.py'
    snippets = [{'name': 'build_load_case.py'}]
    outputs = ['load_case']
    out = {
        'script': {
            'content': get_wrapper_script(__package__, script_name, snippets, outputs),
            'filename': script_name,
        }
    }
    return out

@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='uniaxial')
def write_load_case_uniaxial_param_file(path, total_times, num_increments, directions,
                                        target_strain_rates, target_strains,
                                        rotations, dump_frequency):
    out = {
        'load_case_specs': [
            {
                'type': 'uniaxial',
                'total_times': total_times,
                'num_increments': num_increments,
                'directions': directions,
                'target_strain_rates': target_strain_rates,
                'target_strains': target_strains,
                'rotations': rotations,
                'dump_frequency': dump_frequency,
            }
        ]
    }
    hickle.dump(out, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='cyclic_uniaxial')
def write_load_case_uniaxial_cyclic_param_file(path, max_stresses, min_stresses,
                                               cycle_frequencies, num_increments_per_cycle,
                                               num_cycles, directions, waveforms,
                                               dump_frequency):
    out = {
        'load_case_specs': [
            {
                'type': 'cyclic_uniaxial',
                'max_stresses': max_stresses,
                'min_stresses': min_stresses,
                'cycle_frequencies': cycle_frequencies,
                'num_increments_per_cycle': num_increments_per_cycle,
                'num_cycles': num_cycles,
                'directions': directions,
                'waveforms': waveforms,
                'dump_frequency': dump_frequency,
            }
        ]
    }    
    hickle.dump(out, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='mixed')
def write_load_case_mixed_param_file(path, load_case_specs):
    hickle.dump({'load_case_specs': load_case_specs}, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='biaxial')
def write_load_case_biaxial_param_file(path, total_times, num_increments, directions,
                                       target_strain_rates, target_strains,
                                       rotations, dump_frequency):
    out = {
        'load_case_specs': [
            {
                'type': 'biaxial',
                'total_times': total_times,
                'num_increments': num_increments,
                'directions': directions,
                'target_strain_rates': target_strain_rates,
                'target_strains': target_strains,
                'rotations': rotations,
                'dump_frequency': dump_frequency,
            }
        ]
    }
    hickle.dump(out, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='plane_strain')
def write_load_case_plane_strain_param_file(path, total_times, num_increments, directions,
                                            target_strain_rates, target_strains,
                                            dump_frequency, rotations, strain_rate_modes):
    out = {
        'load_case_specs': [
            {
                'type': 'plane_strain',
                'total_times': total_times,
                'num_increments': num_increments,
                'directions': directions,
                'target_strain_rates': target_strain_rates,
                'target_strains': target_strains,
                'rotations': rotations,
                'strain_rate_modes': strain_rate_modes,
                'dump_frequency': dump_frequency,
            }
        ]
    }
    hickle.dump(out, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='planar_2D')
def write_load_case_planar_2D_param_file(path, total_times, num_increments,
                                         normal_directions, target_strain_rates,
                                         target_strains, rotations, dump_frequency):
    out = {
        'load_case_specs': [
            {
                'type': 'planar_2D',
                'total_times': total_times,
                'num_increments': num_increments,
                'normal_directions': normal_directions,
                'target_strain_rates': target_strain_rates,
                'target_strains': target_strains,
                'rotations': rotations,
                'dump_frequency': dump_frequency,
            }
        ]
    }
    hickle.dump(out, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='random_2D')
def write_load_case_random_2D_param_file(path, total_times, num_increments,
                                         normal_directions, target_strain_rates,
                                         target_strains, rotations, dump_frequency):
    out = {
        'load_case_specs': [
            {
                'type': 'random_2D',
                'total_times': total_times,
                'num_increments': num_increments,
                'normal_directions': normal_directions,
                'target_strain_rates': target_strain_rates,
                'target_strains': target_strains,
                'rotations': rotations,
                'dump_frequency': dump_frequency,
            }
        ]
    }    
    hickle.dump(out, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='random_3D')
def write_load_case_random_3D_param_file(path, total_times, num_increments,
                                         target_strains, rotation, rotation_max_angle,
                                         rotation_load_case, non_random_rotation,
                                         dump_frequency):
    out = {
        'load_case_specs': [
            {
                'type': 'random_3D',
                'total_times': total_times,
                'num_increments': num_increments,
                'target_strains': target_strains,
                'rotation': rotation,
                'rotation_max_angle': rotation_max_angle,
                'rotation_load_case': rotation_load_case,
                'non_random_rotation': non_random_rotation,
                'dump_frequency': dump_frequency,
            }
        ]
    }
    hickle.dump(out, path)


@output_mapper(output_name='load_case', task='generate_load_case', method='uniaxial')
@output_mapper(output_name='load_case', task='generate_load_case', method='biaxial')
@output_mapper(output_name='load_case', task='generate_load_case', method='plane_strain')
@output_mapper(output_name='load_case', task='generate_load_case', method='planar_2D')
@output_mapper(output_name='load_case', task='generate_load_case', method='random_2D')
@output_mapper(output_name='load_case', task='generate_load_case', method='random_3D')
@output_mapper(output_name='load_case', task='generate_load_case', method='cyclic_uniaxial')
@output_mapper(output_name='load_case', task='generate_load_case', method='mixed')
def read_load_case(path):
    return hickle.load(path)
