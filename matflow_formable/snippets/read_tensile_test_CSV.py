from formable.tensile_test import TensileTest
from formable.utils import read_non_uniform_csv
from matflow.scripting import main_func


@main_func
def read_tensile_test_CSV(CSV_file_path, CSV_arguments, eng_stress_col_index,
                          eng_strain_col_index, true_stress_col_index,
                          true_strain_col_index, stress_units, plastic_range):

    _, CSV_data = read_non_uniform_csv(
        CSV_file_path,
        delimiter=CSV_arguments.get('delimiter'),
        skip_rows=CSV_arguments.get('skip_rows'),
        header_row=CSV_arguments.get('header_row'),
    )

    eng_strain, eng_stress = None, None
    true_strain, true_stress = None, None

    if eng_strain_col_index is not None:
        eng_strain = CSV_data[:, eng_strain_col_index]
        eng_stress = CSV_data[:, eng_stress_col_index]
        stress = eng_stress

    elif true_strain_col_index is not None:
        true_strain = CSV_data[:, true_strain_col_index]
        true_stress = CSV_data[:, true_stress_col_index]
        stress = true_stress

    if stress_units.strip().upper() == 'MPA':
        stress *= 1e6
    elif stress_units.strip().upper() == 'GPA':
        stress *= 1e9

    tensile_test_obj = TensileTest(
        eng_stress=eng_stress,
        eng_strain=eng_strain,
        true_stress=true_stress,
        true_strain=true_strain,
        plastic_range=plastic_range,
    )

    tensile_test = tensile_test_obj.to_dict()

    return tensile_test
