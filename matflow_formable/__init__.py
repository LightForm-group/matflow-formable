'`matflow_formable.__init__.py`'

from functools import partial

from matflow_formable._version import __version__

from matflow.extensions import (
    input_mapper,
    output_mapper,
    cli_format_mapper,
    register_output_file,
    sources_mapper,
    software_versions
)

SOFTWARE = 'formable'

input_mapper = partial(input_mapper, software=SOFTWARE)
output_mapper = partial(output_mapper, software=SOFTWARE)
cli_format_mapper = partial(cli_format_mapper, software=SOFTWARE)
register_output_file = partial(register_output_file, software=SOFTWARE)
sources_mapper = partial(sources_mapper, software=SOFTWARE)
software_versions = partial(software_versions, software=SOFTWARE)

# This import must come after assigning the partial functions:
from matflow_formable import main
from matflow_formable import load