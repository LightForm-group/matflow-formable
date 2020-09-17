from formable import LoadResponse, LoadResponseSet
from matflow.scripting import main_func


@main_func
def fit_yield_function(yield_function_name, yield_point_criteria, uniaxial_response,
                       multiaxial_responses, fixed_parameters):

    # Generate LoadResponse objects:
    uni_resp = LoadResponse(
        true_stress=uniaxial_response['vol_avg_stress']['data'],
        equivalent_plastic_strain=uniaxial_response['vol_avg_equivalent_plastic_strain']['data'],
    )
    multi_resp = []
    for resp_dat in multiaxial_responses:
        multi_resp.append(
            LoadResponse(
                true_stress=resp_dat['vol_avg_stress']['data'],
                equivalent_plastic_strain=resp_dat['vol_avg_equivalent_plastic_strain']['data'],
            )
        )
    response_set = LoadResponseSet(multi_resp)
    response_set.calculate_yield_stresses(yield_point_criteria)
    response_set.fit_yield_function(
        yield_function_name,
        uniaxial_response=uni_resp,
        **(fixed_parameters or {}),
    )
    fitted_yield_functions = [
        {
            'name': yield_function_name,
            **i['yield_function'].get_parameters()
        }
        for i in response_set.yield_functions
    ]

    return fitted_yield_functions
