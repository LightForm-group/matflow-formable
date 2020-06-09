'`matflow_formable.main.py`'

from matflow_formable import (
    input_mapper,
    output_mapper,
    cli_format_mapper,
    register_output_file,
    func_mapper,
    software_versions,
)

from formable import __version__ as formable_version
from formable.load_response import LoadResponse, LoadResponseSet


@func_mapper(task='fit_yield_function', method='formable')
def fit_yield_function(yield_function_name, yield_point_criteria, uniaxial_response,
                       multiaxial_responses):

    # Generate LoadResponse objects:
    uni_resp = LoadResponse(
        true_stress=uniaxial_response['vol_avg_stress'],
        equivalent_plastic_strain=uniaxial_response['vol_avg_equivalent_plastic_strain'],
    )
    multi_resp = []
    for resp_dat in multiaxial_responses:
        multi_resp.append(
            LoadResponse(
                true_stress=resp_dat['vol_avg_stress'],
                equivalent_plastic_strain=resp_dat['vol_avg_equivalent_plastic_strain'],
            )
        )
    response_set = LoadResponseSet(multi_resp)
    response_set.calculate_yield_stresses(yield_point_criteria)
    response_set.fit_yield_function(yield_function_name, uniaxial_response=uni_resp)
    out = {
        'fitted_yield_functions': [
            {
                'name': yield_function_name,
                **i['yield_function'].get_parameters()
            }
            for i in response_set.yield_functions
        ]
    }

    return out


@software_versions()
def get_versions():
    return {'formable (Python)': {'version': formable_version}}
