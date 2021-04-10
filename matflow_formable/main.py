'`matflow_formable.main.py`'

import hickle
from matflow.scripting import get_wrapper_script

from matflow_formable import input_mapper, output_mapper, sources_mapper


@input_mapper(input_file='inputs.hdf5', task='fit_yield_function', method='least_squares')
def write_fit_yield_function_param_file(path, yield_function_name, yield_point_criteria,
                                        uniaxial_response, multiaxial_responses,
                                        fixed_parameters, initial_parameters,
                                        opt_parameters):
    kwargs = {
        'yield_function_name': yield_function_name,
        'yield_point_criteria': yield_point_criteria,
        'uniaxial_response': uniaxial_response,
        'multiaxial_responses': multiaxial_responses,
        'fixed_parameters': fixed_parameters,
        'initial_parameters': initial_parameters,
        'opt_parameters': opt_parameters,
    }
    hickle.dump(kwargs, path)


@output_mapper(
    output_name='fitted_yield_functions',
    task='fit_yield_function',
    method='least_squares',
)
def read_fitted_yield_functions(path):
    return hickle.load(path)


@sources_mapper(
    task='fit_yield_function',
    method='least_squares',
    script='fit_yield_function',
)
def fit_yield_function():

    script_name = 'fit_yield_function.py'
    snippets = [{'name': 'fit_yield_function.py'}]
    outputs = ['fitted_yield_functions']
    out = {
        'script': {
            'content': get_wrapper_script(__package__, script_name, snippets, outputs),
            'filename': script_name,
        }
    }
    return out


@input_mapper(input_file='inputs.hdf5', task='get_tensile_test', method='from_CSV')
def write_get_tensile_test_param_file(path, CSV_file_path, CSV_arguments,
                                      eng_stress_col_index, eng_strain_col_index,
                                      true_stress_col_index, true_strain_col_index,
                                      stress_units):
    kwargs = {
        'CSV_file_path': CSV_file_path,
        'CSV_arguments': CSV_arguments,
        'eng_stress_col_index': eng_stress_col_index,
        'eng_strain_col_index': eng_strain_col_index,
        'true_stress_col_index': true_stress_col_index,
        'true_strain_col_index': true_strain_col_index,
        'stress_units': stress_units,
    }
    hickle.dump(kwargs, path)


@output_mapper(
    output_name='tensile_test',
    task='get_tensile_test',
    method='from_CSV',
)
def read_loaded_tensile_tests(path):
    return hickle.load(path)


@sources_mapper(
    task='get_tensile_test',
    method='from_CSV',
    script='get_tensile_test',
)
def get_tensile_test():

    script_name = 'get_tensile_test.py'
    snippets = [{'name': 'read_tensile_test_CSV.py'}]
    outputs = ['tensile_test']
    out = {
        'script': {
            'content': get_wrapper_script(__package__, script_name, snippets, outputs),
            'filename': script_name,
        }
    }
    return out


@input_mapper(
    input_file='inputs.hdf5',
    task='optimise_single_crystal_parameters',
    method='levenberg_marquardt'
)
def write_opt_SC_params_LM_file(path, single_crystal_parameters,
                                single_crystal_parameter_perturbations,
                                perturbed_volume_element_responses,
                                experimental_tensile_test, initial_damping):
    kwargs = {
        'single_crystal_parameters': single_crystal_parameters,
        'single_crystal_parameter_perturbations': single_crystal_parameter_perturbations,
        'perturbed_volume_element_responses': perturbed_volume_element_responses,
        'experimental_tensile_test': experimental_tensile_test,
        'initial_damping': initial_damping,
    }
    hickle.dump(kwargs, path)


@output_mapper(
    output_name='single_crystal_parameters',
    task='optimise_single_crystal_parameters',
    method='levenberg_marquardt',
)
def read_optimised_SC_params_LM_1(path):
    return hickle.load(path)['single_crystal_parameters']


@output_mapper(
    output_name='levenberg_marquardt_fitter',
    task='optimise_single_crystal_parameters',
    method='levenberg_marquardt',
)
def read_optimised_SC_params_LM_2(path):
    return hickle.load(path)['levenberg_marquardt_fitter']


@sources_mapper(
    task='optimise_single_crystal_parameters',
    method='levenberg_marquardt',
    script='optimise_SC_parameters_LM',
)
def optimise_single_crystal_parameters_LM():

    script_name = 'optimise_SC_parameters_LM.py'
    snippets = [{'name': 'optimise_SC_parameters_LM.py'}]
    outputs = ['outputs']
    out = {
        'script': {
            'content': get_wrapper_script(__package__, script_name, snippets, outputs),
            'filename': script_name,
        }
    }
    return out
