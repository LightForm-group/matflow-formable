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


@software_versions()
def get_versions():
    return {'formable (Python)': {'version': formable_version}}
