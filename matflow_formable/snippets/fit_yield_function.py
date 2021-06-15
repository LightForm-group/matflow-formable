from formable import LoadResponse, LoadResponseSet
from matflow.scripting import main_func


@main_func
def fit_yield_function(yield_function_name, yield_point_criteria, uniaxial_response,
                       multiaxial_responses, fixed_parameters, initial_parameters,
                       opt_parameters):
    """
    Parameters
    ----------
    yield_function_name : str
    yield_point_criteria : dict
    uniaxial_response :  dict
    multiaxial_responses : list of dict
    fixed_parameters : dict
    initial_parameters: dict
    opt_parameters : dict
        Optimisation parameters. Dict with any of the keys:
            default_bounds : list of length two, optional
                The bounds applied to all non-fixed yield function parameters by
                default.
            bounds : dict, optional
                Dict of bounds for individual named parameters. These bounds take
                precedence over `default_bounds`.
            **kwargs : dict
                Other parameters to be passed to the SciPy least_squares function.    

    """

    # Generate LoadResponse objects:
    uni_resp = LoadResponse(
        true_stress=uniaxial_response['volume_data']['vol_avg_stress']['data'],
        equivalent_plastic_strain=uniaxial_response['volume_data']['vol_avg_equivalent_plastic_strain']['data'],
    )
    multi_resp = []
    for resp_dat in multiaxial_responses:
        multi_resp.append(
            LoadResponse(
                true_stress=resp_dat['volume_data']['vol_avg_stress']['data'],
                equivalent_plastic_strain=resp_dat['volume_data']['vol_avg_equivalent_plastic_strain']['data'],
            )
        )
    response_set = LoadResponseSet(multi_resp)
    response_set.calculate_yield_stresses(yield_point_criteria)
    response_set.fit_yield_function(
        yield_function_name,
        uniaxial_response=uni_resp,
        initial_params=initial_parameters,
        opt_params=opt_parameters,
        **(fixed_parameters or {}),
    )
    fitted_yield_functions = response_set.to_dict()

    return fitted_yield_functions
