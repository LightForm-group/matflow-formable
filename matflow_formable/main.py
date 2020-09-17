'`matflow_formable.main.py`'

import hickle
from matflow.scripting import get_wrapper_script

from matflow_formable import input_mapper, output_mapper, sources_mapper


@input_mapper(input_file='inputs.hdf5', task='fit_yield_function', method='least_squares')
def write_fit_yield_function_param_file(path, yield_function_name, yield_point_criteria,
                                        uniaxial_response, multiaxial_responses,
                                        fixed_parameters):
    kwargs = {
        'yield_function_name': yield_function_name,
        'yield_point_criteria': yield_point_criteria,
        'uniaxial_response': uniaxial_response,
        'multiaxial_responses': multiaxial_responses,
        'fixed_parameters': fixed_parameters,
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
