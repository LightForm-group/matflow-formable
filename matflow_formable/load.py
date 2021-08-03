'`matflow_formable.load.py`'

import hickle
from matflow.scripting import get_wrapper_script

from matflow_formable import input_mapper, output_mapper, sources_mapper


@sources_mapper(task='generate_load_case', method='uniaxial',
                script='get_load_case_uniaxial')
def get_load_case_uniaxial():

    script_name = 'get_load_case_uniaxial.py'
    snippets = [{'name': 'get_load_case_uniaxial.py'}]
    outputs = ['load_case']
    out = {
        'script': {
            'content': get_wrapper_script(__package__, script_name, snippets, outputs),
            'filename': script_name,
        }
    }
    return out


@sources_mapper(task='generate_load_case', method='biaxial',
                script='get_load_case_biaxial')
def get_load_case_biaxial():

    script_name = 'get_load_case_biaxial.py'
    snippets = [{'name': 'get_load_case_biaxial.py'}]
    outputs = ['load_case']
    out = {
        'script': {
            'content': get_wrapper_script(__package__, script_name, snippets, outputs),
            'filename': script_name,
        }
    }
    return out


@sources_mapper(task='generate_load_case', method='plane_strain',
                script='get_load_case_plane_strain')
def get_load_case_plane_strain():

    script_name = 'get_load_case_plane_strain.py'
    snippets = [{'name': 'get_load_case_plane_strain.py'}]
    outputs = ['load_case']
    out = {
        'script': {
            'content': get_wrapper_script(__package__, script_name, snippets, outputs),
            'filename': script_name,
        }
    }
    return out

@sources_mapper(task='generate_load_case', method='planar_2D',
                script='get_load_case_planar_2D')
def get_load_case_planar_2D():

    script_name = 'get_load_case_planar_2D.py'
    snippets = [{'name': 'get_load_case_planar_2D.py'}]
    outputs = ['load_case']
    out = {
        'script': {
            'content': get_wrapper_script(__package__, script_name, snippets, outputs),
            'filename': script_name,
        }
    }
    return out


@sources_mapper(task='generate_load_case', method='random_2D',
                script='get_load_case_random_2D')
def get_load_case_random_2D():

    script_name = 'get_load_case_random_2D.py'
    snippets = [{'name': 'get_load_case_random_2D.py'}]
    outputs = ['load_case']
    out = {
        'script': {
            'content': get_wrapper_script(__package__, script_name, snippets, outputs),
            'filename': script_name,
        }
    }
    return out


@sources_mapper(task='generate_load_case', method='random_3D',
                script='get_load_case_random_3D')
def get_load_case_random_3D():

    script_name = 'get_load_case_random_3D.py'
    snippets = [{'name': 'get_load_case_random_3D.py'}]
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
    kwargs = {
        'total_times': total_times,
        'num_increments': num_increments,
        'directions': directions,
        'target_strain_rates': target_strain_rates,
        'target_strains': target_strains,
        'rotations': rotations,
        'dump_frequency': dump_frequency,
    }
    hickle.dump(kwargs, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='biaxial')
def write_load_case_biaxial_param_file(path, total_times, num_increments, directions,
                                       target_strain_rates, target_strains,
                                       rotations, dump_frequency):
    kwargs = {
        'total_times': total_times,
        'num_increments': num_increments,
        'directions': directions,
        'target_strain_rates': target_strain_rates,
        'target_strains': target_strains,
        'rotations': rotations,
        'dump_frequency': dump_frequency,
    }
    hickle.dump(kwargs, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='plane_strain')
def write_load_case_plane_strain_param_file(path, total_times, num_increments, directions,
                                            target_strain_rates, target_strains,
                                            dump_frequency, rotations, strain_rate_modes):
    kwargs = {
        'total_times': total_times,
        'num_increments': num_increments,
        'directions': directions,
        'target_strain_rates': target_strain_rates,
        'target_strains': target_strains,
        'rotations': rotations,
        'strain_rate_modes': strain_rate_modes,
        'dump_frequency': dump_frequency,
    }
    hickle.dump(kwargs, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='planar_2D')
def write_load_case_planar_2D_param_file(path, total_times, num_increments,
                                         normal_directions, target_strain_rates,
                                         target_strains, rotations, dump_frequency):
    kwargs = {
        'total_times': total_times,
        'num_increments': num_increments,
        'normal_directions': normal_directions,
        'target_strain_rates': target_strain_rates,
        'target_strains': target_strains,
        'rotations': rotations,
        'dump_frequency': dump_frequency,
    }
    hickle.dump(kwargs, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='random_2D')
def write_load_case_random_2D_param_file(path, total_times, num_increments,
                                         normal_directions, target_strain_rates,
                                         target_strains, rotations, dump_frequency):
    kwargs = {
        'total_times': total_times,
        'num_increments': num_increments,
        'normal_directions': normal_directions,
        'target_strain_rates': target_strain_rates,
        'target_strains': target_strains,
        'rotations': rotations,
        'dump_frequency': dump_frequency,
    }
    hickle.dump(kwargs, path)


@input_mapper(input_file='inputs.hdf5', task='generate_load_case', method='random_3D')
def write_load_case_random_3D_param_file(path, total_times, num_increments,
                                         target_strains, rotation, rotation_max_angle,
                                         rotation_load_case, non_random_rotation,
                                         dump_frequency):
    kwargs = {
        'total_times': total_times,
        'num_increments': num_increments,
        'target_strains': target_strains,
        'rotation': rotation,
        'rotation_max_angle': rotation_max_angle,
        'rotation_load_case': rotation_load_case,
        'non_random_rotation': non_random_rotation,
        'dump_frequency': dump_frequency,
    }
    hickle.dump(kwargs, path)


@output_mapper(output_name='load_case', task='generate_load_case', method='uniaxial')
@output_mapper(output_name='load_case', task='generate_load_case', method='biaxial')
@output_mapper(output_name='load_case', task='generate_load_case', method='plane_strain')
@output_mapper(output_name='load_case', task='generate_load_case', method='planar_2D')
@output_mapper(output_name='load_case', task='generate_load_case', method='random_2D')
@output_mapper(output_name='load_case', task='generate_load_case', method='random_3D')
def read_load_case(path):
    return hickle.load(path)
